---
name: review-cu-subagenti
description: Recenzează critic un document pe care l-ai produs deja (o comparație de oferte, un raport, o fișă, un brief) lansând 3 subagenți în paralel, fiecare cu context proaspăt și un unghi distinct — corectitudine, claritate, riscuri/lipsuri — apoi consolidează ce găsesc. Folosește-l când cineva spune „verifică-mi munca", „dă-i un review documentului ăsta", „generează 3 subagenți care să-l critice", „pune pe cineva să-l conteste", „ce am ratat în raportul ăsta", „control de calitate pe documentul X". Subagentul = context proaspăt; skill-ul = metodă reutilizabilă — folosește-le împreună.
---

# Review cu subagenți (review-cu-subagenti)

Pune un document deja făcut sub trei perechi de ochi proaspete în același timp: trei subagenți care **nu au văzut** cum a fost construit, fiecare cu un singur unghi de atac, ca să prindă ce un autor obosit de propriul text nu mai vede. Ideea-cheie a atelierului: un **subagent** pornește cu **context proaspăt** (nu moștenește presupunerile tale), pe când un **skill** e o **metodă reutilizabilă** (acest fișier). Le folosești împreună: skill-ul descrie *cum* lansezi subagenții. Nu folosi acest skill ca să produci documentul (folosește skill-ul de creație potrivit întâi) — se aplică pe ceva deja gata.

## Input
- Documentul de recenzat (un output deja produs: o comparație de oferte, un raport, o fișă de post, un brief).
- Opțional: sursele pe care s-a bazat documentul (ca subagentul de corectitudine să poată verifica față de ele).

## Metodă
1. Confirmă că documentul **există deja** și identifică sursele lui (dacă există), ca verificarea să aibă contra ce să se facă.
2. **Alege 3 lentile potrivite documentului** — nu sunt fixe, le potrivești cu tipul de text. Două seturi des folosite:
   - **Document de lucru intern** (raport, comparație, fișă): **Corectitudine** (cifrele/afirmațiile se susțin în surse?) · **Claritate** (se înțelege, e bine structurat?) · **Riscuri / lipsuri** (ce lipsește, ce ipoteză tacită e periculoasă?).
   - **Text public de marketing/comunicare** (anunț, postare, email): **PR** (servește mesajul, e pe vocea brandului, convinge?) · **Jurnalist sceptic** (ce afirmație nedovedită ar ataca un ziarist critic? unde e hype neacoperit?) · **Client potențial** (mi se adresează? am încredere? ce e neclar, ce obiecție îmi rămâne?).
   Dacă participantul cere explicit anumite lentile (ex. „PR, jurnalist sceptic, client"), folosește exact pe ale lui.
3. Lansează **3 subagenți în paralel**, fiecare cu **context proaspăt** și o singură lentilă (din cele alese).
4. Fiecare subagent returnează o listă scurtă de constatări, fiecare **ancorată** în locul din document (citat/secțiune).
5. Consolidează: strânge constatările sub cele trei etichete, elimină duplicatele, ordonează după gravitate.
6. Separă constatările factuale (subagentul le poate susține) de **deciziile care rămân ale omului**.

## Output (obligatoriu)
Un raport de review în `outputs/` (ex. `outputs/review-<document>.md`):

```
# Review — <document> — <data>

## Corectitudine (Subagent 1)
- [gravitate] <constatare> — în document: „<citat/secțiune>"

## Claritate (Subagent 2)
- <constatare> — în document: „…"

## Riscuri / lipsuri (Subagent 3)
- <constatare> — în document: „…"

## Ce trebuie decis de om
- <alegeri pe care review-ul le ridică dar nu le poate lua în locul omului>
```

## Disciplină (firul roșu)
- Fiecare constatare e **ancorată** în document (și, pentru corectitudine, verificată față de sursă). Subagenții nu inventează probleme și nu „îmbunătățesc" textul — îl critică factual.
- Subagentul de corectitudine nu inventează cifra corectă dacă nu o are din surse: semnalează „de verificat în sursă", nu ghicește.
- Review-ul **nu rescrie** documentul și nu decide în locul omului — secțiunea „Ce trebuie decis de om" e obligatorie.
- Distincția se respectă: subagent = context proaspăt pentru o privire nouă; skill = metoda asta, reutilizabilă pe orice document.
