---
name: risk-tracker
description: Extrage și urmărește riscurile și blocajele dintr-un set de notițe/fișiere de proiect — fiecare cu severitate, responsabil și stare — ancorate în sursă. Folosește-l când cineva spune „fă-mi un risk tracker", „ce riscuri avem", „lista de blocaje", „ce ne poate sări în aer la lansare", „registru de riscuri", „issue log". Nu inventează riscuri ipotetice: urmărește doar ce e numit în fișiere, marcând restul „de evaluat".
---

# Tracker de riscuri și blocaje (risk-tracker)

Scoate la suprafață riscurile și blocajele îngropate prin notițe de ședință, drafturi și emailuri, și le ține într-un registru cu severitate, responsabil și stare. Partea grea: să prinzi riscul real menționat în treacăt („dacă nu vine API-ul de plăți la timp…") fără să inventezi un catalog de pericole teoretice pe care nimeni nu le-a ridicat. Nu folosi acest skill pentru status general de proiect (vezi `status-report`) sau pentru acțiuni operaționale dintr-o ședință (vezi `extragere-actiuni-sedinta`).

## Input
- Unul sau mai multe fișiere de proiect (notițe, transcripturi, drafturi, emailuri).
- Opțional: registrul de riscuri anterior, ca să actualizezi stările.

## Metodă
1. Citește toate fișierele și marchează fiecare loc unde apare un **risc** („există pericolul…", „dacă X atunci Y") sau un **blocaj** („nu putem continua până…").
2. Pentru fiecare, notează: **descrierea**, **impactul** (ce se strică dacă se întâmplă), **responsabilul** (cine îl gestionează), **starea** (deschis / în lucru / închis).
3. Atribuie o **severitate** (mare / medie / mică) pe baza impactului descris în sursă — nu pe intuiție. Dacă sursa nu lasă să se vadă severitatea, pune „de evaluat".
4. Separă **riscurile** (s-ar putea întâmpla) de **blocajele** (deja te oprește acum).
5. Ancorează fiecare rând în fragmentul din sursă.
6. Dacă același risc apare în mai multe fișiere, fă un singur rând și listează toate sursele.

## Output (obligatoriu)
Un registru în `outputs/` (ex. `outputs/riscuri-<proiect>.md`):

| # | Tip | Risc / Blocaj | Impact | Severitate | Responsabil | Stare | Ancoră în sursă |
|---|-----|---------------|--------|------------|-------------|-------|-----------------|
| 1 | Risc | Întârzie API-ul de plăți | Lansarea slipuiește | Mare | Ioana | Deschis | „dacă nu vine plata la timp, nu lansăm" |
| 2 | Blocaj | Lipsește contractul de SMS | Nu testăm notificările | Medie | — (de clarificat) | Deschis | „așteptăm contractul de la furnizor" |

## Disciplină (firul roșu)
- Urmărești doar riscuri/blocaje **numite în fișiere**, fiecare cu ancoră citabilă. Nu genera o listă „generală de riscuri de proiect".
- Severitatea se justifică din impactul scris în sursă; dacă nu există, e „de evaluat", nu o cifră inventată.
- Responsabilul lipsă → „de clarificat", nu ghicit.
- Registrul e o schiță: severitățile și prioritizarea se confirmă cu echipa.
