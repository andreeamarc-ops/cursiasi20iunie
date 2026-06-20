---
name: verificare-firma-anaf
description: Verifică o firmă românească (sau o listă întreagă) direct la ANAF, după CUI — stare activ/inactiv/radiat, plătitor de TVA, denumire oficială și adresă — folosind serverul MCP public demoanaf.ro. Folosește-l când cineva spune „verifică firma asta la ANAF", „e plătitoare de TVA?", „mai e activă firma cu CUI…", „verifică-mi lista de clienți la ANAF", „validează CUI-urile astea" sau vrea să confirme date de facturare înainte să emită o factură. Sursa de adevăr e ANAF, nu fișierul.
---

# Verificare firmă la ANAF (verificare-firma-anaf)

Folosește acest skill când ai un CUI (sau o listă de CUI-uri) și vrei starea **reală, oficială** a firmei — nu ce a
scris cineva într-un formular. Partea care contează: datele dintr-un fișier (nume, „pare activ", „plătitor de TVA")
pot fi greșite sau învechite; **ANAF e sursa de adevăr.** E exact reflexul 4 cu un serviciu real: nu presupui, ci
**întrebi sursa**. Util mai ales înainte de facturare (plătitor de TVA sau nu schimbă factura).

## Cerință: conexiunea MCP la ANAF
Acest skill are nevoie de serverul MCP **`https://demoanaf.ro/mcp`** conectat în Cowork (o alternativă publică și
gratuită la anaf.ro, peste datele oficiale ANAF/ONRC/BNR). Conectarea se face o dată (vezi Cursul 10). Dacă nu e
conectat, skill-ul spune clar „nu pot verifica live — conectează întâi MCP-ul ANAF" și **nu inventează** stări.

## Input
- Un CUI sau o listă (ex. coloana `cui` din `scenarii/clienti-anaf/clienti.csv`).
- Opțional: ce verifici (doar TVA, sau stare completă).

## Metodă
1. **Citește lista** de CUI-uri din fișier (păstrează și `nume_din_formular` / `status_presupus`, ca să le compari).
2. **Pentru fiecare CUI, întreabă ANAF** prin MCP: denumire oficială, stare (activ / inactiv / radiat), înregistrat
   în scop de TVA (da/nu, de când), TVA la încasare / split TVA dacă e cazul, adresă/CAEN dacă e disponibil.
3. **Compară cu fișierul.** Marchează **nepotrivirile**: nume din formular ≠ denumire oficială; „activ" presupus dar
   radiat la ANAF; „plătitor TVA" presupus dar nu e (sau invers).
4. **CUI invalid / negăsit** → marchează explicit „negăsit la ANAF — de verificat", nu ghici.
5. **Nu acționa.** Skill-ul *raportează*; nu emite facturi, nu modifică date de client — omul decide ce face cu
   nepotrivirile.

## Output (obligatoriu)
Un tabel în `outputs/` cu, pe fiecare firmă: `CUI · denumire oficială (ANAF) · stare · plătitor TVA · nepotrivire
față de formular · de făcut`. La final, o listă scurtă „**De rezolvat înainte de facturare**" (firme radiate,
CUI-uri invalide, statut TVA diferit).

## Disciplină (firul roșu)
Fiecare stare vine **live de la ANAF**, nu din `status_presupus` și nu din memorie. Dacă MCP-ul nu e conectat sau
o firmă nu se găsește, scrii „neverificat / negăsit" — niciodată o stare inventată. Tu raportezi; **omul decide**
ce face cu un client radiat sau cu un CUI invalid (nu refuza/nu factura nimic automat în numele lui).
