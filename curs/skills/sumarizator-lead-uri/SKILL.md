---
name: sumarizator-lead-uri
description: Rezumă și triază lead-urile primite în cald / cald-tiepid / rece, cu următoarea acțiune pentru fiecare. Folosește-l când cineva spune „triază-mi lead-urile", „care lead-uri sunt fierbinți", „rezumă-mi cererile de la potențiali clienți", „pune lead-urile în ordine de prioritate", „ce fac cu lead-urile astea" sau are cereri/mesaje de la potențiali clienți și vrea să știe pe cine să sune întâi. Nu inventează interes sau buget care nu reiese din mesaj — ce nu e clar rămâne „de calificat".
---

# Sumarizator de lead-uri (sumarizator-lead-uri)

Ia un set de lead-uri primite (formulare, emailuri, mesaje) și le împarte în fierbinte / cald / rece, fiecare cu un rezumat de o frază și următoarea acțiune concretă. Partea care nu e trivială: clasarea se face din semnale reale din mesaj (buget pomenit, urgență, potrivire cu oferta), nu din optimism — un lead entuziast fără fit rămâne cald, nu fierbinte. Nu îl folosi pentru digestul general al fondatoarei (acolo e `digest-zilnic`) și nici pentru briefingul de echipă (acolo e `brief-saptamanal-echipa`).

## Input
- Un set de lead-uri: mesaje de formular, emailuri, mesaje directe.
- Opțional: criteriile proprii de calificare (ce înseamnă „fierbinte" pentru afacerea ta — buget, mărime, urgență, fit).

## Metodă
1. Pentru fiecare lead, extrage: cine, ce vrea, ce semnale de interes/buget/urgență apar în text.
2. Clasează: **🔥 fierbinte** (semnal clar de cumpărare + fit), **🌤 cald** (interes real, nelămurit pe buget/timp), **❄ rece** (curiozitate, fără fit sau fără semnal).
3. Justifică clasarea cu fraza din mesaj pe care te-ai bazat.
4. Dă următoarea acțiune concretă per lead (sună azi / trimite ofertă / cere clarificare / pune pe lista de nurturing).
5. Marchează ce informație lipsește pentru o calificare bună („de calificat: buget necunoscut").

## Output (obligatoriu)
- **Tabel de lead-uri:** nume/sursă · ce vrea · clasă (🔥/🌤/❄) · semnalul-sursă · următoarea acțiune.
- **Top de azi:** lead-urile fierbinți, în ordinea în care merită contactate.
- **De calificat:** ce date lipsesc per lead pentru o decizie sigură.

## Disciplină (firul roșu)
Clasarea se sprijină pe ce scrie efectiv în mesaj — nu inventezi buget, urgență sau intenție de cumpărare. Un lead fără semnal clar nu devine „fierbinte" pentru că ar fi convenabil; rămâne cald/rece cu „de calificat". Acțiunile sunt propuneri; omul decide pe cine sună și ce trimite — tu nu contactezi pe nimeni.
