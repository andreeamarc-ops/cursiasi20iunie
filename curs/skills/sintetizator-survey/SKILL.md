---
name: sintetizator-survey
description: Sintetizează răspunsuri text-liber dintr-un sondaj sau feedback (de la clienți, angajați, participanți) în teme recurente, fiecare cu citate reprezentative din răspunsurile reale. Folosește-l când cineva spune „sintetizează feedbackul ăsta", „ce teme ies din sondaj", „rezumă răspunsurile deschise", „ce zic clienții/angajații", „analiză de survey", „grupează comentariile". Nu inventează sentiment și nu pune procente fără să le numere din date.
---

# Sintetizator de survey / feedback (sintetizator-survey)

Ia un morman de răspunsuri text-liber (zeci/sute de comentarii) și le condensează în câteva teme clare, fiecare ilustrată cu citate reale, ca omul să vadă rapid ce spun de fapt oamenii. Greul e să grupezi fidel (nu să forțezi răspunsuri în teme convenabile) și să nu inventezi un sentiment sau o pondere pe care datele nu o susțin. Nu folosi acest skill pentru a compara documente structurate (vezi `comparator-fise-rol`) sau pentru a extrage acțiuni dintr-o ședință (vezi `extragere-actiuni-sedinta`).

## Input
- Răspunsurile text-liber (un fișier/coloană cu comentarii, un export de sondaj).
- Opțional: întrebarea pusă și cine a răspuns (context pentru interpretare).

## Metodă
1. Citește toate răspunsurile o dată, fără să tragi concluzii, ca să prinzi spectrul.
2. Identifică **temele recurente** — grupuri de răspunsuri care spun același lucru. Lasă o temă „Altele" pentru ce nu se grupează; nu forța nimic.
3. Pentru fiecare temă, alege **2-3 citate reprezentative**, copiate **exact** din răspunsuri (fără a le rescrie ca să sune mai bine).
4. Indică **cât de des** apare tema doar dacă o poți număra („~12 din 40 menționează prețul"); altfel descrie calitativ („mai mulți menționează…"), fără procent inventat.
5. Separă sentimentul pozitiv de cel negativ doar dacă răspunsurile îl exprimă clar; ambiguul rămâne „mixt/neclar".
6. Nu inventa o concluzie generală („toți sunt mulțumiți") pe care datele nu o susțin.

## Output (obligatoriu)
O sinteză în `outputs/` (ex. `outputs/sinteza-survey-<tema>.md`):

```
# Sinteză feedback — <sursă> — <data>
Total răspunsuri analizate: <n>

## Tema 1: <nume>  (frecvență: <x din n / „mai mulți">)
Citate:
- „<citat exact>"
- „<citat exact>"

## Tema 2: …

## Semnale izolate (1-2 mențiuni, dar notabile)
- …

## De verificat
- <ce nu a putut fi numărat sau e ambiguu>
```

## Disciplină (firul roșu)
- **Citatele sunt exacte**, copiate din răspunsuri — nu parafrazate ca să sune mai clar.
- **Nu inventa procente.** O frecvență se trece doar dacă e numărată din date; altfel formulare calitativă onestă.
- Nu atribui sentiment unde nu există: ambiguul rămâne „mixt/neclar", nu îl împingi spre pozitiv sau negativ.
- Sinteza e materie primă pentru decizia omului; concluziile despre „ce facem cu asta" îi aparțin lui.
