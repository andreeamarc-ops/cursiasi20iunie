# Starting Kits — harta celor 7 kituri pe domenii

Cele șapte **Starting Kit-uri** sunt seturi de skill-uri gata făcute, unul pentru fiecare tip de rol din sală.
Șase sunt kiturile de pe pagina de înscriere — **PM / Team Lead Kit**, **Content & Community Kit**, **HR Kit**,
**Finance & Admin Kit**, **Procurement Kit**, **Antreprenor Kit** — plus un **Legal Kit** adăugat pentru partea
juridică (contracte, GDPR, verificarea firmelor la ANAF).

Toate scenariile se petrec în aceeași firmă fictivă — **Nordica**, firma din Iași care lansează *Nordica Booking
v2.0* (vezi `reference/firma-nordica.md`). Kiturile sunt rolurile din Nordica, ca toate domeniile să se simtă ca un
singur loc de muncă, nu ca demo-uri separate. (Personajele firmei Nordica sunt feminine; participanții din sală sunt
și bărbați, și femei — adresarea către cursant e la masculin, forma neutră din română.)

**Cum le folosești:** fiecare participant **își instalează skill-urile propriului kit în Cowork** și apoi le
**adaptează** muncii lui reale (exact ce facem la Cursul 8 — modifici un skill ca să devină al tău). Skill-urile sunt
un punct de plecare, nu o cușcă: le rescrii pașii, le schimbi formatul de output, le legi de fișierele tale.

Setul complet de skill-uri trăiește în **`curs/skills/`** — un folder per skill, fiecare cu propriul `SKILL.md`.

> **Folosite live în timpul cursurilor:** câteva skill-uri sunt rulate chiar în lecții, nu doar instalate —
> `comparator-oferte` (Cursul 5), `profilare-date` (Cursul 6, are și cod: `scripts/profil_cheltuieli.py`),
> `generator-fisa-post` (Cursul 8), `reguli-de-casa` + `review-cu-subagenti` (Cursul 9, anunț de marketing +
> 3 subagenți), `verificare-firma-anaf` (Cursul 10, prin MCP la ANAF) și `digest-zilnic` (Cursul 11).
> (La Cursul 2 metoda de extragere a acțiunilor e folosită **direct, fără a porni un skill** — vezi
> `extragere-actiuni-sedinta` pentru aceeași metodă, ca skill de kit.)

---

## 1. PM / Team Lead Kit

Pentru product manageri și team leads — din notițe de ședință și update-uri scoți acțiuni, status și riscuri.

| Skill | Ce face | Rol Nordica / lecție |
|-------|---------|----------------------|
| `extragere-actiuni-sedinta` | Din notițe/transcript de ședință → listă de acțiuni cu responsabil + termen, fiecare ancorată în ce s-a spus. | Ioana (PM), **L2** — metoda e folosită direct (fără a porni skill-ul) |
| `status-report` | Asamblează un status report din progresul echipei, fiecare punct cu sursă. | Ioana (PM), kit propriu |
| `risk-tracker` | Ține evidența riscurilor: ce, probabilitate, impact, owner, plan de mitigare. | Ioana (PM), kit propriu |
| `brief-stakeholderi` | Sinteză scurtă pentru stakeholderi: unde suntem, ce ne blochează, ce decizii cer. | Ioana (PM), kit propriu |

## 2. Content & Community Kit

Pentru content & community — planifici, scrii variante și pregătești materialele de comunicare.

| Skill | Ce face | Rol Nordica / lecție |
|-------|---------|----------------------|
| `calendar-content` | Construiește un calendar de content din teme + date, gata de programat. | Bianca (Content), împletit + kit propriu |
| `reguli-de-casa` | Scrie un text de comunicare (anunț, postare, email) pe **regulile casei** Nordica — voce, ce promitem/ce nu; marchează „[de confirmat]", nu inventează. | Bianca (Content), **L9** — rulat live |
| `variante-postari` | Generează mai multe variante de postare dintr-un singur mesaj, pe canale diferite. | Bianca (Content), kit propriu |
| `asistent-seo` | Pregătește unghiul SEO al unui text: cuvinte-cheie, titluri, structură. | Bianca (Content), kit propriu |
| `asamblare-newsletter` | Asamblează un newsletter din piese de content existente, cu linkuri și CTA. | Bianca (Content), kit propriu |

## 3. HR Kit

Pentru HR / People Ops — din descrieri brute scoți fișe de post, onboarding și sinteze de oameni.

| Skill | Ce face | Rol Nordica / lecție |
|-------|---------|----------------------|
| `generator-fisa-post` | Din descriere brută de rol → fișă de post completă (pe `templates/fisa-postului.md`). | Raluca (HR), **L8** — rulat live |
| `checklist-onboarding` | Construiește un checklist de onboarding pentru un rol nou, pe etape. | Raluca (HR), kit propriu |
| `comparator-fise-rol` | Pune două fișe de post cap la cap ca să vezi suprapuneri și goluri. | Raluca (HR), kit propriu |
| `sintetizator-survey` | Sintetizează răspunsuri de survey în teme + citate, fără să inventeze procente. | Raluca (HR), kit propriu |

