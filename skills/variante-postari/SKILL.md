---
name: variante-postari
description: Ia un singur mesaj/anunț și produce variante adaptate pe canale (LinkedIn, Instagram, newsletter, X) — același adevăr, formă diferită pentru fiecare audiență. Folosește-l când cineva spune „fă-mi variante pentru fiecare canal", „adaptează postarea asta pentru LinkedIn și Instagram", „cum sună asta în newsletter", „variante de anunț", „același mesaj, mai multe rețele". Păstrează faptele identice între variante; nu inventează detalii noi pentru un canal anume.
---

# Variante de postări pe canale (variante-postari)

Pornește de la un mesaj-sursă (un anunț, o veste, un beneficiu) și scoate versiuni croite pe fiecare canal — LinkedIn vrea altceva decât Instagram, care vrea altceva decât newsletterul. Greul e să păstrezi **același adevăr** în toate (aceeași dată, același preț, aceeași promisiune) în timp ce schimbi tonul, lungimea și cârligul. Nu folosi acest skill pentru a planifica ce postezi și când (vezi `calendar-content`) sau pentru a asambla un newsletter întreg (vezi `asamblare-newsletter`).

## Input
- Mesajul-sursă: ce vrei să comunici (anunț, beneficiu, invitație).
- Opțional: canalele țintă și tonul brandului.

## Metodă
1. Extrage **nucleul de adevăr** din mesajul-sursă: faptele care nu au voie să se schimbe (dată, preț, loc, promisiune, link).
2. Pentru fiecare canal, adaptează:
   - **LinkedIn:** ton profesional, poveste sau insight, paragrafe scurte, 1 CTA.
   - **Instagram:** vizual-întâi, hook în prima linie, hashtag-uri relevante, ton cald.
   - **Newsletter:** subiect + intro personal + corp + CTA clar, ton de „scriu eu către tine".
   - **X/Twitter:** scurt, un singur cârlig, eventual thread dacă merită.
3. Variază hook-ul și forma, **nu faptele**. Verifică la final: toate variantele spun același lucru despre dată/preț/promisiune?
4. Marchează orice loc unde un canal cere un detaliu care nu e în sursă (ex. dimensiune imagine) ca „de pregătit".

## Output (obligatoriu)
Un fișier în `outputs/` (ex. `outputs/variante-<mesaj>.md`), o secțiune per canal:

```
## LinkedIn
<textul variantei>
CTA: <…>

## Instagram
<textul variantei>
Hashtag-uri: <…>

## Newsletter
Subiect: <…>
<corpul>

## Nucleu de adevăr (verificare)
- Dată: <…> · Preț: <…> · Link: <…>  (identice în toate variantele)
```

## Disciplină (firul roșu)
- **Nucleul de adevăr e identic în toate variantele.** Dacă o variantă schimbă data, prețul sau promisiunea, e o eroare, nu o „adaptare".
- Nu inventa detalii ca să umpli un canal (testimoniale, cifre, beneficii care nu sunt în sursă).
- Secțiunea de verificare a nucleului e obligatorie — e plasa de siguranță contra derapajului între variante.
- Variantele sunt schițe: omul aprobă și apasă „publică" (regula automatizării — schițezi, nu postezi).
