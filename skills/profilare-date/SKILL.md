---
name: profilare-date
description: Profilează un fișier CSV (de ex. scenarii/date/cheltuieli-2026.csv) și scoate un rezumat pe coloane, totaluri/sume pe categorii, semnalează anomalii și produce un grafic HTML de sine stătător în outputs/. Folosește-l când cineva spune „profilează-mi CSV-ul", „fă-mi un rezumat al fișierului de cheltuieli", „cât cheltuim pe Marketing", „totaluri pe categorie", „analizează datele astea", „fă-mi un grafic din tabelul ăsta" sau când vrei să verifici o cifră „din memorie" calculând suma reală din fișier. Calculează sume reale din date — corectează orice ghicitură ținută minte.
---

# Profilare de date & grafic (profilare-date)

Ia un fișier tabelar (CSV) și îl transformă într-un profil onest: ce conține fiecare coloană, ce se adună la cât pe categorii, ce arată ciudat, plus un grafic HTML **interactiv** (cu filtrare și sortare) pe care îl poți deschide direct în browser. Partea care nu e trivială: **calculează sumele reale din fișier și corectează orice cifră „din memorie"** dintr-un draft sau email — nu repetă ghicitura, ci o înlocuiește cu adevărul din date. Nu îl folosi ca să explici de ce diferă planul de realizat (acolo e `explicator-variatii`) și nici ca să cauți greșeli de tip duplicat/câmp lipsă într-o listă de cheltuieli (acolo e `verificator-cheltuieli`).

**Acest skill nu e doar un prompt — vine la pachet cu o bucată de cod** (`scripts/profil_cheltuieli.py`) care chiar se rulează pe fișier. E exemplul perfect de skill „prompt + cod": instrucțiunile spun *cum* să profilezi datele, iar scriptul *face efectiv* calculul și generează HTML-ul interactiv. (Diferența asta — skill doar-prompt vs. skill prompt+cod — se discută la Cursul 7.)

## Input
- Un fișier CSV (de ex. `scenarii/date/cheltuieli-2026.csv`), menționat cu `@nume-fișier` sau dat ca cale.
- Opțional: ce coloană e categoria și ce coloană e suma (dacă nu e evident din antet, întreabă o dată).
- Opțional: o cifră „din memorie" de verificat (ex. „cred că Marketing-ul a fost ~38.000 lei").

## Metodă
1. Citește fișierul și rulează cod real pe el (nu estima din ochi). Confirmă numărul de rânduri și antetele.
2. **Rulează scriptul la pachet:** `python3 scripts/profil_cheltuieli.py <cale-csv> outputs/grafic-cheltuieli.html` —
   adaugă `--din-memorie 38000 --verifica-categorie Marketing` când vrei să verifici o cifră ținută minte față de
   totalul unei categorii. Scriptul calculează totalurile reale, semnalează anomaliile și scrie HTML-ul interactiv.
   (Dacă scriptul nu poate rula în mediul curent, fă același calcul manual și spune sincer că ai calculat de mână.)
3. **Rezumat pe coloane:** pentru fiecare coloană spune tipul (text/număr/dată), câte valori lipsesc, min/max/sumă unde e numerică, valori distincte unde e categorie.
4. **Totaluri pe categorii:** grupează pe coloana de categorie și însumează coloana de sumă. Dă un tabel sortat descrescător, cu un total general care chiar e suma rândurilor.
5. **Anomalii:** semnalează valori negative neașteptate, outlieri evidenți, dublări de rând, date în afara perioadei, câmpuri goale. Le numești; nu le „repari" singur.
6. **Verifică cifra din memorie:** dacă ai primit una, compar-o explicit cu suma reală calculată. Dacă diferă, scrie negru pe alb: „din memorie X, în fișier Y — corect e Y".
7. **Grafic HTML interactiv:** scriptul scrie în `outputs/` un singur fișier `.html` de sine stătător (fără dependențe externe, fără CDN — totul inline) cu un bar chart al totalurilor pe categorie **plus un tabel cu toate rândurile, care se poate filtra (căsuța de căutare) și sorta (clic pe antet)**. Trebuie să se deschidă cu dublu-clic.

## Output (obligatoriu)
Un mesaj scurt + un fișier HTML:
- **Rezumat pe coloane** (tabel: coloană · tip · valori lipsă · sumă/min/max sau nr. distincte).
- **Totaluri pe categorie** (tabel sortat descrescător + rând TOTAL).
- **Anomalii** (listă cu marcaje, fiecare cu rândul/valoarea concretă).
- **Verificarea cifrei** (dacă a fost cerută): „din memorie X → în fișier Y → corect Y".
- **Graficul:** cale către `outputs/<nume>.html`, bar chart al totalurilor pe categorie **+ tabel interactiv (filtrare + sortare)**.

## Disciplină (firul roșu)
Fiecare cifră din rezultat este o sumă calculată din fișier, nu una ținută minte sau rotunjită „ca să sune bine". Dacă suma reală contrazice un draft sau un email, câștigă fișierul — îl corectezi explicit (ex. Marketing 52.340 lei în fișier vs 38.000 ghicit altundeva). Nu inventa categorii care nu există în date și nu completa câmpuri goale cu presupuneri — le marchezi „de verificat". Graficul reflectă exact totalurile din tabel, nicio cifră nu apare în grafic dacă nu e și în calcul.
