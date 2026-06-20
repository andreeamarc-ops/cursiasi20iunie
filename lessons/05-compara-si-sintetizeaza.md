# Cursul 5: Compară și sintetizează *(procurement)*

Context curat. Acum ești **Sorina**, pe operațiuni la Nordica. După lansarea v2.0 o să vină un val de tichete de
suport, așa că ai cerut oferte de la trei furnizori de help-desk. Ai trei oferte și un caiet de sarcini. Sarcina
clasică de achiziții: *care e cea bună?* — și capcana clasică: *cea mai ieftină nu e mereu răspunsul.*

ACTION: Arată-i ce e în `scenarii/oferte-furnizori/`: caietul de sarcini (`caiet-de-sarcini.md`) și cele trei
oferte (AjutorPro, DeskNord, TichetRapid). Nu le compara încă.

Întâi, citește **caietul de sarcini** — pentru că *el* e standardul față de care judecăm, nu prețul. Spune-mi: care
crezi că e prima întrebare pe care o pun despre fiecare ofertă?

WAIT: Care e prima întrebare? *(„pas" = îți spun eu)*

USER: [Ghicește — ideal: „respectă cerințele obligatorii?")]

---

Exact: **întâi cerințele obligatorii, abia apoi prețul.** Caietul de sarcini are cerințe marcate „obligatoriu" —
una dintre ele e **suport și interfață în limba română**. O ofertă care pică o cerință obligatorie e
**descalificată**, oricât de ieftină ar fi.

Hai să le pun cap la cap ca lumea. Cere-mi o comparație — sau spune „ocupă-te tu, Claude" și o fac cu skill-ul de
procurement.

WAIT: Cere-mi comparația. *(USER: „compară cele trei oferte față de caietul de sarcini")*

USER: [Cere comparația]

ACTION: Rulează `comparator-oferte` (din Procurement Kit). Scrie în `outputs/comparatie-oferte.md` un tabel
side-by-side: fiecare **cerință obligatorie** marcată pass/fail pentru fiecare ofertă, apoi nice-to-have-urile,
apoi prețul. **Descalifică** orice ofertă care pică un obligatoriu, chiar dacă e cea mai ieftină. Încheie cu o
recomandare *cu rezerve*, nu un verdict sec.

---

Și uite capcana cum iese la iveală: **TichetRapid** e cea mai ieftină (~90 €/lună) și arată tentant — dar e
**doar în engleză**. Pică cerința obligatorie de suport în română. Dacă te uitai doar la preț, o alegeai și-ți
cumpărai o problemă de suport pentru toți clienții Nordica.

Câștigătoarea probabilă e **DeskNord**: respectă tot ce e obligatoriu, e în buget (~140 €), îi lipsește doar un
nice-to-have (app mobil). Dar observă cum am formulat — „probabil", „cu rezerve". Recomand; **Sorina decide**.

WAIT: Vezi în tabel cum TichetRapid pică pe „limba română", deși are cel mai bun preț?

USER: [Se uită]

---

Ăsta e reflexul 4 din nou, dar pe sinteză: nu rezum oferte „în general", le judec **față de un standard explicit**
și marchez clar unde fiecare cade. Asta transformă trei PDF-uri într-o decizie.

---

Încă ceva util înainte să mergem mai departe: comparația e acum un `.md`, dar tu poate vrei s-o trimiți cuiva care
nu deschide așa ceva. Același conținut poate ieși în **mai multe formate** — un **document Word**, un **PDF** de
atașat la email, sau o **pagină HTML** pe care o deschizi în browser. Nu rescrii nimic; doar îl scot în forma de
care ai nevoie.

WAIT: Vrei să-ți transform `comparatie-oferte.md` într-un format anume — Word, PDF sau HTML? *(„pas" = mergem mai
departe așa)*

USER: [Alege un format sau spune „pas"]

ACTION: Dacă alege, exportă `outputs/comparatie-oferte.md` în formatul cerut (`outputs/comparatie-oferte.docx` /
`.pdf` / `.html`), păstrând tabelul comparativ și recomandarea. Conținutul rămâne identic — se schimbă doar
ambalajul. Spune-i să-l deschidă din panou.

TRAINER: (opțional) Madalina poate lega aici ideea „un rezultat, mai multe formate" de munca lor reală — când vrei
Word pentru un coleg, PDF pentru un client, HTML pentru ceva de pus pe ecran. Predă ștafeta scurt dacă e momentul.

---

**Ce ai învățat:** Cum sintetizezi mai multe surse față de un criteriu, nu „pe simțite". Obligatoriu înainte de
preț. Descalificarea unei oferte ieftine dar neconforme. Și că același rezultat îl poți scoate în **Word, PDF sau
HTML**, după cine îl primește.

**Ce ai produs:** `outputs/comparatie-oferte.md` — comparație cu pass/fail pe obligatorii și recomandare cu rezerve
(plus, dacă ai cerut, o variantă în Word / PDF / HTML).

**Decizia umană:** Furnizorul ales îl semnează Sorina. Eu am făcut comparația transparentă.

**Urmează:** Mergem la date — un CSV de cheltuieli — și corectăm exact cifra de 38.000 de la Cursul 4.

**Ca să continui:** sarcină nouă, spune **„cursul 6"**.
