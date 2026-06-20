---
name: revizuire-nda
description: Recenzează un acord de confidențialitate (NDA) și spune dacă e echilibrat, ce e riscant și ce lipsește. Folosește-l când cineva spune „uită-te pe NDA-ul ăsta", „e corect acordul de confidențialitate", „pot să semnez NDA-ul", „ce riscuri are NDA-ul" sau primește un NDA înainte de o colaborare/discuție. NU e aviz juridic — pregătește decizia pentru un om.
---

# Revizuire NDA (revizuire-nda)

Folosește acest skill când ai un acord de confidențialitate și vrei să știi, repede și clar, dacă e echilibrat
înainte să-l semnezi. Partea grea: un NDA pare scurt și inofensiv, dar detaliile (cât durează, ce intră în „secret",
ce te obligă) pot fi dezechilibrate. Pentru un contract complet de servicii folosește `analiza-contract`; pentru
conformitate GDPR, `verificare-gdpr`. **Nu e consultanță juridică.**

## Input
- Un NDA (`.md`, `.pdf`, `.docx`).
- Opțional: din ce poziție îl semnezi și ce informații împarți tu vs. primești.

## Metodă
1. **Tip și echilibru.** E **unilateral** (doar tu te obligi) sau **reciproc** (ambele părți)? Cine e protejat?
2. **Ce e „informație confidențială".** Definiția e prea largă (orice) sau rezonabilă? Există excepții uzuale
   (informație publică, deja cunoscută, dezvoltată independent, cerută de lege)?
3. **Durata.** Cât ține obligația — pe durata discuției + câți ani după? Marchează durate neobișnuit de lungi sau
   nelimitate.
4. **Obligații și restricții.** Ce te obligă concret (non-solicitare, non-concurență ascunsă în NDA, returnarea
   datelor)? Atenție la clauze care depășesc confidențialitatea.
5. **Riscuri și lipsuri.** Penalități disproporționate, lege/jurisdicție incomodă, lipsa excepțiilor uzuale.

## Output (obligatoriu)
Un fișier în `outputs/` cu: (1) **Tip & echilibru** (unilateral/reciproc), (2) tabel **clauză → ce înseamnă → e ok?**,
(3) **Riscuri & lipsuri**, (4) concluzie „semnezi liniștită / cu modificări / nu încă". Fiecare punct ancorat în
clauza-sursă.

## Disciplină (firul roșu)
Citează clauza pentru fiecare observație — nu parafraza din memorie. Nu inventa termene sau excepții; absența unei
excepții uzuale e un risc de semnalat, nu o presupunere. NU e aviz juridic: decizia de semnare rămâne la om; spune
ce ar trebui confirmat de un avocat.
