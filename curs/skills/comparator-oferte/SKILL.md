---
name: comparator-oferte
description: Compară două sau mai multe oferte de furnizor față de un caiet de sarcini, cap la cap, marcând fiecare cerință OBLIGATORIE ca trecută/picată per ofertă și DESCALIFICÂND orice ofertă care pică o cerință obligatorie — chiar dacă e cea mai ieftină — apoi recomandă cu rezerve. Folosește-l când cineva spune „compară ofertele astea", „care furnizor să-l aleg", „pune ofertele cap la cap pe caietul de sarcini", „care e cea mai bună ofertă", „evaluează furnizorii" sau are mai multe oferte și un set de cerințe. Cea mai ieftină nu câștigă automat: o cerință obligatorie nerespectată descalifică oferta.
---

# Comparator de oferte (comparator-oferte)

Așază 2+ oferte de furnizor lângă un caiet de sarcini și produce un tabel comparativ în care fiecare cerință **obligatorie** primește pass/fail per ofertă. Partea care nu e trivială și care e tot rostul skill-ului: o ofertă care pică **fie și o singură** cerință obligatorie este **descalificată**, oricât de ieftină ar fi — prețul mic nu salvează o cerință lipsă (ex. „fără suport în limba română"). Recomandarea vine doar dintre ofertele care trec toate obligatoriile, cu rezervele de rigoare. Nu îl folosi doar pentru a extrage clauze dintr-un singur contract (acolo e `extractor-clauze`) și nici pentru a curăța o listă de furnizori (acolo e `organizator-furnizori`).

## Input
- Un `caiet-de-sarcini.md` (cerințele), cu cerințele obligatorii marcate sau identificabile.
- Două sau mai multe oferte (`scenarii/oferte-furnizori/`), fiecare cu preț, funcționalități, SLA, suport etc.
- Opțional: ponderi pentru criteriile neobligatorii (preț, termen, SLA).

## Metodă
1. Citește caietul de sarcini și fă o listă a cerințelor, separând clar **obligatorii (must)** de **opționale/dezirabile (nice-to-have)**.
2. Pentru fiecare ofertă, verifică fiecare cerință și marchează ✅ trece / ❌ pică / ⚠️ neclar — citând fraza din ofertă pe care te bazezi.
3. **Aplică regula de descalificare:** orice ofertă cu un ❌ pe o cerință **obligatorie** e marcată DESCALIFICATĂ, indiferent de preț. Spune explicit care cerință a picat.
4. Dintre ofertele rămase calificate, compară pe criteriile opționale (preț, termen, SLA) și recomandă una.
5. Scrie rezervele: ce e „neclar" (⚠️) și trebuie confirmat cu furnizorul înainte de semnătură.

## Output (obligatoriu)
- **Tabel comparativ:** rânduri = cerințe (obligatoriile grupate sus), coloane = oferte, celule = ✅/❌/⚠️ + nota scurtă cu sursa.
- **Verdict de calificare:** care oferte sunt DESCALIFICATE și pentru ce cerință obligatorie.
- **Recomandare cu rezerve:** oferta propusă dintre cele calificate + de ce, plus lista de „⚠️ de confirmat".
- Dacă cea mai ieftină e descalificată, spune-o pe față: „X e cea mai ieftină dar pică [cerință] → descalificată".

## Disciplină (firul roșu)
Fiecare pass/fail trimite la o frază concretă din ofertă sau din caietul de sarcini — fără presupuneri. Regula obligatoriilor nu se negociază: o cerință must nerespectată descalifică, chiar dacă rezultatul „te încurcă" la preț. Ce nu e scris clar în ofertă rămâne ⚠️ „de confirmat cu furnizorul", nu se trece la pass din optimism. Recomandarea e o propunere pentru om — decizia de achiziție și semnătura rămân ale lui.