## 4. Finance & Admin Kit

Pentru financiar-administrativ — profilezi date, scoți rapoarte, explici variații și verifici cheltuieli. Aici
trăiește disciplina cifrelor: **fiecare număr vine din fișier, ghicitura „din memorie" se corectează prin calcul.**

| Skill | Ce face | Rol Nordica / lecție |
|-------|---------|----------------------|
| `profilare-date` | Profilează un CSV: rezumat pe coloane, totaluri pe categorii, anomalii + grafic HTML; corectează cifra „din memorie". | Mihaela (financiar), **L6** — rulat live |
| `raport-lunar` | Scaffold de raport lunar din date + `templates/raport-lunar.md`, fiecare cifră cu sursă. | Mihaela (financiar), kit propriu |
| `explicator-variatii` | Explică în română simplă variațiile dintr-un tabel (planificat vs realizat, lună de lună), doar din cifrele prezente. | Mihaela (financiar), kit propriu |
| `verificator-cheltuieli` | Verifică o listă de cheltuieli: duplicate, câmpuri lipsă, articole în afara politicii, totaluri care nu se adună. | Mihaela (financiar), L4/L6 |

## 5. Procurement Kit

Pentru procurement / operațiuni — compari oferte, scoți clauze și ții furnizorii ordonați. Lecția-cheie:
**cea mai ieftină ofertă nu câștigă dacă pică o cerință obligatorie.**

| Skill | Ce face | Rol Nordica / lecție |
|-------|---------|----------------------|
| `comparator-oferte` | Compară 2+ oferte pe un caiet de sarcini, marchează must-urile pass/fail, descalifică oferta care pică un must, recomandă cu rezerve. | Sorina (procurement), **L5** — rulat live |
| `extractor-clauze` | Extrage clauzele cheie dintr-un contract/ofertă (preț, durată, SLA, penalități, ieșire) cu fraza-sursă. | Sorina (procurement), kit propriu |
| `organizator-furnizori` | Strânge informații împrăștiate de furnizori într-un registru curat și comparabil. | Sorina (procurement), kit propriu |

## 6. Antreprenor Kit

Pentru fondatori / antreprenori — intri în zi cu un digest, triezi lead-uri și ții echipa pe aceeași pagină.
**Linie roșie peste tot: aduni și schițezi, nu trimiți nimic — omul apasă butonul final.**

| Skill | Ce face | Rol Nordica / lecție |
|-------|---------|----------------------|
| `digest-zilnic` | Din inbox + calendar → un paragraf + puncte: ce e azi, ce poate aștepta, programul, un „atenție"; nu trimite nimic. | Andreea (CEO), **L11** — rulat live |
| `sumarizator-lead-uri` | Rezumă și triază lead-urile în fierbinte/cald/rece, cu următoarea acțiune. | Andreea (CEO), kit propriu |
| `brief-saptamanal-echipa` | Brief săptămânal din update-uri: ce s-a livrat, ce e blocat, ce urmează, ce decizii cer. | Andreea (CEO), kit propriu |

## 7. Legal Kit

Pentru consilier juridic / DPO (și pentru oricine pune mâna pe un contract) — recenzezi contracte, verifici GDPR și
**verifici firmele la ANAF, în timp real**. Lecția-cheie: înainte să semnezi sau să facturezi, **întrebi sursa
oficială, nu fișierul.**

| Skill | Ce face | Rol Nordica / lecție |
|-------|---------|----------------------|
| `analiza-contract` | Recenzează un contract: termeni-cheie, clauze riscante, **ce lipsește**, întrebări de renegociat — fiecare cu articol-sursă. | Diana (Legal), material bonus (contractul din `scenarii/legal-contract/`) |
| `verificare-firma-anaf` | Verifică o firmă/o listă întreagă **live la ANAF** prin MCP (`demoanaf.ro`): stare, plătitor TVA, denumire oficială; semnalează nepotrivirile față de formular. | Diana (Legal), **L10** — rulat live |
| `verificare-gdpr` | Verifică un document/proces față de bazele GDPR: ce date, ce temei, ce lipsește (DPA, durată, drepturi). | Diana (Legal/DPO), kit propriu |
| `revizuire-nda` | Recenzează un NDA: unilateral/reciproc, definiția „confidențial", durată, riscuri și lipsuri. | Diana (Legal), kit propriu |

---

## Skill comun tuturor kiturilor

| Skill | Ce face | Lecție |
|-------|---------|--------|
| `review-cu-subagenti` | Pune un panel de 3 subagenți (context proaspăt) cu lentile potrivite documentului să recenzeze un rezultat — verificarea muncii. | **L9** — rulat live (PR / jurnalist sceptic / client), comun |

---

**Firul roșu, în toate kiturile:** AI-ul e instrument, nu sursă de adevăr. Orice cifră, clauză, nume sau termen vine
dintr-un fișier din folder; ce nu e confirmat se scrie „de verificat", nu se inventează. Tu instalezi skill-ul, îl
adaptezi, îl rulezi — dar **decizia finală și butonul de trimitere rămân ale omului.**
