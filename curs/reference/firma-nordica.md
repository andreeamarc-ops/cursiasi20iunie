# Nordica — firma fictivă din atelier (context comun)

> Acesta este universul în care lucrăm toată ziua. **Totul e fictiv** — firma, oamenii, cifrele. Îl tratăm ca pe
> muncă reală (verificăm fiecare cifră în fișier), dar nimic de aici nu e un proiect adevărat al cuiva din sală.
> Cele șapte Starting Kit-uri (PM, Content, HR, Financiar, Procurement, **Legal**, Antreprenor) sunt roluri din
> Nordica, ca toate domeniile să se simtă ca un singur loc de muncă, nu ca demo-uri separate.
>
> Notă: **sala e formată numai din femei** — toate personajele Nordica sunt femei, iar tot ce produci se adresează
> unei audiențe feminine (acord gramatical la feminin acolo unde se aplică).

## Ce e Nordica

**Nordica** e o firmă mică din **Iași**, ≈15 oameni, care construiește **Nordica Booking** — o aplicație de
programări online pentru saloane, cabinete și clinici mici (clientul își ia singur o programare; firma-client
gestionează calendarul și plățile). E pe piață de doi ani, are câteva sute de clienți-firme și **lansează acum
versiunea 2.0** (calendar reproiectat, plăți integrate, notificări SMS). Lansarea v2.0 e firul care leagă toate
scenariile.

## Oamenii (cine apare în scenarii)

| Nume | Rol | Apare în |
|------|-----|----------|
| **Andreea Pop** | Fondatoare / CEO | L11 (digest zilnic inbox+calendar), prezentă peste tot |
| **Ioana Marin** | Product Manager | L2 (ședința de kickoff v2.0) |
| **Bianca Radu** | Content & Community | împletit (variante de anunț, calendar de content) |
| **Raluca Ene** | HR / People Ops | L8 (angajare Customer Success) |
| **Mihaela Dobre** | Office manager / financiar-administrativ | L4 (folderul dezordonat) + L6 (cheltuieli) |
| **Sorina Vlad** | Operațiuni / procurement | L5 (alegerea unui furnizor de help-desk) |
| **Diana Ionescu** | Legal & DPO (consilier juridic) | L9 (review de contract) + L10 (verificare clienți la ANAF) |

(Restul echipei — 2 developeri, un designer, 3 oameni pe suport, 2 pe vânzări — există în fundal, nu apar
nominal.)

## Firul comun: lansarea Nordica Booking v2.0

Data țintă internă a lansării: **15 septembrie 2026**. În jurul ei se învârt toate scenariile:

- **PM (L2):** Ioana ține ședința de kickoff a lansării — cine ce face până la 15 sept.
- **Administrativ (L4):** Mihaela are un folder dezordonat cu pontaje, ciorne de raport și notițe despre proiect.
  Una dintre ciorne are o **cifră de buget greșită „din memorie"** — capcana care se corectează la L6.
- **Procurement (L5):** Sorina alege un **furnizor de help-desk/suport** (pentru valul de tichete așteptat după
  lansare), comparând trei oferte față de un caiet de sarcini. Una dintre oferte nu respectă o cerință obligatorie
  — capcana de la L5.
- **Financiar (L6):** Mihaela analizează `cheltuieli-2026.csv` (execuția bugetară a firmei) și **corectează exact
  cifra greșită** semnalată la L4.
- **HR (L8):** Raluca angajează un **Customer Success Specialist** pentru clienții noi de după lansare; pornește
  de la o descriere brută și scoate o fișă de post.
- **Legal (L9 & L10):** Diana, consilier juridic, are două sarcini legate de lansare. La **L9** recenzează
  **contractul cu DeskNord** (furnizorul de help-desk recomandat la L5) înainte de semnare — un panel de subagenți
  caută clauze riscante și lipsuri. La **L10** verifică **automat lista de clienți-firme** ale Nordicăi direct la
  **ANAF** (prin MCP, serviciul real `demoanaf.ro`): care firme sunt active, plătitoare de TVA, ca facturarea de
  după lansare să fie corectă.
- **Antreprenor (L11):** Andreea vrea în fiecare dimineață un **digest** din inbox + calendar, ca să intre în zi
  cu un singur paragraf, nu cu 40 de emailuri.

## Capcane intenționate (de ce există)

Sunt acolo ca participantul să simtă pe pielea lui **reflexul 4 — verifică în sursă**:

1. **Cifra „din memorie" (L4 → L6).** În `scenarii/folder-haos-admin/`, o ciornă de raport afirmă un buget
   cheltuit „din cap" care **nu corespunde** cu suma reală din `scenarii/date/cheltuieli-2026.csv`. La L4 o
   semnalezi ca neconfirmată; la L6 calculezi suma reală din CSV și o corectezi. Cele două fișiere trebuie să fie
   **deliberat în dezacord**.
2. **Oferta care încalcă caietul de sarcini (L5).** Una dintre cele trei oferte din `scenarii/oferte-furnizori/`
   pare cea mai ieftină dar **nu respectă o cerință obligatorie** din `caiet-de-sarcini.md` (ex. fără suport în
   limba română, sau fără SLA). Cea „mai ieftină" nu e cea care câștigă — exact lecția.

## Reguli de ton pentru tot ce produci în numele Nordicăi

- Română cu diacritice (ă â î ș ț), ton de coleg, fără jargon corporatist gol.
- Orice cifră vine dintr-un fișier din folder. Ce nu e confirmat → „de verificat", nu inventat.
- Date sensibile reale (clienți, salarii, contracte adevărate) **nu** se încarcă în exercițiu — lucrăm doar cu
  Nordica.
