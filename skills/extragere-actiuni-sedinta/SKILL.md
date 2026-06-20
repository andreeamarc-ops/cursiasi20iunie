---
name: extragere-actiuni-sedinta
description: Transformă notițe brute sau un transcript de ședință într-un tabel curat de acțiuni (task, responsabil, termen), fiecare ancorată în linia din sursă care a generat-o. Folosește-l când cineva spune „scoate-mi acțiunile din ședință", „fă-mi un to-do din notițele astea", „cine ce face din transcriptul ăsta", „extrage action items", „minuta cu responsabili și termene". Marchează clar acțiunile fără responsabil sau fără dată ca „de clarificat" — nu inventează niciuna.
---

# Extragere acțiuni din ședință (extragere-actiuni-sedinta)

Scoate deciziile acționabile dintr-o ședință haotică și le pune într-un tabel pe care echipa îl poate urmări. Partea grea nu e să rezumi — e să separi *acțiunile reale* (cineva trebuie să facă ceva) de discuții, opinii și divagații, fără să atribui responsabili sau termene pe care nimeni nu i-a numit. Nu folosi acest skill pentru a urmări riscuri/blocaje (vezi `risk-tracker`) sau pentru un status general de proiect (vezi `status-report`).

## Input
- Un fișier cu notițe de ședință și/sau un transcript (de obicei `.md` sau `.txt`).
- Opțional: lista participanților, ca să poți potrivi prenume cu responsabili.

## Metodă
1. Citește tot fișierul o dată, cap-coadă, înainte să extragi ceva. Nu te apuca de la prima linie.
2. Marchează fiecare loc unde cineva **se angajează la o acțiune** sau **i se cere una** („mă ocup eu de…", „Ioana trimite…", „trebuie făcut până vineri").
3. Pentru fiecare acțiune notează: **ce** (verb + obiect, concret), **cine** (responsabil), **până când** (termen).
4. Ancorează fiecare rând: citează scurt linia/fragmentul din sursă care a generat acțiunea. Dacă nu poți cita, nu e acțiune — scoate-o.
5. Dacă lipsește responsabilul sau termenul, **nu-l ghici**. Pune „—" și marchează rândul „de clarificat".
6. Nu fuziona două acțiuni într-una și nu sparge una în trei. Un angajament = un rând.

## Output (obligatoriu)
Un tabel salvat în `outputs/` (ex. `outputs/actiuni-<sedinta>.md`):

| # | Acțiune | Responsabil | Termen | Ancoră în sursă | Stare |
|---|---------|-------------|--------|-----------------|-------|
| 1 | Trimite specul de plăți către dev | Ioana | 12 iun | „mă ocup eu de specul de plăți, până vineri" | ok |
| 2 | Decide furnizorul de SMS | — | — | „rămâne să stabilim cine ne dă SMS-urile" | de clarificat |

Sub tabel, o secțiune scurtă **„De clarificat"** care listează doar rândurile incomplete, ca omul să le închidă rapid.

## Disciplină (firul roșu)
- Fiecare acțiune trebuie să aibă o **ancoră citabilă** din sursă. Fără ancoră → nu intră în tabel.
- Nu inventa responsabili, termene sau acțiuni „logice" pe care nimeni nu le-a spus. Lipsa se scrie „de clarificat", nu se completează din cap.
- Termenele vagi („cât de curând", „săptămâna viitoare") se trec ca atare, nu le converti în date exacte de unul singur — marchează-le „de verificat".
- Tabelul e o schiță pentru om: responsabilii și termenele se confirmă cu oamenii reali înainte să devină angajamente.
