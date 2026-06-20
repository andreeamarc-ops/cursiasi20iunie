---
name: verificator-cheltuieli
description: Verifică o listă de cheltuieli pentru probleme — duplicate, câmpuri lipsă, articole în afara politicii și totaluri care nu se adună. Folosește-l când cineva spune „verifică-mi cheltuielile", „caută dublurile", „e ceva în neregulă în lista asta de cheltuieli", „validează tabelul de cheltuieli", „se potrivesc totalurile?" sau vrea un control de calitate înainte să trimită un decont/raport. Nu corectează singur datele — semnalează fiecare problemă cu rândul exact și lasă decizia la om.
---

# Verificator de cheltuieli (verificator-cheltuieli)

Trece o listă de cheltuieli prin patru filtre — duplicate, câmpuri lipsă, articole în afara politicii, totaluri care nu se adună — și scoate o listă de probleme, fiecare ancorată în rândul exact din fișier. Partea care nu e trivială: nu „repară" tăcut datele și nu inventează o politică — verifică doar contra regulilor pe care i le dai, iar restul marchează ca neclar. Nu îl folosi pentru rezumate/grafice (acolo e `profilare-date`) și nici pentru a explica variații plan-vs-realizat (acolo e `explicator-variatii`).

## Input
- O listă/tabel de cheltuieli (CSV sau tabel), cu antete clare (dată, furnizor, categorie, sumă etc.).
- Opțional: regulile de politică (plafoane pe categorie, câmpuri obligatorii, furnizori permiși). Dacă lipsesc, întreabă o dată sau verifică doar duplicate + câmpuri lipsă + adunarea.

## Metodă
1. **Câmpuri lipsă:** parcurge fiecare rând, marchează rândurile cu celule goale în câmpurile obligatorii.
2. **Duplicate:** găsește rânduri (aproape) identice (aceeași dată + furnizor + sumă) care par înregistrate de două ori.
3. **În afara politicii:** dacă ai reguli, marchează articolele care le încalcă (peste plafon, categorie nepermisă, furnizor neaprobat). Fără reguli, sari acest pas și spune că l-ai sărit.
4. **Totaluri:** recalculează suma din rânduri și compar-o cu orice total declarat în fișier; semnalează diferența exactă dacă nu se potrivesc.
5. Adună totul într-o listă de probleme, fiecare cu numărul de rând și valoarea concretă.

## Output (obligatoriu)
- **Tabel de probleme:** rând · tip problemă (duplicat / câmp lipsă / în afara politicii / total greșit) · detaliu concret · severitate.
- **Verificarea totalului:** suma calculată vs suma declarată, cu diferența dacă există.
- **Rezumat:** câte probleme, pe tipuri; ce blochează trimiterea decontului.
- Nicio corecție aplicată — doar semnalări pentru om.

## Disciplină (firul roșu)
Fiecare problemă trimite la un rând și o valoare reale din fișier — fără acuzații vagi. Nu inventezi o politică pe care nu ai primit-o; ce nu poți verifica rămâne „de verificat de un om". Nu modifici și nu ștergi rânduri — un decont se corectează de către persoana responsabilă, tu doar arăți unde să se uite.
