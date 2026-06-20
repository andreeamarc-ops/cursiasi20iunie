---
name: organizator-furnizori
description: Strânge informații de furnizori împrăștiate prin emailuri, oferte și notițe într-un registru curat și comparabil. Folosește-l când cineva spune „organizează-mi furnizorii", „fă-mi un registru de furnizori", „adună datele furnizorilor într-un tabel", „am informații împrăștiate despre furnizori", „pune furnizorii cap la cap" sau are date neuniforme despre mai mulți furnizori și vrea un singur tabel ordonat. Nu evaluează și nu recomandă — doar normalizează și aliniază; ce lipsește e marcat „—".
---

# Organizator de furnizori (organizator-furnizori)

Adună date de furnizori risipite (emailuri, PDF-uri de ofertă, notițe) și le pune într-un registru unic, cu aceleași coloane pentru toți, ca să poată fi comparați mai târziu. Partea care nu e trivială: normalizează formate diferite (preț cu/fără TVA, monede, termene scrise diferit) fără să inventeze ce lipsește — golurile rămân goluri vizibile. Nu îl folosi ca să decizi un câștigător pe un caiet de sarcini (acolo e `comparator-oferte`) și nici ca să scoți clauze dintr-un singur contract (acolo e `extractor-clauze`).

## Input
- Mai multe surse de date despre furnizori: emailuri, oferte, notițe, fișiere separate (de ex. din `scenarii/oferte-furnizori/`).
- Opțional: coloanele dorite în registru (dacă nu, folosește setul standard de mai jos).

## Metodă
1. Identifică fiecare furnizor distinct și adună tot ce ai despre el din toate sursele.
2. Stabilește un set comun de coloane (ex. furnizor · contact · produs/serviciu · preț · monedă/TVA · termen livrare · SLA · note).
3. Normalizează valorile la același format (aceeași monedă unde poți, preț cu mențiune TVA, termene în zile). Spune ce ai normalizat.
4. Pentru câmpurile fără sursă, pune „—" (gol vizibil), nu o presupunere.
5. Semnalează inconsecvențele între surse pentru același furnizor (ex. două prețuri diferite în două emailuri).

## Output (obligatoriu)
- **Registru de furnizori:** un singur tabel, o linie per furnizor, coloane uniforme, „—" la ce lipsește.
- **Note de normalizare:** ce ai convertit/aliniat (monede, TVA, termene).
- **Inconsecvențe:** unde aceeași informație apare diferit în surse, cu trimitere la fiecare sursă.

## Disciplină (firul roșu)
Fiecare celulă vine dintr-o sursă reală; ce nu există rămâne „—", niciodată completat din presupunere. Nu armonizezi tăcut date care se contrazic — le pui pe ambele și semnalezi conflictul, ca omul să decidă care e corectă. Nu clasezi și nu recomanzi furnizori aici — registrul e doar materia primă curată pentru o decizie ulterioară a omului.
