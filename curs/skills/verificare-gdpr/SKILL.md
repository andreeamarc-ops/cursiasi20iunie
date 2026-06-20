---
name: verificare-gdpr
description: Verifică un document sau un proces (politică de confidențialitate, formular, flux de date, clauză dintr-un contract) față de elementele de bază GDPR și scoate golurile. Folosește-l când cineva spune „e ok din punct de vedere GDPR", „verifică politica de confidențialitate", „ce date personale colectăm aici", „avem temei legal", „lipsește ceva la protecția datelor" sau pregătește o decizie de tip DPO. NU e aviz juridic — semnalează riscuri și goluri pentru un om.
---

# Verificare GDPR (verificare-gdpr)

Folosește acest skill când vrei să vezi dacă un document sau un flux respectă principiile de bază din GDPR și **ce
lipsește**. Partea grea nu e să citești regulamentul, ci să pui întrebările potrivite despre *datele reale* din
fața ta: ce se colectează, de ce, pe ce temei, cât timp, cu cine se împarte. Nu îl folosi pentru recenzia generală
a unui contract (acolo e `analiza-contract`). **Nu e consultanță juridică** — pregătește o decizie pentru un DPO /
avocat.

## Input
- Documentul/procesul de verificat (politică, formular, descriere de flux, o clauză dintr-un contract).
- Opțional: contextul (cine sunt persoanele vizate — clienți, angajați, clienți finali).

## Metodă
1. **Ce date personale apar?** Listează categoriile (nume, email, telefon, date de plată, date sensibile) și
   **persoanele vizate**.
2. **Temei și scop.** Pentru fiecare colectare: care e scopul și care ar fi temeiul legal (consimțământ, contract,
   obligație legală, interes legitim)? Marchează unde nu reiese.
3. **Principii de bază.** Verifică: minimizare (se colectează doar ce e nevoie?), transparență (e informată
   persoana?), durata păstrării, securitate, drepturile persoanei (acces, ștergere).
4. **Persoane terțe / sub-procesatori.** Cu cine se împart datele? Există un **acord de prelucrare (DPA)**? Unde
   sunt stocate (UE / în afara UE)?
5. **Goluri și riscuri.** Ce lipsește față de pașii de mai sus — listă clară, prioritizată.

## Output (obligatoriu)
Un fișier în `outputs/` cu: (1) tabelul **date colectate → scop → temei**, (2) **Goluri GDPR** (ce lipsește, cu
prioritate), (3) **De clarificat cu DPO/avocat**. Fiecare punct ancorat în textul verificat; ce nu reiese se scrie
„nespecificat în document", nu se presupune.

## Disciplină (firul roșu)
Nu inventa temeiuri legale, durate de păstrare sau practici care nu sunt scrise — absența lor e exact golul de
semnalat. Acesta NU e aviz juridic: e o pregătire pentru decizia unui om responsabil cu protecția datelor. Spune
explicit ce trebuie confirmat de un specialist și nu da niciodată asigurarea „e conform" — dă „iată ce lipsește".
