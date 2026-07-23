# La lente del VC — come ragiona un investitore (modalità EVALUATOR)

Reference per valutare una startup con il modello mentale di chi mette capitale di rischio.
Non cambia la domanda centrale dell'evaluator (team/capability/capitale sul problema giusto):
la **completa** con la logica economica del fondo. Resta valido `NOT_INVESTMENT_ADVICE`.

## 1. La matematica del fondo (perché il VC ragiona per outlier)

Un fondo VC tipico: dimensione es. $100M, durata ~10 anni, commissioni **2/20**, hurdle
degli LP ~**12%/anno**. Su 10 anni, 1,12^10 ≈ **3,1x**: il fondo deve restituire ~3x lordo
**prima** che il GP guadagni carry. Ma i ritorni seguono una **power-law**: in uno scenario
realistico ~metà delle società rende <1x, poche fanno il grosso del risultato. Conseguenza:

> Il VC non cerca "una buona azienda". Cerca poche aziende che possano restituire **da sole
> una quota rilevante (idealmente l'intero) fondo**. Questo è il *fund-returner test*.

**Domanda di screening che ne deriva (spesso assente nei pitch):**
*"Se tutto va bene, questa società è abbastanza grande da essere un fund-returner? L'upside
giustifica il capitale di rischio, o è un'ottima azienda ma non venture-scale?"*

Nota onesta: molte startup valide **non** sono venture-backable (e va benissimo: bootstrap,
debito, grant, corporate). Per un valutatore **angel/VC** la non-venture-scale è un motivo di
"pass"; per **open innovation / corporate pilot** la fund-math NON si applica — lì conta il fit
strategico, non il moltiplicatore. Dichiara sempre da quale cappello stai valutando.

## 2. I 4 rischi da ridurre (mappa sugli strumenti)

Il VC investe per **ridurre rischio** tappa dopo tappa. Classifica le evidenze in 4 rischi:

- **Development risk** — il prodotto/tecnologia si può davvero costruire? (→ strumenti 1, 7,
  10; capability vs use case)
- **Market risk** — esiste domanda reale, TAM grande, timing giusto? (→ 3, 4, 6; "perché ora")
- **Execution risk** — il team sa costruire e scalare? (→ 8 team, 5 GTM/persona, traction)
- **Finance risk** — quanto capitale serve, runway, prossimi round raccoglibili, cap table
  sana? (→ 9 pitch/fundraising, 12 unit economics)

Per ogni rischio: qual è l'evidenza? è ridotto o aperto? è la prossima cosa da de-riskare?

## 3. Le 5 T (checklist di screening rapido)

- **Team** — coeso e capace di execution? founder-market fit? (→ str. 8)
- **TAM** — mercato *davvero* enorme e credibile bottom-up? (→ str. 6; usa l'add-on Scalable
  per comparabili reali)
- **Technology** — c'è qualcosa di leva, scalabile, difendibile tecnicamente? (→ str. 7)
- **Traction** — cosa mostra **ora**? crescita rapida, pull reale, non vanity metrics? (→ str. 4, 6)
- **Trenches** — quali posizioni difensive / moat? switching cost, rete, IP, dati? (→ str. 8b
  replication risk)

Una T debole non è una condanna: è un rischio da nominare e una domanda da fare al founder.

## 4. Tre lenti dal principio "valuation = belief con numeri attaccati"

La domanda del founder è "quanto vale la mia azienda?"; quella dell'investitore è **"quanto
rischio resta prima che questa diventi molto più grande?"**. Due startup con la stessa revenue
prendono valuation diverse non per lo spreadsheet ma per la **storia**: stesso foglio, rischio
residuo diverso. Da qui tre lenti operative (NON danno un numero, espongono un gap).

### 4a. Valuation come rischio residuo, non come multiplo
Quando il materiale include una valuation o un multiplo, **non** giudicare se il numero è
"giusto". Valuta invece: **quale rischio è già stato rimosso** (problema, GTM, retention,
team, finance) e **quale resta aperto**? Il numero chiede una fiducia *proporzionata* al
rischio rimosso, o poggia su un "magic multiple" non dimostrato (AI multiple, founder-market
fit, strategic premium, "premio strategico")? Se il premio si regge su una narrativa di
fiducia non supportata da evidenze, segnala `VALUATION_BELIEF_GAP` (+ `VALUATION_METHOD_RISK` /
`COMPARABLES_SCALE_MISMATCH` se da comparabili). Formula: *"La valuation è una confidence score
sul rischio che resta: qui il numero presuppone già rimossi rischi che le evidenze non mostrano
ancora rimossi."* Resta `NOT_INVESTMENT_ADVICE`: segnali il gap di fiducia, non correggi il prezzo.

### 4b. GTM repeatable vs "founder heroics"
*La GTM motion si ripete senza l'eroismo del founder?* Distingui traction ottenuta da un
**sistema** (canale, sales motion, pricing ripetibili, CAC che regge) da traction ottenuta
dall'**eroismo del founder** (ogni deal chiuso perché ci va lui di persona, relazioni
personali, sforzo non scalabile). Domande al founder: chi ha chiuso gli ultimi deal? si
sarebbero chiusi senza il founder nella stanza? il CAC tiene senza l'effort founder? Più ampio
del solo caso fisico/retail: vale anche per SaaS/deeptech enterprise. Sticker
`GTM_FOUNDER_DEPENDENT`. Distinto da `CAPABILITY_PERSONA_DIPENDENTE` (lì dipende dalla persona
la *delivery*; qui l'*acquisizione clienti*).

### 4c. Legibilità del posizionamento
*Il posizionamento rende l'azienda più facile da capire, comprare e finanziare?* Un buyer che
capisce la startup in una frase è anche un investitore che la finanzia più facilmente. Test:
la spieghi in una riga senza gergo? il buyer sa in quale categoria e budget collocarla? Se
serve un paragrafo per dire cosa fa, segnala `POSITIONING_NON_LEGGIBILE`, spesso sintomo di use
case non a fuoco (collega a `USE_CASE_DEBOLE` / `TARGET_CONFUSO`). Non è marketing: la
non-legibilità è un rischio di adozione e di fundraising.

## 5. Come usarla nell'output

Nel risk memo, oltre agli archetipi e ai rischi IdeaLedger, aggiungi una riga sintetica:
**venture-scale? (sì/no/forse + perché)** e **quale delle 5 T è più debole**. Quando rilevante
aggiungi anche: **rischio residuo che la valuation presuppone rimosso**, **GTM = sistema o
founder-heroics?**, **posizionamento leggibile in una frase?**. Tienilo come inquadramento,
non come verdetto. Chiudi sempre con `NOT_INVESTMENT_ADVICE`.
