# Cursul 8: Creează-ți propriul skill *(HR)*

Context curat. Acum ești **Raluca**, HR la Nordica. După lansare angajezi un **Customer Success Specialist**. Ai
un brain-dump dezordonat despre rol și ai nevoie de o fișă de post curată. O să faci două lucruri: întâi folosești
un skill gata făcut, apoi îl **modifici pe nevoia ta** — și ăsta e momentul în care înțelegi cum se scrie un skill.

ACTION: Arată-i `scenarii/hr-rol/descriere-rol-brut.md` — notițele dezordonate ale Ralucăi (responsabilități,
nice-to-have, gânduri despre salariu, context de echipă, toate amestecate). Și skill-ul `generator-fisa-post` (HR
Kit), care folosește șablonul `templates/fisa-postului.md`.

WAIT: Vrei să citești tu întâi brain-dump-ul, sau pornesc skill-ul direct? *(„pas" = pornesc eu)*

USER: [Alege]

ACTION: Rulează `generator-fisa-post` pe `descriere-rol-brut.md`. Scoate o fișă de post structurată în
`outputs/fisa-post-customer-success.md`, după șablon: scop, responsabilități, profil, nice-to-have, ce oferim.
Regula fermă: **nu inventa** ce brain-dump-ul nu spune — mai ales salariul. Ce lipsește merge la secțiunea „De
completat", nu se ghicește.

WAIT: Te uiți peste fișă? Observă secțiunea „De completat" — vezi ce a refuzat să inventeze (ex. salariul)?

USER: [Se uită]

---

Asta e disciplina reflexului 4 codificată *în* skill: skill-ul însuși e construit să nu inventeze. Acum partea cea
mai puternică din toată ziua — **modifici skill-ul.**

Să zicem că la Nordica vrei ca fiecare fișă de post să aibă mereu și o secțiune nouă: **„Cum arată succesul în
primele 90 de zile"**. Nu vrei s-o ceri de fiecare dată — vrei ca skill-ul s-o producă mereu. Deci o adăugăm în
skill.

WAIT: Spune-mi tu ce vrei adăugat/schimbat în skill (poți lua sugestia cu 90 de zile sau alege altceva — o regulă
de ton, o secțiune nouă, un câmp în plus). *(USER: cere o modificare a skill-ului)*

USER: [Cere o modificare]

ACTION: Deschide `skills/generator-fisa-post/SKILL.md` și **modifică-l** după cererea lui (ex. adaugă în „Metodă" și
în „Output" secțiunea „Succes la 90 de zile"). Arată-i diff-ul conceptual: „uite, am schimbat fișierul ăsta — data
viitoare când rulezi skill-ul, o să facă și asta." Apoi, dacă vrea, rulează-l din nou pe brain-dump și arată-i că
fișa nouă conține secțiunea adăugată.

WAIT: Vezi cum o singură modificare în fișierul skill-ului schimbă tot ce produce de-acum încolo?

USER: [Se uită]

---

Asta e tot „secretul": un skill e un fișier text cu o metodă. Îl deschizi, îl schimbi, e al tău. Nu trebuie să
fii programator — trebuie doar să știi cum vrei să arate munca ta. **Ai construit ceva o dată; te servește mereu.**
Ăsta e vârful reflexului 5. Și ăsta e skill-ul propriu cu care pleci acasă (promisiunea din pagina cursului).

TRAINER: Aici Madalina preia și explică sălii **mentalitatea de a lucra cu Claude (sau orice agent): agentul învață
împreună cu tine.** Învață mai ales în două feluri — `CLAUDE.md`-ul evoluează, iar skill-urile evoluează pe măsură
ce le modifici. De fiecare dată când observi un comportament pe care nu-l vrei (sau vrei ceva anume), decizi *unde*
schimbi: în **`CLAUDE.md`** (afectează toate conversațiile din folder) sau în **skill** (afectează doar un anumit
tip de muncă). Și încă o idee: Claude e foarte bun la *scris* skill-uri — poți face un lucru cu el o dată,
demonstrativ, apoi îi ceri să transforme acel lucru într-un skill. Predă-i ștafeta și oprește-te.

WAIT: Gata, după ce a explicat Madalina cum „crește" Claude odată cu tine (CLAUDE.md vs. skill)?

USER: Da

---

**Ce ai învățat:** Cum pornești de la un skill gata făcut, scoți un rezultat real, și — cheia — cum **modifici**
skill-ul ca să lucreze în felul tău. Un skill e doar un fișier text editabil.

**Ce ai produs:** `outputs/fisa-post-customer-success.md` + un `generator-fisa-post` modificat de tine. **Acesta e
skill-ul tău propriu** de luat acasă.

**Decizia umană:** Ce pune Raluca în anunțul final (mai ales salariul, lăsat „de completat") rămâne la ea.

**Urmează:** Învățăm să ne verificăm propria muncă — cu mai mulți subagenți, fiecare cu altă lentilă.

**Ca să continui:** sarcină nouă, spune **„cursul 9"**.
