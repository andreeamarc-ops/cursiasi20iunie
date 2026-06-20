# Cursul 9: Verifică-ți munca, cu subagenți *(curs-cheie)*

Context curat. Primul instrument nou: **subagenții**. Și cea mai bună folosire a lor e și cea mai sănătoasă
disciplină — **să-ți verifici critic propria muncă** înainte s-o trimiți mai departe. Azi o facem pe un text de
**marketing**: un anunț de lansare pe care vrem să-l publicăm.

Întâi diferența, că se confundă des:
- **Skill** = o *metodă reutilizabilă*, salvată. Aceeași rețetă, de fiecare dată. (Ce am făcut la Cursurile 7–8.)
- **Subagent** = un *asistent secundar cu context proaspăt*, pe care îl pornesc pentru o sarcină de moment. Nu
  știe ce-am vorbit noi — și tocmai de-aia e bun la verificat: vine cu **ochi noi**, nu e „îndrăgostit" de
  rezultatul pe care chiar eu l-am produs.

Ideea cheie: dacă eu îmi verific singur textul în aceeași conversație, am deja toate presupunerile mele în cap.
Trei subagenți, fiecare cu context curat și **altă perspectivă**, prind ce mie îmi scapă.

## Partea 1 — Scriem textul (pe regulile casei)

Ești în pielea cuiva de la **marketing/comunicare** la Nordica. Se apropie lansarea v2.0 și ai nevoie de un anunț.
Dar nu-l scriem „din burtă" — îl scriem pe **regulile casei**: vocea Nordica, ce promitem și ce nu.

ACTION: Arată-i `scenarii/marketing-lansare/brief-anunt-v2.md` (faptele despre lansare — ce e confirmat, ce e doar
„posibil", ce NU avem voie să afirmăm) și skill-ul `reguli-de-casa` (regulile noastre de comunicare, codificate).

WAIT: Vrei să citești tu întâi brieful, sau pornesc skill-ul direct? *(„pas" = pornesc eu)*

USER: [Alege]

ACTION: Rulează `reguli-de-casa` pe brief. Scrie un anunț de lansare în `outputs/anunt-lansare-v2.md`, pe structura
casei (titlu clar → o promisiune → 2–3 beneficii concrete → onestitate despre ce e „posibil" → un singur CTA).
Regula fermă: **nu promite ce nu e în brief** — SMS-urile rămân „posibil", nicio cifră/testimonial inventat, ce nu e
acoperit se marchează „[de confirmat]". La final, secțiunea „De confirmat înainte de publicare".

WAIT: Te uiți peste anunț? Observă cum sună pe vocea Nordica — și ce a marcat „[de confirmat]" în loc să inventeze.

USER: [Se uită]

## Partea 2 — Îl punem sub trei perspective

Acum partea puternică: înainte să-l publicăm, îl trecem prin **trei subagenți**, fiecare cu altă pereche de ochi.
Pentru un text public, perspectivele bune nu sunt „corectitudine/claritate", ci oamenii pe care textul îi
întâlnește în lume:

- **PR** — servește mesajul nostru? E pe vocea brandului? Convinge fără să sune a reclamă goală?
- **Jurnalist sceptic** — ce afirmație nedovedită ar ataca un ziarist critic? Unde e hype neacoperit de fapte?
- **Client potențial** — mi se adresează mie? Am încredere? Ce rămâne neclar, ce obiecție îmi stă în gât?

Și vreau **tu** să-mi dai comanda, ca să simți cum sună:

WAIT: Scrie-mi: **„generează 3 subagenți care să recenzeze `outputs/anunt-lansare-v2.md`, fiecare cu altă
perspectivă — PR, jurnalist sceptic, client potențial."** *(USER: îți dă exact acest tip de prompt)*

USER: [Îți dă promptul de subagenți]

ACTION: Rulează `review-cu-subagenti` pe anunț, cu cele **trei perspective cerute** (PR · jurnalist sceptic · client
potențial). Pornește trei subagenți cu context proaspăt. Adună constatările în `outputs/review-anunt-v2.md`: grupate
pe perspectivă, fiecare cu „ce e bun" și „ce trebuie schimbat/dovedit", plus o secțiune finală **„Ce trebuie decis
de om"**. Fii sincer — dacă jurnalistul sceptic prinde o promisiune neacoperită (ex. un beneficiu scris prea tare
sau SMS-ul promis ca sigur), spune-o direct.

WAIT: Te uiți peste review? Ce a prins jurnalistul sceptic — ceva ce ție ți-ar fi scăpat la prima citire?

USER: [Se uită]

---

Observă ce s-a întâmplat: am scris un text **și** l-am atacat din trei unghiuri, fără să-l trimit la trei colegi și
să aștept o zi. Dar atenție la linia roșie: subagenții **pregătesc** decizia — textul final, cuvânt cu cuvânt, și
butonul „publică" rămân la om. Nu publicăm „un text aprobat de AI".

Două reflexe se ating aici. **Reflexul 4** (verifici) — dar acum verificarea e structurată, din trei perspective,
nu „mai citește o dată". Și **reflexul 3** (când delegi și când nu): scrii și verifici cu Claude, dar mesajul către
lume îl asumi tu.

---

**Ce ai învățat:** Skill vs. subagent (metodă reutilizabilă vs. minte proaspătă). Cum scrii un text pe **regulile
casei** și apoi îl pui sub un panel de subagenți cu **perspective** diferite (PR, jurnalist sceptic, client) ca
să-l verifici critic înainte de publicare.

**Ce ai produs:** `outputs/anunt-lansare-v2.md` (anunțul) și `outputs/review-anunt-v2.md` — recenzia din trei
perspective, cu „ce decide omul".

**Decizia umană:** Subagenții pregătesc; tu scrii varianta finală și apeși „publică". Mereu.

**Urmează:** Conectăm Cowork la o unealtă reală — calendar / email, apoi un serviciu românesc (ANAF) — și înțelegem
ce e MCP.

**Ca să continui:** sarcină nouă, spune **„cursul 10"**.
