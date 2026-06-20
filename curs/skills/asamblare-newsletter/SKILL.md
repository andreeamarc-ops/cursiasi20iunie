---
name: asamblare-newsletter
description: Asamblează un newsletter curat dintr-un folder de fragmente, linkuri și notițe — selectează, ordonează și leagă materialele într-o ediție coerentă cu subiect, intro și secțiuni. Folosește-l când cineva spune „fă-mi newsletterul din folderul ăsta", „asamblează ediția de săptămâna asta", „strânge linkurile astea într-un newsletter", „compune buletinul", „ediție de newsletter din fragmente". Nu inventează conținut: tot ce intră vine din materialele date.
---

# Asamblare newsletter (asamblare-newsletter)

Ia un folder dezordonat de fragmente — linkuri, notițe, ciorne de paragrafe, un citat, o veste — și le compune într-o ediție de newsletter ordonată: subiect, intro, secțiuni, CTA. Greul e curatoria (ce intră, ce rămâne pe dinafară) și ordonarea (ce e cap de afiș, ce e nota de subsol), nu scrierea de la zero. Nu folosi acest skill pentru a planifica ce postezi pe rețele (vezi `calendar-content`) sau pentru a adapta un mesaj pe canale (vezi `variante-postari`).

## Input
- Un folder cu fragmente: linkuri, notițe, ciorne, citate, imagini referite.
- Opțional: tema ediției și publicul (ajustează ce selectezi și tonul).

## Metodă
1. Inventariază folderul: ce fragmente există, ce tip e fiecare (știre, link, citat, anunț propriu).
2. Selectează ce intră în ediție pe baza temei/relevanței; pune restul într-o listă „rămas pe dinafară" (nu le pierde, ca omul să decidă).
3. Ordonează: cel mai puternic element sus (cap de afiș), apoi secundarele, anunțul propriu la final cu CTA.
4. Scrie un **subiect** (atrăgător, onest) și un **intro** scurt și personal care leagă ediția.
5. Pentru fiecare element păstrează **linkul/sursa** exact cum e în fragment — nu rescrie URL-uri din memorie.
6. Marchează orice fragment incomplet (link lipsă, citat fără autor) ca „de completat".

## Output (obligatoriu)
O ediție în `outputs/` (ex. `outputs/newsletter-<data>.md`):

```
Subiect: <…>

<Intro — 2-4 propoziții, personal>

## <Titlu secțiune principală>
<text> — [link]

## <Secțiuni secundare>
- <element> — [link]

## <Anunț propriu / CTA>
<…>

---
Rămas pe dinafară (de decis): <fragmente neincluse>
De completat: <fragmente cu link/sursă lipsă>
```

## Disciplină (firul roșu)
- **Nu inventa știri, citate, linkuri sau autori.** Tot ce intră vine din fragmentele din folder; sursele se copiază, nu se reconstruiesc din memorie.
- Fragmentele incomplete se marchează „de completat", nu se „repară" cu detalii presupuse.
- Ce nu intră nu se șterge — ajunge în „rămas pe dinafară", ca omul să aibă ultimul cuvânt.
- Ediția e o schiță gata de revizuit; omul aprobă și apasă „trimite" (regula automatizării — asamblezi, nu trimiți).
