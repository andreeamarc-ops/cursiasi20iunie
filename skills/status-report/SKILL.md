---
name: status-report
description: Construiește un status report săptămânal/de sprint dintr-un folder de proiect — ce s-a făcut, ce e în lucru, ce e blocat, ce urmează — fiecare punct ancorat în fișierul din care vine. Folosește-l când cineva spune „fă-mi un status report", „raportul de săptămâna asta", „unde suntem cu proiectul", „status de sprint", „sumar de progres pentru echipă". Nu inventează progres: ce nu e dovedit într-un fișier ajunge la „de verificat".
---

# Status report de proiect (status-report)

Strânge starea unui proiect dintr-un folder de fișiere și o pune într-un raport scurt, citabil, pe care echipa și șeful îl pot citi în două minute. Greul e să distingi *ce s-a făcut cu adevărat* (există un fișier, un commit, o decizie scrisă) de *ce și-ar dori cineva să fie făcut*. Nu folosi acest skill pentru a urmări doar riscurile (vezi `risk-tracker`), pentru un brief către stakeholderi externi (vezi `brief-stakeholderi`) sau pentru a extrage acțiuni dintr-o singură ședință (vezi `extragere-actiuni-sedinta`).

## Input
- Un folder de proiect (notițe, acțiuni, fișiere de lucru, drafturi).
- Opțional: raportul anterior, ca să arăți doar ce s-a schimbat.

## Metodă
1. Indexează folderul: ce fișiere există, ce conțin, când par modificate ultima oară.
2. Sortează fiecare element în patru găleți: **Făcut**, **În lucru**, **Blocat**, **Urmează**.
3. Pune ceva la „Făcut" **doar** dacă există dovadă în fișier (un livrabil, o decizie scrisă, un task bifat). Altfel e „În lucru".
4. La „Blocat", numește **cauza** și **cine/ce deblochează** — nu doar „e blocat".
5. La „Urmează", listează doar pașii care reies din folder, nu o listă de dorințe.
6. Ancorează fiecare punct: din ce fișier vine.

## Output (obligatoriu)
Un raport în `outputs/` (ex. `outputs/status-<proiect>-<data>.md`), cu această structură:

```
# Status — <proiect> — <data>
Pe scurt: <2-3 propoziții, ce contează acum>

## Făcut
- <punct> — sursă: <fișier>

## În lucru
- <punct> (responsabil dacă se știe) — sursă: <fișier>

## Blocat
- <punct> — cauză: <…> — deblochează: <cine/ce> — sursă: <fișier>

## Urmează
- <pas> — sursă: <fișier>

## De verificat
- <ce n-a putut fi confirmat din fișiere>
```

## Disciplină (firul roșu)
- Fiecare punct e ancorat în **fișierul din care vine**. Niciun progres „din amintire".
- Nu umfla raportul: dacă un fișier nu spune că ceva e gata, nu îl trece la „Făcut".
- Procentajele („80% gata") se trec doar dacă apar într-un fișier; altfel evită-le sau marchează-le „de verificat".
- Secțiunea „De verificat" e obligatorie — acolo pui tot ce sună adevărat dar nu ai putut ancora.
