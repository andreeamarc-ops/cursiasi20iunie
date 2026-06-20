---
name: generator-fisa-post
description: Transformă o descriere brută/dezordonată de rol (un brain-dump al managerului care angajează) într-o fișă de post curată și structurată, folosind șablonul din templates/fisa-postului.md. Folosește-l când cineva spune „fă-mi o fișă de post", „structurează descrierea asta de post", „job spec din notițele astea", „transformă brain-dump-ul ăsta în anunț de angajare", „fișă de post pentru rolul X". Marchează ce nu e specificat ca „de completat" și NU inventează salariu, beneficii sau cerințe.
---

# Generator de fișă de post (generator-fisa-post)

Ia descrierea brută a unui rol — așa cum o aruncă pe hârtie cineva care angajează: dezordonată, cu repetiții, cu lipsuri — și o transformă într-o fișă de post structurată după un șablon fix. Greul e disciplina: completezi din brief ce e acolo, dar **nu inventezi** ce lipsește (mai ales salariu și beneficii) — îl marchezi ca „de completat". Nu folosi acest skill pentru a compara mai multe fișe/CV-uri (vezi `comparator-fise-rol`) sau pentru checklist-ul de onboarding al noului angajat (vezi `checklist-onboarding`).

## Input
- Descrierea brută a rolului (ex. `scenarii/hr-rol/descriere-rol-brut.md`).
- Șablonul de structură: `templates/fisa-postului.md` (secțiunile obligatorii).

## Metodă
1. Citește descrierea brută în întregime și citește șablonul `templates/fisa-postului.md` ca să știi ce secțiuni trebuie umplute.
2. Mapează informația din brief pe secțiunile șablonului: **scop**, **responsabilități**, **profil (must-have)**, **nice-to-have**, **ce oferim**.
3. Curăță și grupează: scoate repetițiile, transformă propoziții vagi în responsabilități concrete (verb + obiect).
4. Separă onest **must-have** de **nice-to-have** — nu urca o preferință la cerință obligatorie dacă brieful nu o cere.
5. Pentru orice secțiune pe care brieful nu o acoperă (salariu, beneficii, locație, raportare), scrie **„de completat"** — nu umple cu valori plauzibile.
6. Adună toate lipsurile într-o secțiune finală **„De completat"**, ca omul care angajează să le închidă rapid.

## Output (obligatoriu)
O fișă de post completată după `templates/fisa-postului.md`, salvată în `outputs/` (ex. `outputs/fisa-post-<rol>.md`), cu secțiunile: Rol/echipă/raportare, **Scop**, **Responsabilități**, **Profil (must-have)**, **Nice-to-have**, **Ce oferim**, și o secțiune finală **„De completat"** care listează tot ce brieful nu a specificat.

## Disciplină (firul roșu)
- **Nu inventa salariu, beneficii, niveluri sau cerințe.** Ce nu e în brief → „de completat", niciodată o cifră sau o clauză plauzibilă scoasă din cap.
- Nu promova o preferință la „obligatoriu": must-have vs. nice-to-have reflectă exact ce spune brieful.
- Responsabilitățile se sprijină pe ce e în descriere; nu adăuga sarcini „tipice rolului" pe care managerul nu le-a numit.
- Fișa e o schiță: omul care angajează completează lipsurile și aprobă înainte de publicarea anunțului.
