# clienti-anaf/ — clienții de verificat la ANAF (Nordica, fictiv)

`clienti.csv` — o listă de firme-client ale Nordicăi, așa cum au fost completate în formularele de facturare:
`nume_din_formular`, `cui`, `oras_declarat`, `plan`, `status_presupus`. Folosită la **Cursul 10** (conectarea unui
instrument), de skill-ul `verificare-firma-anaf` (Legal Kit), pentru a verifica **automat** fiecare firmă direct la
**ANAF** prin MCP (serviciul real `https://demoanaf.ro/mcp`): denumire oficială, stare (activ/inactiv), plătitor de
TVA, adresă.

**Important (firul roșu — reflexul 4):** coloanele `nume_din_formular` și `status_presupus` sunt ce a *scris
clientul în formular* — pot fi greșite, abreviate sau învechite. **ANAF e sursa de adevăr, nu fișierul.** Sarcina e
să iei starea reală de la ANAF și să **semnalezi nepotrivirile**.

## CUI-uri reale — datele vin live de la ANAF

CUI-urile din listă sunt **CUI-uri reale, publice**, alese ca lookup-ul să întoarcă date adevărate în timpul
cursului. **Nu presupune rezultatul** — se ia live de la ANAF; datele oficiale se pot schimba în timp. Numele de pe
firme și `status_presupus` sunt puse intenționat ca să iasă nepotriviri.

Notă pentru trainer — ce întoarce ANAF (verificat la 2026-06-18, prin `demoanaf.ro`), adică unde sunt capcanele:

| CUI | Denumire oficială ANAF | Capcana de semnalat |
|-----|------------------------|---------------------|
| 14837428 | BORG DESIGN SRL | curat — activ, plătitor TVA (control pozitiv) |
| 11198699 | MEGAOIL SRL | curat — activ, plătitor TVA |
| 6300600 | RODINELA IMPORT-EXPORT SRL | **INACTIV** la ANAF, deși formularul zice „activ" → nu factura |
| 13548146 | CUBUS ARTS SRL | **NEPLĂTITOR de TVA**, deși formularul zice „plătitor TVA" → factură fără TVA |
| 199370 | JUDE SI HALBAC SNC | neplătitor TVA — formularul a nimerit-o (control) |
| 14688237 | LOZER EXPRESS SRL | statut TVA fluctuant la verificări — **verifică live** |
| 14399840 | DANTE INTERNATIONAL SA | nume greșit în formular („Dante Internacional") → nepotrivire de denumire |
| 99999999 | — | **negăsit la ANAF** (CUI invalid intenționat) → de verificat manual |

Ideea pentru sală: din 8 „clienți", câțiva au o problemă reală pe care formularul o ascundea (firmă inactivă,
neplătitor de TVA, nume greșit, CUI invalid) — exact de ce verifici la sursă înainte să facturezi.

> **Trainer — reverifică în dimineața cursului.** Datele ANAF sunt vii și se pot schimba (am văzut un CUI
> schimbându-și statutul TVA între două verificări la un minut distanță). Rulează o verificare rapidă înainte de
> sesiune ca să știi ce întoarce fiecare CUI azi — și dacă s-a schimbat ceva, cu atât mai bine: **sursa vie bate
> fișierul**, fix lecția. Endpoint public (același backend ca MCP-ul): `https://demoanaf.ro/api/company/<CUI>`.
