---
name: brief-saptamanal-echipa
description: Construiește un brief săptămânal de echipă din update-urile membrilor — ce s-a livrat, ce e blocat, ce urmează și ce decizii sunt necesare. Folosește-l când cineva spune „fă-mi briefingul săptămânal", „adună update-urile echipei", „ce s-a livrat / ce e blocat săptămâna asta", „pregătește-mi sinteza pentru ședința de luni", „ce decizii avem de luat" sau are update-uri individuale și vrea o singură pagină pentru echipă/conducere. Nu inventează progres sau blocaje — fiecare punct vine din update-ul cuiva; ce lipsește se cere explicit.
---

# Brief săptămânal de echipă (brief-saptamanal-echipa)

Strânge update-urile individuale ale echipei într-un singur brief pe patru axe — livrat, blocat, urmează, decizii necesare — gata de citit înainte de ședința săptămânală. Partea care nu e trivială: distinge „în lucru" de „livrat" și scoate la suprafață blocajele și deciziile care altfel se pierd în text. Nu îl folosi pentru digestul personal al fondatoarei (acolo e `digest-zilnic`) și nici pentru triajul de lead-uri (acolo e `sumarizator-lead-uri`).

## Input
- Update-urile membrilor echipei (mesaje, note de ședință, rapoarte scurte).
- Opțional: săptămâna țintă și obiectivul mare al perioadei (ex. lansarea v2.0), ca să poți marca ce contribuie la el.

## Metodă
1. Citește fiecare update și clasează fiecare punct: livrat / în lucru / blocat / decizie necesară.
2. **Livrat:** doar ce e clar terminat în update — nu treci „aproape gata" la livrat.
3. **Blocat:** numește blocajul, cine e afectat și (dacă scrie) ce/cine îl deblochează.
4. **Urmează:** ce și-a asumat fiecare pentru săptămâna viitoare.
5. **Decizii necesare:** întrebările deschise care cer un om să decidă, cu cine trebuie să decidă.
6. Marchează cine n-a trimis update („update lipsă: X") — nu inventa progresul lui.

## Output (obligatoriu)
- **✅ Livrat săptămâna asta** (puncte, cu cine).
- **⛔ Blocat** (blocaj · afectat · ce-l deblochează).
- **➡️ Urmează** (per persoană sau temă).
- **❓ Decizii necesare** (întrebarea · cine decide).
- **Update-uri lipsă** (cine n-a raportat).

## Disciplină (firul roșu)
Fiecare punct trimite la update-ul unei persoane reale — nu inventezi progres, blocaje sau decizii. „Aproape gata" nu e „livrat". Pentru cine n-a raportat, scrii „update lipsă", nu completezi tu. Briefingul e o ciornă pentru om — el confirmă, adaugă context și îl prezintă echipei; tu nu îl trimiți și nu iei deciziile din secțiunea „decizii necesare".
