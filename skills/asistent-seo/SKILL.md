---
name: asistent-seo
description: Îmbunătățește un text/articol pentru SEO fără keyword-stuffing — propune titlu, meta description, structură de headinguri și legături interne, fiind sincer despre ce nu poate verifica (volume de căutare, poziții). Folosește-l când cineva spune „optimizează articolul ăsta pentru SEO", „fă-mi un meta description", „cum stau cu SEO la textul ăsta", „titlu și headinguri SEO", „internal linking". Nu inventează date de trafic sau volume de cuvinte-cheie.
---

# Asistent SEO (asistent-seo)

Ia un draft existent și îl face mai descoperibil în căutări — titlu și meta atrăgătoare, structură de headinguri logică, sugestii de legături interne — fără să-l umple de cuvinte-cheie care strică lectura. Greul e echilibrul: optimizezi pentru motor și pentru om în același timp, și ești **sincer** despre ce un model nu poate ști fără unelte (volume reale de căutare, dificultatea unui cuvânt, poziția actuală). Nu folosi acest skill pentru a scrie textul de la zero (vezi `copywriting`/`copy-editing` din librărie) sau pentru variante pe canale sociale (vezi `variante-postari`).

## Input
- Draftul/articolul de optimizat (`.md` sau text).
- Opțional: cuvântul-cheie principal vizat și lista altor pagini ale site-ului (pentru legături interne).

## Metodă
1. Citește draftul și identifică **tema principală** și un **cuvânt-cheie natural** (cel pe care textul deja îl servește), nu unul forțat.
2. Propune un **titlu** (sub ~60 caractere, conține tema, e atrăgător) și o **meta description** (~150 caractere, promite valoare, conține cuvântul-cheie firesc).
3. Verifică **structura de headinguri**: un singur H1, H2/H3 logice, fiecare secțiune scanabilă. Propune o ierarhie curată.
4. Sugerează **legături interne** doar către pagini reale din lista dată; dacă nu ai listă, descrie tipul de pagină de legat („leagă spre pagina de prețuri"), marcat „de confirmat URL".
5. Verifică densitatea: dacă un cuvânt-cheie apare nefiresc de des, semnalează keyword-stuffing și propune rescriere naturală.
6. Spune clar ce **nu poți verifica** fără unealtă SEO (volum, dificultate, poziție, intenție de căutare reală).

## Output (obligatoriu)
Un fișier în `outputs/` (ex. `outputs/seo-<articol>.md`):

```
## Titlu propus
<…> (xx caractere)

## Meta description
<…> (xx caractere)

## Structură headinguri (propusă)
H1: …
  H2: …
    H3: …

## Legături interne sugerate
- spre <pagină> — context: <unde în text> — [de confirmat URL]

## Semnale de risc
- <keyword-stuffing / paragraf prea lung / titlu duplicat>

## Ce NU pot verifica fără unealtă SEO
- volume de căutare, dificultate cuvânt, poziție actuală, intenția reală — necesită Ahrefs/GSC/etc.
```

## Disciplină (firul roșu)
- **Nu inventa cifre SEO** — volume de căutare, „dificultate 35", „locul 4 pe Google". Dacă nu vin dintr-o unealtă, scrie explicit că nu pot fi verificate aici.
- Legăturile interne se propun doar către pagini care **există**; URL-urile neconfirmate se marchează „de confirmat".
- Optimizarea nu strică lectura: dacă o sugestie face textul robotic, semnaleaz-o ca dezavantaj, nu o impune.
- Output.ul e o listă de propuneri pe care omul le aprobă înainte de publicare.
