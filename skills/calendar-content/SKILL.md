---
name: calendar-content
description: Construiește un calendar de content pe o săptămână (sau mai mult) pornind de la o temă/obiectiv — pe zile, cu canal, format, hook, mesaj și CTA. Folosește-l când cineva spune „fă-mi un calendar de content", „plan de postări pe săptămâna asta", „ce postăm și când", „content calendar pentru lansare", „idei de postări pe teme". Pornește de la mesaje reale din folder/brief, nu inventează rezultate sau cifre de performanță.
---

# Calendar de content (calendar-content)

Transformă un obiectiv („vrem să creăm așteptare pentru lansarea v2.0") într-un plan concret de postări pe zile, cu canal, format, hook și CTA pentru fiecare. Greul e să distribui mesajele coerent (nu trei postări identice, nu toate pe LinkedIn) și să legi fiecare postare de un obiectiv real, nu să umpli un grid. Nu folosi acest skill pentru a rescrie un singur mesaj pe mai multe canale (vezi `variante-postari`) sau pentru a asambla un newsletter (vezi `asamblare-newsletter`).

## Input
- Tema/obiectivul perioadei (lansare, recrutare, conținut educativ etc.).
- Opțional: canalele disponibile, frecvența dorită, materiale existente din folder.

## Metodă
1. Clarifică **obiectivul** și **perioada** (câte zile, ce canale). Dacă lipsesc, întreabă o dată, scurt.
2. Listează **unghiurile** care servesc obiectivul (ex. behind-the-scenes, beneficiu pentru client, întrebare-cârlig, social proof) — fiecare e o postare, nu o repetiție.
3. Distribuie unghiurile pe **zile** și **canale**, potrivind formatul cu canalul (carusel pe Instagram, text lung pe LinkedIn, scurt pe newsletter teaser).
4. Pentru fiecare zi scrie: **hook** (prima linie care oprește scroll-ul), **mesaj** (ce comunici), **CTA** (ce vrei să facă cititorul).
5. Evită canibalizarea: nu pune același mesaj de două ori în aceeași săptămână fără variație.
6. Marchează ce **materiale** lipsesc (poză, citat, link) ca „de pregătit".

## Output (obligatoriu)
Un calendar în `outputs/` (ex. `outputs/calendar-content-<tema>.md`):

| Ziua | Canal | Format | Hook | Mesaj (pe scurt) | CTA | Material necesar |
|------|-------|--------|------|------------------|-----|------------------|
| Luni | LinkedIn | text + imagine | „Am reconstruit calendarul de la zero." | De ce v2.0 | „Spune-ne ce te enervează acum" | screenshot UI nou |
| Marți | Instagram | carusel | … | … | … | de pregătit |

Sub tabel: o listă scurtă **„De pregătit"** cu materialele lipsă.

## Disciplină (firul roșu)
- Mesajele se sprijină pe **fapte reale** din brief/folder. Nu inventa funcționalități, date de lansare sau cifre („+200% utilizatori") ca să umpli un hook.
- Nu promite în CTA lucruri pe care firma nu le poate susține.
- Materialele care nu există încă se marchează „de pregătit", nu se presupun gata.
- Calendarul e o schiță editorială: omul aprobă tonul și mesajul înainte de publicare (regula automatizării: schițezi, nu postezi).
