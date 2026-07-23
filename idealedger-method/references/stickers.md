# IdeaLedger — Catalogo Sticker / Gate / Stati

Il metodo IdeaLedger ha una progressione logica, ma NON obbliga tutti i founder a partire dallo stesso punto: il **Gate 00** determina il punto di ingresso. Gate rigidi, ingresso flessibile.

Stickers are operational labels for maturity and state. Apply the honest one, not the
flattering one. Show the current sticker in the status header and in each file's header.

## Etichette di stato epistemico (per ogni claim)
`FATTO` · `IPOTESI` · `ASSUNZIONE` · `SUGGERIMENTO_AI` · `SEGNALE_DEBOLE` · `SEGNALE_FORTE`
· `EVIDENZA_VALIDATA`

## Evidence Ledger (per ogni segnale)
0 Ipotesi non testata · 1 Segnale debole · 2 Segnale comportamentale · 3 Workaround esistente
· 4 Costo gia' sostenuto · 5 Impegno concreto.
Regola: mai trattare un livello 1 come validazione.

## Sticker per fase e strumento

### Gate 00 — Intake & Diagnosi (trasversale, inizio sessione)
- `GATE_00_COMPLETATO` — intake fatto e diagnosi prodotta.
- `PUNTO_INGRESSO_FLESSIBILE` — l'ingresso non è il Tool 1 ma quello scelto dalla diagnosi.
- `DOCUMENTO_GIA_STRUTTURATO` — il founder arriva con doc/canvas/pitch già fatto.
- `DOCUMENT_AUDIT_NECESSARIO` — serve un audit del materiale esistente, non ripartire da zero.
- `CAMPIONE_DISTORTO` — discovery fatta su rete personale/amici/founder esperti/non target.
- `CUSTOMER_DISCOVERY_DA_RIFARE` — il campione non è rappresentativo: rifare su target reale.
- `COMPETITOR_AUDIT_ANTICIPATO` — Competition & Status Quo portato avanti rispetto alla fase 03.
- `METODO_TROPPO_RIGIDO` — il founder ha segnalato frizione/rigidità (dal feedback loop).
- `FEEDBACK_LOOP_ATTIVO` — eseguito il check di metà sessione sulla frizione.

### Fase 01 — Chiarisci e stressa l'idea
- Idea Stress Test: IDEA_GREZZA · IDEA_CHIARITA · ASSUNZIONE_CRITICA · DA_VALIDARE ·
  NON_COSTRUIRE_ANCORA
- Lean Canvas: LEAN_CANVAS_DRAFT · IPOTESI_DA_VALIDARE · MODELLO_PRELIMINARE

### Fase 02 — Valida il problema
- Customer Discovery: PROBLEMA_IPOTIZZATO · EVIDENZA_DEBOLE · EVIDENZA_FORTE · FALSO_POSITIVO
  · PROBLEMA_VALIDATO_PRELIMINARE · PROBLEMA_NON_VALIDATO
- PMF Readiness: PMF_NON_DIMOSTRATO · PMF_READINESS · SEGNALE_DEBOLE · SEGNALE_FORTE ·
  RETENTION_DA_MISURARE

### Fase 03 — Cliente, mercato, concorrenza
- Buyer Persona: ICP_PRELIMINARE · BUYER_DA_VERIFICARE · PERSONA_IPOTETICA ·
  PERSONA_EVIDENCE_BASED
- TAM/SAM/SOM: MERCATO_STIMATO · MERCATO_NON_VERIFICATO · SOM_OPERATIVO · DATI_MANCANTI
- Competition & Status Quo: STATUS_QUO_IDENTIFICATO · SWITCHING_COST_ALTO ·
  COMPETITOR_INDIRETTO · REAL_ENEMY

### Fase 04 — GTM e primi 10 clienti
- First 10 Customers: PRIMI_10_IDENTIFICATI · OUTREACH_PRONTO · LISTA_TROPPO_GENERICA
- Go-to-Market: GTM_IPOTESI · GTM_CANALE_PRIORITARIO · GTM_DA_TESTARE
- MVP 2 settimane: MVP_ESPERIMENTO · MVP_NON_PRODOTTO · MVP_DA_TAGLIARE · SEGNALE_DI_DOMANDA

### Fase 05 — Scala e raccogli capitali
- KPI: METRICHE_PRELIMINARI · KPI_DA_VALIDARE · VANITY_METRIC · KPI_EVIDENCE_BASED
- Unit Economics: UNIT_ECONOMICS_DA_VALIDARE · CAC_IPOTETICO · LTV_IPOTETICO ·
  MODELLO_NON_SCALABILE · UNIT_ECONOMICS_OK_PRELIMINARE
- Le Fasi: FASE_IDEA · PROBLEM_SOLUTION_FIT · PMF_READINESS · GTM_FIT · SCALE_NOT_READY ·
  ATTIVITA_PREMATURA
- Pitch Deck: PITCH_EARLY_DRAFT · PITCH_VALIDATION_BASED · INVESTOR_READY_DRAFT · STORY_GAP
- Fundraising: NON_READY_FOR_FUNDRAISING · PRE_SEED_READY_PRELIMINARE · ROUND_STORY_DRAFT ·
  INVESTOR_READY_DRAFT

### Artefatti finali
- Founder Plan: FOUNDER_PLAN_PRELIMINARE · FOUNDER_PLAN_VALIDATION_BASED ·
  FOUNDER_PLAN_INVESTOR_READY

### Trasversale
- ATTIVITA_PREMATURA — applicalo a qualsiasi richiesta fuori fase (es. pitch/fundraising
  prima della validazione del problema).

## Come funziona il gate
Ogni strumento ha un "gate di uscita" descritto in `tools.md`. Non avanzare di fase finche'
il gate non e' soddisfatto. Quando il gate e' superato, aggiorna lo sticker e il prossimo
gate nello status header.

## Status header (ogni turno)
```
Fase attuale:     <01-05 nome fase>
Strumento attivo: <nome strumento>
Sticker attuale:  <sticker corrente>
Prossimo gate:    <cosa serve per superare la fase>
```
