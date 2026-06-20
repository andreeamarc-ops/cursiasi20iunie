---
name: analiza-contract
description: Recenzează un contract (prestări servicii, furnizor, colaborare) și scoate la suprafață clauzele riscante, lipsurile și termenii-cheie, în limbaj clar — nu juridic încâlcit. Folosește-l când cineva spune „uită-te pe contractul ăsta", „ce riscuri are contractul", „verifică-mi contractul înainte să semnez", „ce clauze lipsesc", „rezumă-mi contractul" sau vrea o părere structurată înainte de semnare. NU înlocuiește un avocat — pregătește decizia pentru un om.
---

# Analiză de contract (analiza-contract)

Folosește acest skill când ai un contract și vrei să-l înțelegi și să-i vezi riscurile *înainte* de semnare.
Partea grea nu e să citești contractul, ci să observi **ce lipsește** și **ce e formulat în dezavantajul tău** —
lucruri care nu sar în ochi la o citire rapidă. Nu îl folosi pentru un NDA (acolo e `revizuire-nda`) sau pentru
conformitatea GDPR a unui proces (acolo e `verificare-gdpr`). **Nu e consultanță juridică** — e o pregătire a
deciziei pentru un om (idel un consilier juridic).

## Input
- Un contract (`.md`, `.pdf`, `.docx`) — ex. `scenarii/legal-contract/contract-furnizor.md`.
- Opțional: din ce poziție citești (beneficiar/prestator) și ce te îngrijorează cel mai mult.

## Metodă
1. **Termeni-cheie, pe scurt.** Extrage într-un tabel: obiect, durată, preț și mod de plată, reînnoire, SLA,
   răspundere, confidențialitate, date personale (DPA), încetare, lege/jurisdicție. Fiecare cu **articolul-sursă**.
2. **Clauze riscante.** Marchează ce e în dezavantajul tău sau neobișnuit: reînnoire automată cu preaviz lung,
   plată în avans, SLA fără penalități, plafon de răspundere absent sau ciudat, jurisdicție la sediul celuilalt.
3. **Ce lipsește.** La fel de important: acord de prelucrare a datelor (DPA), drept de export al datelor la
   încetare, durata confidențialității după încetare, plafon de răspundere — absențele sunt riscuri.
4. **Semnalează, nu rescrie.** Nu inventa clauze și nu „repara" contractul singur — propune ce ar trebui clarificat
   sau renegociat, în limbaj clar.
5. **Întrebări pentru cealaltă parte / pentru avocat.** O listă scurtă, acționabilă.

## Output (obligatoriu)
Un fișier în `outputs/` cu: (1) tabelul de termeni-cheie cu articol-sursă, (2) **Clauze riscante** (cu de ce),
(3) **Ce lipsește**, (4) **Întrebări / de renegociat**, (5) o concluzie de 2 rânduri „verde / cu rezerve / nu
semna încă". Fiecare punct ancorat în articolul din contract.

## Disciplină (firul roșu)
Fiecare observație trimite la un articol real din contract — citat, nu parafrazat din burtă. Nu inventa clauze,
sume sau termene; ce nu scrie în contract e o **lipsă de semnalat**, nu o presupunere. Acesta NU e aviz juridic:
decizia de a semna și negocierea rămân la om (consilier juridic / avocat). Spune clar ce trebuie confirmat de un
specialist.
