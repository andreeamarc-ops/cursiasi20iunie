---
name: raport-lunar
description: Construiește scheletul unui raport lunar pornind de la date (CSV/tabel) și de la șablonul templates/raport-lunar.md, completând fiecare secțiune cu cifre luate din fișiere. Folosește-l când cineva spune „fă-mi raportul lunar", „pregătește raportul pe luna asta", „completează șablonul de raport", „scrie raportul de status financiar/lunar" sau vrea o ciornă de raport gata structurată din date. Nu inventează nicio cifră — fiecare valoare e ancorată în sursă, restul rămâne „de completat".
---

# Schelet de raport lunar (raport-lunar)

Transformă un set de date plus șablonul `templates/raport-lunar.md` într-o ciornă de raport lunar în care fiecare cifră vine dintr-un fișier. Partea care nu e trivială: respectă fidel structura șablonului și nu lasă goluri tăcute — orice secțiune fără sursă e marcată explicit „de completat de un om", nu umplută cu text de impresie. Nu îl folosi pentru a *explica* de ce au variat cifrele (acolo e `explicator-variatii`) și nici pentru a calcula de la zero totaluri/grafice (acolo e `profilare-date`, pe care îl poți rula înainte).

## Input
- Șablonul `templates/raport-lunar.md` (structura obligatorie a raportului).
- Una sau mai multe surse de cifre: un CSV de cheltuieli/execuție, un tabel de KPI, sau ieșirea de la `profilare-date`.
- Opțional: luna/perioada țintă și note de context (ce s-a întâmplat în lună).

## Metodă
1. Citește șablonul și ia exact secțiunile lui, în ordinea lui. Nu reinventa structura.
2. Citește sursele de date și extrage doar cifrele care se mapează pe secțiuni (totaluri, comparații plan vs realizat, KPI-uri).
3. Completează fiecare secțiune cu cifra + o trimitere scurtă la sursă (ce fișier, ce coloană/rând).
4. Pentru orice secțiune fără sursă în fișiere (ex. „comentariu de management", „context"), pune un marcaj `[de completat de un om]` — nu inventa narațiune.
5. La final, listează ce a rămas „de completat" și de unde ar veni datele lipsă.

## Output (obligatoriu)
Un fișier Markdown în `outputs/` care urmează exact secțiunile din `templates/raport-lunar.md`, cu:
- fiecare cifră însoțită de sursa ei (fișier · coloană/rând),
- secțiunile fără sursă marcate `[de completat de un om]`,
- o listă finală „De completat / de verificat" cu ce lipsește.

## Disciplină (firul roșu)
Nicio cifră nu intră în raport dacă nu e într-un fișier sursă — fără estimări, fără rotunjiri „de prezentare". Comentariile narative care nu se sprijină pe date nu se inventează; se lasă ca marcaj pentru om. Raportul e o ciornă pe care un om o citește, ajustează tonul și o aprobă înainte să plece mai departe — tu nu îl trimiți și nu îl prezinți ca final.
