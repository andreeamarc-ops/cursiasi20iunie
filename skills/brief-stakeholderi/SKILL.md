---
name: brief-stakeholderi
description: Transformă starea internă a unui proiect într-un brief scurt, fără jargon, pentru stakeholderi (șef, client, board, investitor). Folosește-l când cineva spune „fă-mi un brief pentru șef/client", „update pentru stakeholderi", „rezumat pentru board", „cum explic asta non-tehnic", „o pagină pentru investitor". Traduce detaliul intern în limbaj clar, dar nu inventează rezultate sau date pe care fișierele nu le susțin.
---

# Brief pentru stakeholderi (brief-stakeholderi)

Ia starea internă (zgomotoasă, tehnică) a unui proiect și o condensează într-un brief scurt pe care un stakeholder ocupat și non-tehnic îl înțelege în 60 de secunde. Greul nu e să scurtezi — e să traduci jargonul în mize reale („de ce-i pasă cititorului") fără să pierzi adevărul și fără să maschezi veștile proaste. Nu folosi acest skill pentru raportul intern detaliat al echipei (vezi `status-report`) sau pentru registrul de riscuri (vezi `risk-tracker`).

## Input
- Starea proiectului: un `status-report`, un folder de proiect, sau notițe.
- Opțional: cine e stakeholderul și ce decizie are de luat (ajustează tonul și ce evidențiezi).

## Metodă
1. Pornește de la sursele interne și extrage doar ce **contează pentru cineva din afara echipei**: progres vizibil, riscuri care îi afectează, decizii pe care le aștepți de la el.
2. Tradu fiecare element tehnic în limbaj de business: nu „am refactorizat modulul de plăți", ci „plățile sunt acum mai stabile, gata de testat cu clienți".
3. Spune clar **veștile bune și pe cele proaste** — un brief care ascunde un blocaj e inutil. Încadrează blocajul cu ce e nevoie ca să se rezolve.
4. Termină cu o secțiune **„Ce-ți cerem"** (o decizie, o aprobare, o resursă) — sau „Nimic acum, doar pentru informare".
5. Ține-l la o pagină. Dacă nu încape, e prea lung.

## Output (obligatoriu)
Un brief în `outputs/` (ex. `outputs/brief-<stakeholder>-<data>.md`):

```
# <Proiect> — pe scurt pentru <stakeholder> — <data>

**Unde suntem:** <2-3 propoziții, fără jargon>
**Ce merge bine:** <2-3 puncte>
**Ce ne dă bătăi de cap:** <1-2 puncte + ce e nevoie>
**Ce-ți cerem:** <decizie/aprobare/resursă — sau „nimic acum">
**Pentru detalii:** <link/fișier intern>
```

## Disciplină (firul roșu)
- Brief.ul se sprijină pe surse interne reale. Nu inventa metrici de impact, procente sau rezultate ca să sune bine.
- „Simplu" nu înseamnă „înfrumusețat": dacă un risc e real, apare în brief, nu se șterge pentru ton.
- Cifrele citate se trag din fișiere; ce nu poți ancora marchezi „de verificat" (intern), nu îl pui în brief ca fapt.
- Brief.ul rămâne o schiță pe care omul o citește înainte să-l trimită — el deține mesajul către stakeholder.
