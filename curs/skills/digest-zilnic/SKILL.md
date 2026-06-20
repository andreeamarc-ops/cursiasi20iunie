---
name: digest-zilnic
description: Construiește un digest de dimineață dintr-un inbox + calendar (de ex. scenarii/inbox-antreprenor/): un paragraf de sus + puncte cu ce are nevoie fondatoarea AZI, ce poate aștepta, programul zilei și un „atenție" de un rând. Folosește-l când cineva spune „fă-mi digestul de dimineață", „rezumă-mi inboxul + calendarul", „ce trebuie să fac azi", „cu ce intru în zi", „brief de dimineață" sau vrea să intre în zi cu un singur paragraf, nu cu 40 de emailuri. LINIE ROȘIE: adună și schițează, nu trimite niciodată nimic.
---

# Digest zilnic (digest-zilnic)

Citește un inbox plus un calendar și produce briefingul de dimineață al fondatoarei: un paragraf scurt care prinde esența zilei, apoi puncte clare — ce cere acțiune azi, ce poate aștepta, ce e pe agendă și un singur „atenție". Partea care nu e trivială: triază după ce contează pentru fondatoare *azi*, nu repetă fiecare email; și nu confundă urgent cu zgomotos. Nu îl folosi pentru a califica lead-uri de vânzări (acolo e `sumarizator-lead-uri`) și nici pentru briefingul de echipă săptămânal (acolo e `brief-saptamanal-echipa`).

## Input
- Un set de emailuri / mesaje (de ex. `scenarii/inbox-antreprenor/`).
- Un calendar / agenda zilei (evenimente cu oră).
- Opțional: ce înseamnă „important" pentru această fondatoare (clienți, lansare, bani, oameni).

## Metodă
1. Parcurge inboxul; pentru fiecare mesaj decide: cere acțiune AZI / poate aștepta / e doar informativ.
2. Citește calendarul și ordonează cronologic evenimentele zilei, cu ora și ce pregătire cer.
3. Scrie paragraful de sus: 3–4 fraze cu pulsul zilei (ce e în joc, ce nu poate fi ratat).
4. Fă buletele: „Azi" (acțiuni de făcut), „Poate aștepta", „Programul zilei".
5. Scrie un singur „⚠️ Atenție" de un rând — riscul/sensibilul zilei (un client supărat, un termen, o plată).
6. Pentru orice cere răspuns/trimitere, **schițează** o ciornă marcată clar ca ciornă — nu o trimite.

## Output (obligatoriu)
- **Paragraf de dimineață** (3–4 fraze, pulsul zilei).
- **Azi** (puncte: ce are nevoie fondatoarea azi, cu de ce).
- **Poate aștepta** (puncte scurte).
- **Programul zilei** (cronologic, cu ore).
- **⚠️ Atenție** (un singur rând).
- Ciornele de răspuns (dacă există) marcate „CIORNĂ — de aprobat și trimis de om".

## Disciplină (firul roșu)
Fiecare punct vine dintr-un email sau eveniment real din folder — fără sarcini inventate. Nu trimiți, nu confirmi, nu accepți/refuzi nimic în numele fondatoarei: aduni și schițezi, omul apasă butonul. Ce nu e clar din mesaje (cine, când, cât) se marchează „de verificat", nu se presupune. Prioritizarea e o propunere — fondatoarea rearanjează cum vrea.
