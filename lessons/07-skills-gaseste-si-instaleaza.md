# Cursul 7: Skill-uri — găsește și instalează *(comun, condus de trainer)*

Context curat. Ai folosit deja câteva **skill-uri** azi fără să le numim așa: ai scos acțiunile din ședință la
Cursul 2 (fără skill, manual), apoi `comparator-oferte` la 5 și `profilare-date` la 6. Acum le numim, înțelegem din
ce-s făcute și înveți să-ți aduci unul nou.

Pe scurt: un **skill** e o **metodă reutilizabilă, salvată**, pe care o pornești cu o comandă (`/nume-skill`). În
loc să explici de fiecare dată cum vrei o comparație de oferte, o codifici o dată într-un skill și apoi spui doar
`/comparator-oferte`. **Construiești o dată, folosești la nesfârșit.** Cele 7 Starting Kit-uri din `skills/` sunt
exact asta — pachete de skill-uri gata făcute, pe domenii (vezi `STARTING-KITS.md`).

## Un skill nu e mereu la fel: doar-prompt vs. prompt + cod

Hai să te uiți pe dinăuntru la **două** skill-uri, ca să vezi că nu-s toate la fel.

ACTION: Deschide-i întâi `skills/extragere-actiuni-sedinta/SKILL.md` — un skill **doar din prompt**: e un singur
fișier text cu o metodă scrisă clar (citește, marchează acțiunile, ancorează-le, nu inventa). Fără cod, fără magie.

ACTION: Apoi deschide-i `skills/profilare-date/` întreg — vezi că, pe lângă `SKILL.md`, are și un folder
`scripts/` cu un fișier de **cod** (`profil_cheltuieli.py`). Ăsta e un skill **prompt + cod**: instrucțiunile spun
*cum* să profilezi datele, iar codul *chiar rulează* calculul și scoate graficul interactiv (l-ai văzut la Cursul 6).

WAIT: Vezi diferența? Unul e doar o rețetă în text; celălalt are și o bucată de cod care se execută. *(„pas")*

USER: [Se uită]

---

Asta e ideea de reținut: un skill poate fi **doar instrucțiuni** sau **instrucțiuni + cod care trebuie rulat**. De
aceea, când iei un skill de la cineva, te uiți ce conține *înainte* să-l rulezi.

TRAINER: Acum că au văzut un skill pe dinăuntru, Madalina preia și explică sălii **diferența dintre `CLAUDE.md` și
skill-uri — și când se încarcă fiecare**: `CLAUDE.md` se încarcă **singur, mereu**, la începutul oricărei sarcini
din folder (reguli generale, de fundal); un **skill** se încarcă **doar când îl chemi** cu `/nume-skill` (o metodă
punctuală, pentru un anumit tip de muncă). Predă-i ștafeta și oprește-te — e explicația ei.

WAIT: Gata, după ce a explicat Madalina când se încarcă un `CLAUDE.md` și când un skill?

USER: Da

## Găsești și instalezi un skill nou

Acum partea practică: **îți aduci un skill nou de pe internet.** Există colecții publice de skill-uri pe care le poți
descărca, de exemplu:

- https://aitmpl.com/skills/
- https://skillsmp.com/
- https://github.com/alirezarezvani/claude-skills

Important — și aici Madalina a avut dreptate să întrebe: în Cowork **nu e de ajuns să pui skill-ul în folderul
`skills/`**. Un skill „adevărat", care apare în lista de `/`, se **instalează din setări**, cam așa:

1. În claude.ai / Cowork, intri la **Settings → Capabilities** și te asiguri că **„Code execution and file
   creation"** e pornit (fără el, skill-urile cu cod nu rulează).
2. Skill-ul se împachetează ca un **`.zip`** care conține folderul skill-ului (cu `SKILL.md` înăuntru).
3. Mergi la **Customize → Skills**, apeși **„+" → „Upload a skill"** și încarci `.zip`-ul.
4. După încărcare, Claude citește singur `SKILL.md` și-ți arată numele + descrierea. Îl pornești apoi cu
   `/nume-skill`. (Skill-urile încărcate sunt **private contului tău**.)

TRAINER: Madalina conduce ea acest pas live cu sala — alege o colecție, arată cum descarci/împachetezi un skill, cum
îl încarci din **Customize → Skills**, și cum confirmi că a apărut în lista de `/`. Predă ștafeta și oprește-te; nu
instala tu nimic în locul ei.

WAIT: Ați găsit și instalat un skill împreună cu Madalina? L-ați văzut apărând în lista de `/`?

USER: Da / [întrebare]

---

Un sfat de coleg, pe linia firului roșu: un skill e cod/instrucțiuni pe care le rulezi cu drepturile tale. **Uită-te
ce face înainte să-l pornești** — exact ca atunci când instalezi orice aplicație. Dacă nu înțelegi ce face, nu-l
rula pe date adevărate.

---

**Ce ai învățat:** Ce e un skill (metodă reutilizabilă, `/comandă`), că poate fi **doar-prompt sau prompt+cod**,
diferența față de `CLAUDE.md` (unul se încarcă mereu, celălalt doar la cerere), și cum **găsești + instalezi** unul
nou — împachetat ca `.zip`, încărcat din **Customize → Skills**, nu doar pus în folder. Plus reflexul de siguranță:
citește înainte să rulezi.

**Ce ai produs:** Un skill nou instalat în contul tău (cu Madalina).

**Decizia umană:** Tu alegi în ce ai încredere și ce rulezi pe date reale.

**Urmează:** Pasul în care îți **scrii propriul** skill, pornind de la unul existent.

**Ca să continui:** sarcină nouă, spune **„cursul 8"**.
