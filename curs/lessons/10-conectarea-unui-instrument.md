# Cursul 10: Conectarea unui instrument *(comun)*

Context curat. Până acum Cowork a lucrat pe fișierele din folder. Dar munca ta nu trăiește doar în fișiere — trăiește
și în **alte locuri**: în **calendar**, în **Zoom**, în **Gmail**, în servicii online. Cursul ăsta e despre cum le
**conectezi**, ca Claude să poată întreba o sursă reală, nu să presupună.

Începem cu ce ai tu cel mai la îndemână — **calendarul și emailul** — pentru că-s cele mai ușor de conectat. Abia
apoi mergem la un serviciu de business (ANAF).

WAIT: Înainte de partea practică — cât timp pierzi într-o zi sărind între calendar, inbox și fișiere ca să aduni ce-ți
trebuie? *(„pas")*

USER: [Spune ceva]

---

## Partea 1 — Întâi uneltele tale: Calendar / Gmail

Cel mai natural prim pas e să-i dai lui Claude acces la **calendarul** tău (sau Gmail). Atunci poate să-ți spună ce
ai azi, sau să-ți adauge o programare — fără să copiezi nimic.

TRAINER: Madalina conduce live conectarea **calendarului** (Google Calendar / Gmail) în Cowork — de unde se adaugă
conexiunea — și, foarte important, arată sălii **cum arată permisiunile în Claude Cowork**: ce-i dai voie să vadă, ce
poate și ce nu poate face, cum revoci accesul. Predă-i ștafeta și oprește-te până confirmă sala.

WAIT: E conectat calendarul? Ați văzut împreună cu Madalina ce permisiuni i-ați dat?

USER: Da / [a mers / n-a mers]

---

Acum că e conectat, hai să-l folosești în două feluri — **întâi să primești informație, apoi să adaugi.**

**a) Primești informație (citire — comod și sigur):**

WAIT: Cere-mi tu o citire din calendar — de exemplu „ce am azi în calendar?" sau „rezumă-mi întâlnirile de
săptămâna asta". *(USER: îți cere o citire din calendar)*

USER: [Cere o citire]

ACTION: Dacă e conectat, citește calendarul și răspunde scurt și util (ce are azi, în ordine, cu orele). Dacă nu e
conectat în mediul de azi, **nu te preface** — arată cum ar arăta cererea și ce-ar întoarce, sincer.

**b) Adaugi ceva (scriere — cu confirmarea ta):**

WAIT: Acum cere-mi să-ți **adaug** ceva în calendar — de exemplu „pune-mi o întâlnire mâine la 10 cu echipa". *(USER:
îți cere să adaugi un eveniment)*

USER: [Cere o adăugare]

ACTION: Pregătește evenimentul (titlu, dată, oră, durată) și **arată-i exact ce vei adăuga înainte să confirmi** —
abia după „da" îl creezi. Aici e nuanța liniei roșii: o adăugare pe care **tu o ceri și o confirmi** e în regulă;
ce nu vrem e o automatizare care trimite/modifică **singură**, fără om. (Despre asta e tot Cursul 11.)

WAIT: Vezi cum am pregătit evenimentul și am așteptat confirmarea ta înainte să-l pun în calendar?

USER: [Se uită]

---

## Partea 2 — Ce altceva poți conecta (și cum știi că se poate)

Calendarul a fost doar începutul. La fel se conectează **Gmail, Sheets, Slack, Zoom** și o grămadă de servicii. Dar
cum știi *ce* se poate conecta și *cum*? Aici intervin două cuvinte pe care merită să le demitizăm.

TRAINER: Madalina preia și explică sălii, pe înțelesul tuturor, **ce sunt API-urile și MCP-urile** — „prizele
standard" prin care un serviciu se leagă de Claude (MCP e priza prin care un serviciu vorbește cu Claude; API e
termenul mai larg pentru „o aplicație vorbește cu alta"). Ideea de transmis: nu le construiești tu, doar le
conectezi — și de obicei, dacă un serviciu are o astfel de „priză", îl poți lega. Predă-i ștafeta și oprește-te.

