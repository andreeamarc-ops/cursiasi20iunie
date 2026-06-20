---
name: explicator-variatii
description: Explică în română simplă variațiile dintr-un tabel — planificat vs realizat, sau lună de lună — folosind doar cifrele prezente în tabel. Folosește-l când cineva spune „de ce a crescut/scăzut", „explică-mi diferențele", „planificat vs realizat", „ce s-a schimbat față de luna trecută", „comentează variațiile din tabelul ăsta" sau vrea un comentariu pe diferențe, nu o re-calculare. Nu inventează cauze: descrie ce arată cifrele, iar cauza reală o marchează „de verificat".
---

# Explicator de variații (explicator-variatii)

Ia un tabel cu două coloane comparabile (planificat vs realizat, sau luna curentă vs anterioară) și scrie, în limbaj de coleg, ce s-a schimbat și cât — în lei și în procente. Partea care nu e trivială: separă strict **ce spune cifra** (diferența, sensul, mărimea) de **de ce s-a întâmplat** (cauza), pe care nu o inventează niciodată. Nu îl folosi ca să produci totaluri sau grafice de la zero (acolo e `profilare-date`) și nici ca să umpli un raport întreg (acolo e `raport-lunar`).

## Input
- Un tabel cu cel puțin două coloane de comparat (ex. `planificat`, `realizat`) și o coloană de etichetă (categorie/lună).
- Opțional: un prag de la care o variație contează (ex. „doar peste 5% sau 1.000 lei").
- Opțional: note de context furnizate de om (de la care poți atribui o cauză — doar dacă sunt explicite).

## Metodă
1. Pentru fiecare rând, calculează diferența absolută (realizat − planificat) și procentuală, din cifrele din tabel.
2. Sortează variațiile după mărime; aplică pragul dacă a fost dat, ca să nu îneci semnalul în zgomot.
3. Pentru fiecare variație care contează, scrie o propoziție clară: ce categorie, cât a crescut/scăzut, în lei și %.
4. Adaugă o cauză **doar** dacă există în notele de context primite; altfel scrie „cauză de verificat".
5. Închide cu un rezumat: 2–3 variații care mișcă cel mai mult totalul.

## Output (obligatoriu)
- **Tabel de variații:** etichetă · planificat · realizat · diferență (lei) · diferență (%) · sens (↑/↓).
- **Explicații în proză** (o frază per variație importantă, limbaj simplu).
- **Top 2–3 factori** care mișcă totalul.
- Fiecare cauză e fie ancorată în notele de context, fie marcată „de verificat".

## Disciplină (firul roșu)
Toate diferențele se calculează din cifrele din tabel — nimic estimat. Nu atribui cauze pe care nu le ai în scris („probabil din cauza campaniei" e interzis dacă nu e în note); cauza necunoscută rămâne „de verificat". Descrii ce arată datele, nu inventezi povestea din spatele lor — povestea o confirmă omul care cunoaște contextul.
