# Cursul 6: Analiză de date & grafic *(administrativ)*

Context curat. Înapoi la Mihaela și la cifra aceea suspectă. Îți amintești „~38.000 lei marketing, din memorie" din
ciorna de la Cursul 4? Azi aflăm cât e de fapt — calculat din datele reale — și scoatem și un grafic.

Mai întâi, un mic test de memorie. La Cursul 4 ai învățat un truc prin care îmi spui exact **pe care** fișier să
lucrez, ca să nu caut prin tot folderul.

WAIT: Mai ții minte cum îmi „țintești" exact fișierul pe care vrei să-l ating — semnul pe care îl scrii în fața
numelui? *(„pas" = ți-l amintesc eu)*

USER: [Ideal: „cu `@`" — `@cheltuieli-2026`]

---

Exact — `@`. Scriu `@cheltuieli-2026` și știu fix despre ce fișier vorbim. Hai să-l folosești tu acum.

WAIT: Scrie-mi o sarcină care folosește `@cheltuieli-2026.csv` — de exemplu „profilează `@cheltuieli-2026.csv` și
spune-mi cât s-a cheltuit pe fiecare categorie". *(„pas" = o scriu eu și ți-o arăt)*

USER: [Scrie sarcina cu @mențiune]

ACTION: Rulează `profilare-date` (Finance & Admin Kit) pe `scenarii/date/cheltuieli-2026.csv` — skill-ul ăsta vine
cu o **bucată de cod** (`scripts/profil_cheltuieli.py`) pe care chiar o rulezi, nu doar instrucțiuni. Claude **chiar
rulează cod** pe fișier (nu ghicește): rezumat pe coloane, **total pe fiecare categorie**, anomalii. Scrie sinteza
în `outputs/profil-cheltuieli.md` **și** generează un **grafic HTML interactiv** în `outputs/grafic-cheltuieli.html`
— nu doar bare pe categorii, ci și un **tabel cu toate rândurile, pe care îl poți filtra (căsuța de căutare) și
sorta (clic pe antet)**. Spune-i să deschidă HTML-ul din panou și să se joace puțin cu filtrarea/sortarea.

---

Acum momentul: cât e **de fapt** marketingul? Adună rândurile de Marketing din CSV. Iese **52.340 lei**.

Ciorna spunea ~38.000 „din memorie". Realitatea, calculată din date, e **52.340**. O diferență de peste 14.000
de lei — adică un raport trimis pe baza memoriei ar fi fost greșit cu 38%.

ACTION: Corectează. Scrie clar în `outputs/profil-cheltuieli.md`: „Marketing real (din `cheltuieli-2026.csv`):
**52.340 lei**. Ciorna de raport estima ~38.000 lei «din memorie» — incorect, de înlocuit." Asta închide capcana
deschisă la Cursul 4.

WAIT: Vezi diferența — 38.000 «din cap» vs. 52.340 din date? Și graficul în panou?

USER: [Se uită]

---

Asta e puterea reflexului 4 dusă până la capăt: nu doar *bănuiesc* că o cifră e greșită — **o înlocuiesc cu una
calculată din sursă, pe care o poți reproduce.** Cifra mea nu vine „de undeva"; vine din rândurile pe care le poți
număra și tu.

TRAINER: Madalina arată sălii alternativele pentru cine trăiește în foi de calcul: **Claude direct în Excel** și
**Gemini în Google Sheets** — când are sens să tragi datele în Cowork și când le lași unde sunt. Predă ștafeta și
oprește-te.

WAIT: Gata, după ce a arătat Madalina Excel/Sheets?

USER: Da

---

**Ce ai învățat:** ai folosit din nou `@fișier` ca să țintești exact (truc de la Cursul 4). Claude rulează cod pe
date reale (nu estimează) și scoate și un **grafic interactiv** — pe care îl filtrezi și-l sortezi. Și ai văzut,
negru pe alb, de ce „din memorie" e periculos. Plus: skill-ul ăsta nu e doar text, are și o bucată de cod care chiar
rulează — ține minte asta pentru Cursul 7.

**Ce ai produs:** `outputs/profil-cheltuieli.md` (cu corecția 38.000 → 52.340) și `outputs/grafic-cheltuieli.html`.

**Decizia umană:** Ce intră în raportul lunar și cum se prezintă rămâne la Mihaela — dar acum pe cifre verificabile.

**Urmează:** Trecem la skill-uri „adevărate" — găsești și instalezi unul de pe internet, singur.

**Ca să continui:** sarcină nouă, spune **„cursul 7"**.