WAIT: Gata, după ce a explicat Madalina API & MCP?

USER: Da

---

## Partea 3 — Conectăm ANAF (un serviciu românesc real)

Acum trecem de la uneltele personale la un serviciu de business — și e ceva foarte util pentru oricine facturează în
România. Ești **Diana**, pe legal/compliance la Nordica. Înainte să facturăm clienți noi, vrem să fim siguri că
firmele lor există, sunt active și știm dacă-s plătitoare de TVA. Asta se verifică la **ANAF** — și există un server
MCP public, **`https://demoanaf.ro/mcp`** (o alternativă gratuită peste datele oficiale), pe care îl conectăm în Cowork.

Uite cum se adaugă conectorul (e mai simplu decât pare — nu editezi fișiere):
1. Intră la **`claude.ai/customize/connectors`**.
2. Apasă **„+" → „Add custom connector"**.
3. Lipește URL-ul: **`https://demoanaf.ro/mcp`**.
4. Apasă **„Add"**.
5. Ca să-l folosești într-o conversație: apasă **„+"** (stânga-jos în chat) → **„Connectors"** → pornește
   **DemoANAF**.

TRAINER: Madalina conduce conectarea live a lui DemoANAF cu sala, după pașii de mai sus, și se asigură că **toți cei
care vor să-l folosească sunt efectiv conectați** (uneori cere câțiva pași). Predă-i ștafeta și oprește-te.

WAIT: E conectat ANAF (DemoANAF)? Îl vezi în listă, pornit?

USER: Da / [a mers / n-a mers]

---

Acum că e conectat, e firesc să întrebi *ce poate*. Înainte să-l punem la treabă, întreabă-l ce știe să facă.

