---
name: checklist-onboarding
description: Construiește un checklist de onboarding pentru un angajat nou, grupat pe săptămâni (înainte de prima zi, săptămâna 1, săptămâna 2-4), fiecare task cu responsabil. Folosește-l când cineva spune „fă-mi un plan de onboarding", „checklist pentru noul angajat", „ce pregătim pentru prima zi a lui X", „onboarding pentru rolul Y", „plan de integrare". Pornește de la rol și context real; marchează ce depinde de firmă ca „de confirmat", nu inventează conturi/acces specifice.
---

# Checklist de onboarding (checklist-onboarding)

Transformă „avem un om nou luni" într-un plan concret și etapizat: ce se pregătește înainte de prima zi, ce se face în săptămâna 1, ce se urmărește în primele 30 de zile — fiecare task cu un responsabil. Greul e să acoperi cele trei dimensiuni (administrativ/acces, social/echipă, rol/learning) fără să presupui detalii pe care doar firma le știe. Nu folosi acest skill pentru a scrie fișa rolului (vezi `generator-fisa-post`) sau pentru a compara candidați (vezi `comparator-fise-rol`).

## Input
- Rolul și echipa noului angajat (ideal o fișă de post existentă).
- Opțional: data începerii, cine e managerul/buddy, instrumentele firmei.

## Metodă
1. Pornește de la rol: ce trebuie să poată face persoana, deci ce acces/unelte/cunoștințe îi trebuie.
2. Acoperă trei axe pentru fiecare etapă: **administrativ** (contract, conturi, acces), **social** (prezentări, buddy, echipă), **rol** (primul task mic, documentația de citit, cu cine vorbește).
3. Grupează pe etape: **Înainte de prima zi**, **Săptămâna 1**, **Săptămânile 2-4**.
4. Pune un **responsabil** pe fiecare task (HR, manager, IT, buddy). Dacă nu se știe, „de atribuit".
5. Marchează ce depinde de specificul firmei (ce conturi exacte, ce sisteme) ca „de confirmat" — nu inventa nume de sisteme.
6. Adaugă un **check de final de lună**: ce ar trebui să poată face persoana singură până atunci.

## Output (obligatoriu)
Un checklist în `outputs/` (ex. `outputs/onboarding-<rol>.md`):

```
# Onboarding — <rol> — start: <data / de confirmat>

## Înainte de prima zi
- [ ] <task> — responsabil: <…>

## Săptămâna 1
- [ ] <task> — responsabil: <…>

## Săptămânile 2-4
- [ ] <task> — responsabil: <…>

## La 30 de zile — ar trebui să poată
- <…>

## De confirmat / de atribuit
- <ce depinde de firmă sau n-are încă responsabil>
```

## Disciplină (firul roșu)
- Nu inventa sisteme, conturi sau proceduri specifice firmei. Ce nu știi → „de confirmat".
- Fiecare task are un responsabil real; lipsa se scrie „de atribuit", nu se pune la întâmplare.
- Datele (prima zi, termene) se trec doar dacă sunt date; altfel „de confirmat".
- Checklistul e o schiță pe care HR/managerul o ajustează la realitatea firmei înainte de a-l folosi.
