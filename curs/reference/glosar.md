# Glosar — termenii din atelier, pe înțelesul tuturor

Read-only. Dacă un participant întreabă „ce înseamnă X", explică-i scurt, cu un exemplu de birou.

- **Cowork** — spațiul de lucru din aplicația Claude. Claude lucrează direct în folderul tău, pe fișierele tale,
  cu un panou de fișiere lateral. Nu e un terminal, nu scrii cod. Tehnic e același motor pe care îl folosesc și
  developerii (Claude Code), dar aici îl folosim pentru documente, tabele și procese.
- **Agent** — un AI care nu doar răspunde, ci *face*: citește fișiere, scrie altele, rulează pași, verifică. Spre
  deosebire de un chat unde tu cari informația înăuntru, agentul vine la fișierele tale.
- **Folder de proiect** — folderul pe care îl deschizi în Cowork. Tot ce e în el, Claude poate vedea și folosi.
- **Panoul de fișiere** — lista laterală cu fișierele din folder. Tot ce atinge Claude apare acolo, în timp real.
- **Context (fereastra de context)** — „memoria de lucru" a lui Claude într-o conversație. E limitată: cu cât o
  conversație e mai lungă, cu atât e mai aglomerată, mai lentă și mai scumpă. De aceea: **un curs = o sarcină
  nouă.**
- **Token** — bucățică de text (≈ ¾ dintr-un cuvânt). Contextul și costul se măsoară în tokeni. O sarcină
  proaspătă = mai puțini tokeni cărați degeaba.
- **`.md` (Markdown)** — fișier text simplu, lizibil și de om și de AI. Lucrăm mult cu el pentru că e curat și
  ușor de versionat. `.csv` = tabel. `.pdf` = document fix.
- **`@fișier` (mențiune de fișier)** — scriind `@nume-fișier` îi spui lui Claude exact pe ce fișier să se uite,
  fără să-i copiezi conținutul.
- **CLAUDE.md** — un fișier de instrucțiuni de folder. Se încarcă singur când deschizi folderul și-i spune lui
  Claude cum să lucreze acolo (ton, reguli, unde sunt lucrurile). Îl scrii o dată, te servește mereu. (Cursul 3.)
- **Skill** — o metodă reutilizabilă, salvată, pe care o pornești cu o comandă (`/nume-skill`). „Construiești o
  dată, folosești la nesfârșit." Cele 7 Starting Kit-uri sunt skill-uri gata făcute. (Cursurile 7–8.)
- **Subagent** — un asistent secundar pe care Claude îl pornește pentru o sarcină, **cu context proaspăt**. Util
  ca să-ți recenzeze critic propriul rezultat (mai mulți subagenți, fiecare cu altă lentilă). Diferența de skill:
  skill = metodă reutilizabilă; subagent = minte nouă, de moment. (Cursul 9.)
- **MCP / API** — felul în care Claude se conectează la alte unelte și servicii (Gmail, Calendar, Sheets, Slack,
  Zoom, ANAF). MCP e „priza standard" prin care un serviciu se leagă de Claude. (Cursul 10.)
- **ANAF / demoanaf.ro** — ANAF e autoritatea fiscală din România. `demoanaf.ro` e un serviciu public, gratuit,
  peste datele oficiale, care are și un **server MCP** (`https://demoanaf.ro/mcp`). Îl conectezi în Cowork și poți
  verifica o firmă după **CUI**: denumire oficială, stare (activ/inactiv/radiat), dacă e **plătitoare de TVA**,
  adresă. Sursă reală = scade riscul de „date din cap". (Cursul 10.)
- **CUI** — Codul Unic de Identificare al unei firme din România (codul fiscal). După el verifici firma la ANAF.
- **DPA** — acord de prelucrare a datelor; clauza care spune cum și unde un furnizor prelucrează datele tale
  personale. Lipsa lui dintr-un contract e un risc GDPR. (Cursul 9, Legal Kit.)
- **GDPR** — regulamentul european de protecție a datelor personale. „Verificare GDPR" = vezi ce date se colectează,
  pe ce temei, cât se păstrează și ce lipsește. (Legal Kit.)
- **Rutină** — o sarcină care rulează singură, programat (ex. un digest în fiecare dimineață). Linia roșie:
  automatizezi *adunarea* și *schițarea*, nu *trimiterea*. (Cursul 11.)
- **Starting Kit** — un pachet de skill-uri pe un domeniu (PM, content, HR, financiar, procurement, antreprenor).
  Fiecare participant pleacă cu kitul lui. (`STARTING-KITS.md`.)
- **Firul roșu** — disciplina care nu se negociază: AI = instrument, nu sursă de adevăr; nu inventăm cifre/surse;
  omul deține fiecare decizie.