WAIT: Cere-mi să-ți spun **ce instrumente are DemoANAF** — și alege apoi o firmă anume pe care s-o verificăm.
*(USER: „ce instrumente are demo-anaf?" + alege o firmă)*

USER: [Întreabă ce unelte are + alege o firmă]

ACTION: Întreabă conectorul ce instrumente expune și enumeră-le pe scurt. Apoi, pe firma aleasă de participant,
fă o interogare simplă (denumire oficială, stare, plătitor de TVA) ca demonstrație. Dacă nu e conectat, arată sincer
cum ar arăta.

---

Acum, exact înainte să ne bazăm pe el, e momentul potrivit pentru *de ce* contează enorm asta. Îți predau ștafeta,
Madalina.

TRAINER: Madalina explică sălii **halucinațiile** și de ce conectarea e leacul. Ideea de transmis: un AI
„halucinează" mai ales când **nu are informația corectă** — nu „minte", ci umple golul cu ceva ce *sună* plauzibil
(exact cazul cu cei 38.000 lei „din memorie" de la Cursul 4). Soluția nu e „să se străduiască mai mult", ci **să-i
dai informația corectă** — iar cea mai bună cale e să-l **conectezi direct la sursă** (fix MCP-ul ANAF de acum). Când
Claude poate *întreba sursa*, nu mai e nevoit să ghicească. Predă-i ștafeta și oprește-te.

WAIT: Gata, după ce a explicat Madalina legătura halucinații → surse conectate?

USER: Da

---

## Partea 4 — Verificăm clienții, automat

Avem o listă de clienți în `scenarii/clienti-anaf/clienti.csv` — nume, CUI și un „status presupus" (ce a scris
clientul în formular). Important: **fișierul poate minți.** Numele pot fi greșite, „activ" poate fi de fapt radiat,
„plătitor TVA" poate fi greșit. **ANAF e sursa de adevăr, nu coloana din CSV.** Ăsta e reflexul 4 cu un serviciu
real: nu presupui — întrebi sursa.

WAIT: Cere-mi tu verificarea — de exemplu „verifică fiecare firmă din `@clienti.csv` la ANAF și spune-mi care nu se
potrivește". *(USER: îți cere verificarea listei)*

USER: [Cere verificarea]

ACTION: Rulează `verificare-firma-anaf` (Legal Kit) pe `scenarii/clienti-anaf/clienti.csv`. Pentru fiecare CUI,
**întreabă live ANAF prin MCP**: denumire oficială, stare (activ/inactiv/radiat), plătitor de TVA, adresă dacă e
disponibil. Scrie un tabel în `outputs/verificare-clienti-anaf.md` și **marchează nepotrivirile** față de fișier
(nume diferit, „activ" presupus dar radiat, statut TVA diferit). CUI-ul invalid (`99999999`) o să iasă „negăsit" —
marchează-l așa, nu inventa o stare. La final, o listă „**De rezolvat înainte de facturare**".

Dacă din vreun motiv conexiunea ANAF nu merge în mediul de azi, **nu te preface** că ai verificat — arată-i cum ar
arăta comanda și ce-ar întoarce, sincer, și spune că datele reale vin doar cu MCP-ul conectat.

WAIT: Te uiți peste tabel? Vezi unde fișierul spunea una și ANAF spune alta — și firma „negăsită"?

USER: [Se uită]

---

Asta e diferența uriașă dintre „AI care inventează" și „AI care întreabă o sursă". Când conectezi un serviciu real,
scade exact riscul de la Cursul 4: în loc de o stare „din cap", ai răspunsul oficial, pe care îl poți arăta oricui.
Și am verificat toate firmele în câteva secunde — manual ar fi fost câte o căutare pe site pentru fiecare.

## Partea 5 — Ce conectezi tu, în munca ta

ANAF a fost un exemplu de business; calendarul, de la început, unul personal. Întrebarea utilă pentru tine e: *ce
folosești tu zi de zi și s-ar putea conecta?*

TRAINER: Madalina întreabă sala **ce servicii/instrumente folosesc fiecare în munca lor** (un CRM, un program de
facturare, Trello, Notion, Slack…) și îi pune să se intereseze dacă **se pot conecta la Claude** — așa pleacă fiecare
cu o idee concretă, nu generală. Predă-i ștafeta și oprește-te.

WAIT: Gata, după ce ați discutat ce ați conecta fiecare?

USER: Da

TRAINER: La final, Madalina arată **Composio** — un fel de „magazin de prize" care simplifică conectarea multor
unelte deodată (Gmail, Calendar, Slack, Sheets…). Predă ștafeta scurt.

WAIT: Gata, după Composio?

USER: Da

---

Linia roșie, și aici: o conexiune îi dă lui Claude **acces**. Citirea și verificarea (ca la ANAF, sau „ce am în
calendar") sunt comode și sigure. La **acțiuni** care ies în lume — trimite un email, emite o factură, șterge un
eveniment — **omul confirmă** (ca la adăugarea în calendar de adineauri). Conectăm ca să *aflăm* și *să schițăm*;
butonul „trimite" rămâne al tău. (Exact tema de la Cursul 11.)

---

**Ce ai învățat:** Datele tale trăiesc în mai multe locuri; le poți **conecta**. Ai legat întâi o unealtă personală
(Calendar/Gmail) — citire și o adăugare cu confirmarea ta —, ai înțeles **MCP/API** (prize standard), apoi ai
conectat un serviciu românesc real (**ANAF**) și ai **verificat automat o listă de clienți** cu sursa oficială.

**Ce ai produs:** `outputs/verificare-clienti-anaf.md` — clienții verificați la ANAF, cu nepotrivirile semnalate.

**Decizia umană:** Ce faci cu un client radiat sau un CUI invalid (suni, corectezi, nu facturezi) decizi tu. Claude
a adus adevărul; tu acționezi pe el.

**Urmează:** Rutine — cum pui o sarcină să ruleze singură în fiecare dimineață, fără să dai puterea de „trimite".

**Ca să continui:** sarcină nouă, spune **„cursul 11"**.
