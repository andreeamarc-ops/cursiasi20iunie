---
name: comparator-fise-rol
description: Compară două sau mai multe fișe de post sau CV-uri față de cerințele unui rol, cap la cap, într-un tabel — cine acoperă ce cerință, unde sunt golurile. Folosește-l când cineva spune „compară CV-urile astea pentru rolul X", „pune candidații cap la cap", „care fișă de post acoperă cerințele", „tabel comparativ de candidați", „cine se potrivește mai bine". Judecă doar pe baza a ce scrie în documente; nu inventează experiență și nu decide angajarea în locul omului.
---

# Comparator de fișe de post / candidați (comparator-fise-rol)

Pune două sau mai multe documente (fișe de post, CV-uri) cap la cap față de cerințele unui rol și arată clar cine acoperă ce și unde sunt golurile. Greul e să rămâi onest: marchezi „acoperit / parțial / lipsă" **doar** pe baza a ce e scris, fără să citești între rânduri sau să presupui competențe. Nu folosi acest skill pentru a crea fișa postului (vezi `generator-fisa-post`) sau pentru o recenzie critică multi-unghi a unui document deja făcut (vezi `review-cu-subagenti`).

## Input
- Cerințele rolului (o fișă de post sau o listă de criterii must-have / nice-to-have).
- Două sau mai multe documente de comparat (CV-uri sau fișe de post).

## Metodă
1. Extrage din rol lista de **criterii** (must-have și nice-to-have), una pe rând.
2. Pentru fiecare document și fiecare criteriu, marchează: **acoperit** (scrie explicit), **parțial** (atinge tangențial), **lipsă** (nu apare), **neclar** (formulare ambiguă).
3. Ancorează fiecare „acoperit/parțial" în fragmentul din document care îl susține — fără citat, e „neclar", nu „acoperit".
4. Nu presupune: dacă un CV nu menționează o competență, e „lipsă", nu „probabil o are".
5. Sintetizează la final **puncte tari / goluri** per candidat, factual, fără să recomanzi pe cineva ca „cel mai bun".
6. Listează **întrebările de pus la interviu** pentru fiecare „neclar/parțial".

## Output (obligatoriu)
Un tabel + sinteză în `outputs/` (ex. `outputs/comparatie-<rol>.md`):

| Criteriu (must-have) | Candidat A | Candidat B | Ancoră / observație |
|----------------------|-----------|-----------|---------------------|
| 3 ani suport clienți | acoperit | parțial | A: „4 ani help-desk"; B: „internship 6 luni" |
| Română + engleză | acoperit | neclar | B nu menționează engleza |

Sub tabel: **Puncte tari / goluri** per candidat și **Întrebări pentru interviu** (din „neclar/parțial").

## Disciplină (firul roșu)
- Judeci **doar din document**. Lipsa unei mențiuni = „lipsă", nu „probabil are". Fiecare „acoperit" are ancoră citabilă.
- Nu inventa ani de experiență, diplome sau competențe ca să completezi un profil.
- **Nu decizi angajarea.** Output.ul e o comparație factuală; alegerea finală e a omului, după interviu.
- Marchează clar „neclar/de verificat" — sunt exact întrebările pentru interviu, nu goluri de umplut cu presupuneri.
