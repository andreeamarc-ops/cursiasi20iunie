---
name: extractor-clauze
description: Extrage clauzele și termenii cheie dintr-un contract sau o ofertă — preț, durată/termen, SLA, penalități, condiții de ieșire/reziliere — într-un tabel structurat, citând fraza-sursă pentru fiecare. Folosește-l când cineva spune „scoate-mi clauzele din contractul ăsta", „ce scrie despre penalități/reziliere/SLA", „termenii cheie ai ofertei", „rezumă-mi contractul pe puncte", „ce mă obligă contractul ăsta" sau vrea termenii importanți dintr-un singur document. Nu interpretează juridic și nu inventează clauze: ce nu e în text e marcat „neprecizat în document".
---

# Extractor de clauze (extractor-clauze)

Citește un singur contract sau ofertă și scoate termenii care contează — preț, durată, SLA, penalități, ieșire — într-un tabel, fiecare însoțit de fraza exactă din document. Partea care nu e trivială: nu confundă lipsa unei clauze cu o clauză favorabilă — ce nu e scris e marcat explicit „neprecizat", ca omul să știe ce trebuie negociat. Nu îl folosi pentru a compara mai multe oferte cu verdict de calificare (acolo e `comparator-oferte`) și nici nu dă opinii juridice (e doar extragere de text).

## Input
- Un singur document: contract sau ofertă (text/PDF/Markdown).
- Opțional: o listă proprie de clauze de căutat (peste setul standard preț/durată/SLA/penalități/ieșire).

## Metodă
1. Parcurge documentul integral și localizează fiecare categorie de termen.
2. Pentru fiecare, extrage valoarea concretă (suma, perioada, procentul, condiția) **și** citează fraza-sursă din care provine.
3. Dacă o categorie nu apare în text, scrie „neprecizat în document" — nu deduce, nu presupune un standard.
4. Marchează clauzele cu risc evident (penalități mari, reziliere unilaterală, reînnoire automată, lock-in) ca „⚠️ de atenționat".
5. Strânge tot într-un tabel ordonat.

## Output (obligatoriu)
- **Tabel de clauze:** categorie (Preț / Durată / SLA / Penalități / Ieșire / alta) · valoare extrasă · frază-sursă citată · ⚠️ dacă e de atenționat.
- **Lipsuri:** lista categoriilor „neprecizat în document".
- **De atenționat:** clauzele cu risc, cu o frază de context fiecare (nu sfat juridic — doar semnalare).

## Disciplină (firul roșu)
Fiecare valoare extrasă are fraza-sursă lângă ea — fără termeni „rezumați din amintire". Lipsa unei clauze se scrie „neprecizat", nu se completează cu un standard inventat. Nu dai interpretare juridică și nu spui „e legal/ok"; semnalezi ce trebuie citit de un om (sau de un jurist) înainte de semnătură. Decizia de a semna rămâne a omului.
