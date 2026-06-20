# Cursul 4: Organizarea unui folder dezordonat *(administrativ)*

Context curat. Acum ești **Mihaela**, office manager la Nordica. Ai moștenit un folder — pontaje, ciorne de raport,
notițe de telefon, un email forwardat de trei ori, un **Excel** și un **document Word** — cu nume de fișiere
imposibile (`Copy of Copy of raport ciorna.md`, `Document (3).md`, `Registru1.xlsx`, `Document final (1).docx`).
Clasica grămadă administrativă, cu tipuri amestecate. O facem ordine împreună și, pe drum, dăm peste **problema
numărul unu a AI-ului**.

Ca în Cursul 1, eu nu mă uit singur. **Cere-mi tu** să verific folderul și să-ți fac un cuprins.

WAIT: Cere-mi să mă uit în `scenarii/folder-haos-admin/` și să fac ordine. *(scrie cu cuvintele tale)*

USER: [Îți cere un cuprins / o organizare a folderului]

ACTION: Deschide fiecare fișier din `scenarii/folder-haos-admin/` — inclusiv Excel-ul (`Registru1.xlsx`) și
documentul Word (`Document final (1).docx`) —, **identifică-l după conținut, nu după nume**, și fă un cuprins în
`outputs/cuprins-folder-admin.md`: ce e fiecare fișier, ce acțiuni/termene reies din el, și — cel mai important —
**ce nu se potrivește**. Caută activ contradicții. (În Excel, de pildă, totalul scris de mână «2200» nu se
potrivește cu suma rândurilor — semnalează asta, nu lua totalul de bun.)

---

Aici e capcana, și e intenționată. În ciorna de raport (`Copy of Copy of raport ciorna.md`) cineva a scris, **din
memorie**, cât s-a cheltuit pe marketing — „cam pe la 38.000 lei, parcă". Nu e luat din niciun fișier. E o cifră
care *sună* plauzibil.

Asta e exact problema numărul unu: **AI-ul (și omul) produc lucruri care sună bine dar nu sunt verificate.** Dacă
aș fi luat ciorna de bună și aș fi raportat 38.000 lei mai departe, ar fi intrat o cifră greșită în raportul către
Andreea.

**Așa că nu o iau de bună.** O marchez în cuprins ca **neconfirmată**: „raportul spune ~38.000 lei marketing, dar
e «din memorie», fără sursă — de verificat în datele reale." Fă exact asta în fișier.

WAIT: Vezi în cuprins cum am semnalat cifra de 38.000 ca neconfirmată, separat de ce e documentat?

USER: [Se uită]

---

Ăsta e **reflexul 4**, cel mai prețios din toată ziua: **când ai încredere și când verifici.** Regula de aur — o
cifră, o sursă, un nume, o dată nu intră într-un rezultat decât dacă o găsești în fișier. Ce nu e în sursă e „de
verificat", nu un fapt.

Și uite ce frumos se leagă: cifra reală de marketing **chiar există** — e în CSV-ul de cheltuieli. La Cursul 6 o
calculăm din date și corectăm exact acest 38.000. Atunci o să vezi cât de departe era „din memorie".

---

Acum partea satisfăcătoare: **punem ordine și în nume.** Un cuprins e bun, dar tot dai de `Document (3).md` și
`Registru1.xlsx`. Hai să le dau fiecărui fișier un nume care spune ce e.

ACTION: Pe baza conținutului identificat, **redenumește fiecare fișier** din folder cu un nume descriptiv, consistent
(de ex. `Copy of Copy of raport ciorna.md` → `raport-status-financiar-CIORNA.md`, `Registru1.xlsx` →
`cheltuieli-marunte-birou.xlsx`, `Document final (1).docx` → `nota-interna-pregatire-lansare.docx`, `Document (3).md`
și restul la fel). Fă redenumirile **în folder**, ca participantul să le vadă schimbându-se în panou, și notează în
cuprins maparea „nume vechi → nume nou". Păstrează conținutul neatins — schimbi doar numele.

WAIT: Vezi în panou cum fiecare fișier are acum un nume care-ți spune ce e, fără să-l deschizi?

USER: [Se uită]

---

Și fiindcă acum fișierele au nume clare, e momentul perfect pentru un mic truc care-ți schimbă viața când lucrezi
în folder: poți să-mi spui exact pe **care** fișier să mă uit, scriind `@` în fața numelui — `@cheltuieli-marunte-birou`
— și știu fix la ce te referi, fără să caut prin tot folderul.

TRAINER: Madalina preia și arată sălii, pe viu, **mențiunea cu `@`** — cum scrii `@` în Cowork, cum apare lista de
fișiere și cum alegi exact fișierul pe care vrei să lucrez. (Revenim la `@` la Cursul 6, când îți cer chiar tu să-l
folosești.) Predă-i ștafeta și oprește-te.

WAIT: Gata, după ce v-a arătat Madalina cum se menționează un fișier cu `@`?

USER: Da

TRAINER: (opțional) Madalina poate întreba sala: de câte ori ați trimis mai departe un raport cu o cifră „de pe
la cineva"? Predă ștafeta scurt dacă vrea, altfel mergi mai departe.

---

**Ce ai învățat:** Reflexul 4 — verifici în sursă, mereu. Din haos am scos un cuprins cu acțiuni, dar am separat
clar ce e documentat de ce e „din memorie". Și ai mai prins două lucruri practice: Claude citește și Excel/Word, nu
doar `.md`, iar cu **`@nume-fișier`** îl ții exact pe fișierul pe care vrei.

**Ce ai produs:** `outputs/cuprins-folder-admin.md` — folderul indexat, cu contradicția marcată — plus **fișierele
redenumite** descriptiv, direct în folder.

**Decizia umană:** Ce intră în raportul final și ce cifre se confirmă rămâne la Mihaela. Eu doar am semnalat ce nu
se sprijină pe nimic.

**Urmează:** Punem trei oferte de furnizor cap la cap și descoperim că cea mai ieftină nu e cea care câștigă.

**Ca să continui:** sarcină nouă, spune **„cursul 5"**.
