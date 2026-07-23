# IdeaLedger — Playbook dei 15 strumenti

Read the relevant section before running a tool. Each tool lists: fase, quando usarlo,
obiettivo, input richiesti, domande guida (one at a time, behavior-first, never leading),
output markdown locale, sticker possibili, gate di uscita, errori da evitare, risorse.
Always label each item's epistemic status (FATTO / IPOTESI / ASSUNZIONE / SUGGERIMENTO_AI /
SEGNALE_DEBOLE / SEGNALE_FORTE / EVIDENZA_VALIDATA) and Evidence Ledger level (0-5).

Central question, always: **"Sto risolvendo un problema reale?"**

---

## Strumento 1 — Idea Stress Test
- **Fase:** 01 Chiarisci e stressa l'idea
- **Quando usarlo:** all'inizio, prima di investire mesi in prodotto, pitch o fundraising.
- **Obiettivo:** individuare le assunzioni piu' fragili dell'idea.
- **Domanda chiave:** "Cosa deve essere vero perche' questa startup funzioni, che oggi non
  so se e' vero?"
- **Input richiesti:** idea in forma grezza, target ipotizzato, problema percepito.
- **Domande guida:**
  - Puoi nominare 5 persone reali che hanno questo problema oggi?
  - Perche' questo problema non e' gia' stato risolto bene?
  - Perche' adesso e non tre anni fa?
  - Come raggiungeresti i primi 100 clienti senza paid acquisition?
  - Perche' tu sei la persona giusta per risolvere questo problema?
- **Output:** `01_idea_stress_test.md` — idea in una frase; problema ipotizzato; target
  ipotizzato; soluzione immaginata; 10 assunzioni critiche; 3 assunzioni piu' rischiose;
  perche' sono rischiose; evidenze disponibili; cosa verificare prima; cosa non costruire
  ancora.
- **Sticker:** IDEA_GREZZA · IDEA_CHIARITA · ASSUNZIONE_CRITICA · DA_VALIDARE ·
  NON_COSTRUIRE_ANCORA
- **Gate di uscita:** il founder conosce le 3 assunzioni piu' rischiose e sa cosa verificare
  prima di costruire.
- **Errori da evitare:** confondere "interessante" con "vero"; elencare assunzioni generiche;
  saltare alla soluzione; non nominare persone reali.
- **Risorse:** https://www.scalablepod.it/learn/idea-stress-test/

---

## Strumento 2 — Lean Canvas
- **Fase:** 01 Chiarisci e stressa l'idea
- **Quando usarlo:** subito dopo lo stress test, per mappare l'idea come ipotesi di business.
- **Obiettivo:** trasformare l'idea in una mappa sintetica delle ipotesi. Ricorda: il Lean
  Canvas e' una mappa di ipotesi, non una verita'.
- **Input richiesti:** problema, segmento, idea di soluzione.
- **Domande guida:**
  - Il problema e' formulato in modo specifico?
  - Il segmento cliente e' troppo ampio?
  - La UVP e' concreta o solo marketing?
  - Il canale e' specifico o generico?
  - Chi paga, quanto e quando?
- **Output:** `02_lean_canvas.md` con i 9 blocchi: Problem · Customer Segments · Unique Value
  Proposition · Solution · Channels · Revenue Streams · Cost Structure · Key Metrics ·
  Unfair Advantage. **Ogni blocco deve avere uno status:** ipotesi / da validare /
  parzialmente verificato / evidenza raccolta.
- **Sticker:** LEAN_CANVAS_DRAFT · IPOTESI_DA_VALIDARE · MODELLO_PRELIMINARE
- **Gate di uscita:** il canvas mostra chiaramente quali parti del modello sono ipotesi e
  quali richiedono validazione.
- **Errori da evitare:** trattare il canvas come piano definitivo; segmento troppo ampio;
  UVP da brochure; nessuno status sui blocchi.
- **Risorse:** https://www.scalablepod.it/learn/lean-canvas/ · Running Lean
  (https://www.oreilly.com/library/view/running-lean-3rd/9781098114831/) · LEANFoundry
  (https://www.leanfoundry.com/tools/lean-canvas) · Ash Maurya "Fire the Business Plan"
  (https://medium.leanstack.com/its-time-to-fire-the-business-plan-for-good-df165fcc78f6) ·
  Miro template (https://miro.com/it/modelli/lean-canvas/) · BM Toolbox
  (https://bmtoolbox.net/tools/lean-canvas/)

---

## Strumento 3 — Customer Discovery
- **Fase:** 02 Valida il problema
- **Quando usarlo:** per verificare il problema con comportamenti reali, prima di costruire.
- **Obiettivo:** preparare interviste che producano verita' operative, non complimenti.
- **Input richiesti:** problema ipotizzato, profili candidati da intervistare.
- **Domande corrette (comportamentali):**
  - Raccontami l'ultima volta in cui hai avuto questo problema.
  - Come lo hai risolto?
  - Quanto tempo o denaro ti e' costato?
  - Chi era coinvolto?
  - Che strumenti hai usato?
  - Hai gia' pagato per risolverlo?
  - Cosa succede se non lo risolvi?
- **Domande da evitare (leading):** Useresti questa app? · Ti piacerebbe questa soluzione? ·
  Pagheresti per questa idea?
- **Output:** `03_customer_discovery.md` (obiettivo interviste; profili da intervistare;
  domande non-leading; domande vietate; segnali forti; falsi positivi; template di risposta;
  piano minimo di 5-10 conversazioni) **e** `evidence/interviews.md` (una voce per
  conversazione reale, con livello Evidence Ledger).
- **Sticker:** PROBLEMA_IPOTIZZATO · EVIDENZA_DEBOLE · EVIDENZA_FORTE · FALSO_POSITIVO ·
  PROBLEMA_VALIDATO_PRELIMINARE · PROBLEMA_NON_VALIDATO
- **Gate di uscita:** il founder ha raccolto o pianificato conversazioni utili a verificare
  comportamenti reali, non opinioni.
- **Errori da evitare:** domande leading; intervistare amici compiacenti; contare i
  complimenti come validazione; pitchare invece di ascoltare.
- **Risorse:** https://www.scalablepod.it/learn/customer-discovery/ · The Mom Test
  (https://www.momtestbook.com/)

---

## Strumento 4 — Product-Market Fit / PMF Readiness
- **Fase:** 02 Valida il problema
- **Quando usarlo:** per definire QUALI segnali serviranno a capire se il mercato tira il
  prodotto. **Non dichiarare mai PMF in fase idea.** Usalo come PMF Readiness e PMF Evidence
  Ladder, mai come dichiarazione.
- **Obiettivo:** diagnosi dei segnali futuri; capire cosa non basta.
- **Input richiesti:** stato attuale dell'idea, eventuali primi segnali.
- **PMF Evidence Ladder:** 1. Interesse · 2. Attivazione · 3. Retention · 4. PMF
- **Segnali forti:** uso ripetuto; retention; pagamento; referral spontaneo; richiesta di
  continuare il test; cliente che soffre se il prodotto sparisce.
- **Output:** `04_pmf_readiness.md` — livello attuale sulla PMF Evidence Ladder; segnali
  disponibili; segnali mancanti; retention attesa; willingness to pay da verificare; criteri
  futuri di PMF; falsi positivi.
- **Sticker:** PMF_NON_DIMOSTRATO · PMF_READINESS · SEGNALE_DEBOLE · SEGNALE_FORTE ·
  RETENTION_DA_MISURARE
- **Gate di uscita:** il founder sa quali segnali cercare e quali metriche non bastano.
- **Errori da evitare:** dichiarare PMF senza dati di retention/pagamento/referral; scambiare
  interesse per attivazione; vanity signals.
- **Risorse:** https://www.scalablepod.it/learn/product-market-fit/ · The Lean Startup
  (https://theleanstartup.com/) · The Mom Test (https://www.momtestbook.com/) · Andreessen
  "The only thing that matters" (https://pmarchive.com/guide_to_startups_part4.html) ·
  PMFsurvey (https://pmfsurvey.com/) · Strategyzer Test Card
  (https://strategyzr.s3.amazonaws.com/assets/vpd/resources/the-test-card.pdf)

---

## Strumento 5 — Buyer Persona
- **Fase:** 03 Definisci cliente, mercato e concorrenza
- **Quando usarlo:** dopo i primi segnali di problema, per rendere il target operativo.
- **Obiettivo:** trasformare un target generico in una persona operativa e decisionale.
- **Modalità beachhead selection:** se il founder arriva con un target ampio/multi-segmento e il problema non è ancora validato, usa prima questo strumento per **scegliere il primo segmento** (2-4 candidati → scegli per urgenza, frequenza, accessibilità), così la validazione del problema diventa possibile. Non produrre una persona decorativa: serve a decidere PER CHI validare.
- **Input richiesti:** interviste o ipotesi esplicitamente marcate come tali.
- **Domande guida:** Chi usa davvero? Chi paga? Chi decide il budget? Chi puo' bloccare
  l'acquisto? Qual e' il trigger d'acquisto? Quali obiezioni ricorrono?
- **Output:** `05_buyer_persona.md` — persona primaria; user; buyer; economic decision maker;
  influencer; blocker; trigger d'acquisto; obiezioni; canali; frase tipica; segnali di early
  adopter; cosa resta da verificare. **La persona deve essere basata su interviste o ipotesi
  esplicitamente marcate.**
- **Sticker:** ICP_PRELIMINARE · BUYER_DA_VERIFICARE · PERSONA_IPOTETICA ·
  PERSONA_EVIDENCE_BASED
- **Gate di uscita:** il founder distingue chi usa, chi paga, chi decide e chi puo' bloccare.
- **Errori da evitare:** persona inventata spacciata per dato; confondere user e buyer;
  ignorare il blocker.
- **Risorse:** https://www.scalablepod.it/learn/buyer-persona/ · Buyer Personas book
  (https://buyerpersona.com/buyer-personas-book) · NN/g
  (https://www.nngroup.com/articles/persona/) · Buyer Persona Institute
  (https://buyerpersona.com/what-is-a-buyer-persona) · HubSpot Make My Persona
  (https://www.hubspot.com/make-my-persona)

---

## Strumento 6 — TAM / SAM / SOM
- **Fase:** 03 Definisci cliente, mercato e concorrenza
- **Quando usarlo:** per dimensionare il mercato senza gonfiare numeri.
- **Obiettivo:** distinguere mercato teorico, servibile e realisticamente conquistabile.
- **Input richiesti:** segmento, prezzo ipotizzato, fonti dati (se assenti, NON inventare).
- **Domande guida:** Da quali fonti vengono questi numeri? Qual e' il beachhead market? Il
  SOM e' raggiungibile con i canali che hai? Quali assunzioni numeriche stai facendo?
- **Output:** `06_tam_sam_som.md` — TAM; SAM; SOM; approccio top-down; approccio bottom-up;
  fonti necessarie; assunzioni numeriche; rischi di sovrastima; beachhead market; piano per
  rendere il SOM operativo.
- **Regola:** se non ci sono dati, non inventare numeri. Chiedi fonti o formula un piano di
  ricerca.
- **Sticker:** MERCATO_STIMATO · MERCATO_NON_VERIFICATO · SOM_OPERATIVO · DATI_MANCANTI
- **Gate di uscita:** il founder distingue mercato teorico, servibile e conquistabile.
- **Errori da evitare:** TAM gonfiato top-down senza bottom-up; numeri senza fonte; nessun
  beachhead.
- **Risorse:** https://www.scalablepod.it/learn/tam-sam-som/ · Disciplined Entrepreneurship
  (https://www.d-eship.com/) · Crossing the Chasm
  (https://www.harpercollins.com/products/crossing-the-chasm-geoffrey-a-moore) · For
  Entrepreneurs TAM (https://www.forentrepreneurs.com/calculating-tam/) · Miro Market Sizing
  (https://miro.com/templates/market-sizing-for-startups-template/) · HubSpot Market Size
  (https://blog.hubspot.com/marketing/market-size)

---

## Strumento 7 — Competition & Status Quo
- **Fase:** 03 Definisci cliente, mercato e concorrenza
- **Quando usarlo:** per capire contro cosa compete davvero la startup.
- **Obiettivo:** mappare competitor diretti, alternative indirette, workaround, inerzia e
  status quo. **Se il founder dice "non abbiamo concorrenti", fermalo e mappa lo status quo.**
- **Input richiesti:** cosa fa oggi il cliente per risolvere il problema.
- **Domande guida:** Cosa usa il cliente oggi al posto tuo? Quanto gli costa cambiare? Chi e'
  il "real enemy" (abitudine, foglio Excel, inerzia)? Perche' dovrebbe cambiare adesso?
- **Output:** `07_competition_status_quo.md` — competitor diretti; competitor indiretti;
  workaround; strumenti usati oggi; status quo; real enemy; switching cost; costo reale del
  cambiamento; perche' il cliente dovrebbe cambiare.
- **Sticker:** STATUS_QUO_IDENTIFICATO · SWITCHING_COST_ALTO · COMPETITOR_INDIRETTO ·
  REAL_ENEMY
- **Gate di uscita:** il founder sa dire cosa il cliente fa oggi senza la nuova soluzione.
- **Errori da evitare:** "non abbiamo concorrenti"; ignorare i workaround; sottovalutare lo
  switching cost.
- **Risorse:** https://www.scalablepod.it/learn/competition-status-quo/

---

## Strumento 8 — First 10 Customers
- **Fase:** 04 GTM e trova i primi 10 clienti
- **Quando usarlo:** per passare da target astratto a persone/aziende reali da contattare.
- **Obiettivo:** 10 soggetti specifici e nominabili, non un target teorico.
- **Input richiesti:** segmento, rete del founder, canali di accesso.
- **Domande guida:** Chi conosci che potrebbe avere questo problema? Per ciascuno: ruolo,
  perche' avrebbe il problema, canale di contatto, relazione con te.
- **Output:** `08_first_10_customers.md` — lista di 10 contatti reali o aziende specifiche;
  ruolo; perche' potrebbero avere il problema; canale di contatto; relazione con founder;
  messaggio; obiettivo della conversazione; stato.
- **Regola:** chiedi una conversazione, non una vendita.
- **Sticker:** PRIMI_10_IDENTIFICATI · OUTREACH_PRONTO · LISTA_TROPPO_GENERICA
- **Gate di uscita:** il founder ha 10 soggetti specifici, non un target teorico.
- **Errori da evitare:** lista generica ("PMI italiane"); messaggio di vendita anziche' di
  scoperta; nessun canale di contatto.
- **Risorse:** https://www.scalablepod.it/learn/first-10-customers/

---

## Strumento 9 — Go-to-Market Strategy
- **Fase:** 04 GTM e trova i primi 10 clienti
- **Quando usarlo:** per definire come raggiungere, convincere e convertire il primo segmento.
- **Obiettivo:** un canale prioritario, una sales motion, un esperimento GTM concreto.
- **Input richiesti:** segmento prioritario, buyer persona, primi 10 clienti.
- **Domande guida:** Qual e' il canale piu' diretto al buyer? La sales motion e' self-serve,
  inbound o sales-led? Qual e' l'offerta iniziale? Quali proof points hai? Qual e' il primo
  esperimento GTM?
- **Output:** `09_go_to_market.md` — segmento prioritario; canale iniziale; sales motion;
  messaggio; offerta iniziale; proof points; esperimenti; metriche GTM; rischi; prossime
  azioni.
- **Regola:** non confondere "fare marketing" con avere una strategia GTM.
- **Sticker:** GTM_IPOTESI · GTM_CANALE_PRIORITARIO · GTM_DA_TESTARE
- **Gate di uscita:** il founder ha un canale prioritario, una sales motion e un esperimento
  GTM concreto.
- **Errori da evitare:** spruzzare su tutti i canali; messaggio generico; nessuna metrica.
- **Risorse:** https://www.scalablepod.it/learn/go-to-market/ · Crossing the Chasm
  (https://geoffreyamoore.com/book/crossing-the-chasm/) · Disciplined Entrepreneurship
  (https://www.wiley.com/en-us/Disciplined%2BEntrepreneurship%2BSeries-c-5235) · HubSpot GTM
  (https://blog.hubspot.com/sales/gtm-strategy) · Miro GTM
  (https://miro.com/templates/go-to-market-strategy/) · Value Proposition Canvas
  (https://www.strategyzer.com/library/the-value-proposition-canvas)

---

## Strumento 10 — MVP in 2 Settimane
- **Fase:** 04 GTM e trova i primi 10 clienti
- **Quando usarlo:** per testare l'assunzione piu' critica in massimo due settimane.
- **Obiettivo:** definire un MVP come esperimento di apprendimento, non come mini-prodotto
  completo.
- **Domanda chiave:** "Se questa assunzione e' falsa, continuerei a costruire questo prodotto
  in questo modo?"
- **Tipi MVP:** concierge MVP · landing page · fake door · demo clickable · prototipo no-code
  · servizio manuale · pilot controllato.
- **Input richiesti:** l'assunzione critica da testare, gli utenti coinvolti.
- **Domande guida:** Qual e' l'UNICA assunzione che questo MVP testa? Qual e' la metrica
  primaria? Qual e' la soglia di successo? Cosa NON costruisci?
- **Output:** `10_mvp_2_weeks.md` — assunzione da testare; tipo di MVP; cosa costruire; cosa
  non costruire; utenti coinvolti; metrica primaria; soglia di successo; durata; decisione
  successiva.
- **Sticker:** MVP_ESPERIMENTO · MVP_NON_PRODOTTO · MVP_DA_TAGLIARE · SEGNALE_DI_DOMANDA
- **Gate di uscita:** l'MVP testa una sola assunzione critica in massimo due settimane.
- **Errori da evitare:** MVP che e' un mini-prodotto completo; testare 5 assunzioni insieme;
  nessuna soglia di successo decisa prima.
- **Risorse:** https://www.scalablepod.it/learn/mvp-2-settimane/

---

## Strumento 11 — KPI per Startup
- **Fase:** 05 Scala e raccogli capitali
- **Quando usarlo:** per scegliere metriche che descrivano il rischio principale della fase.
- **Obiettivo:** 3-5 metriche che contano, evitando vanity metrics.
- **Input richiesti:** fase attuale (vedi strumento 13), modello di business.
- **Domande guida:** Qual e' il rischio numero uno di questa fase? Quale singola metrica lo
  cattura (North Star)? Quali metriche stai guardando solo perche' fanno sentire bene?
- **Output:** `11_kpi_startup.md` — fase attuale; North Star Metric; 3-5 KPI principali;
  vanity metrics da ignorare; frequenza di misurazione; soglie decisionali; Evidence Score
  per ogni KPI.
- **Evidence Score:** 0 = ipotesi non testata · 1 = segnale debole · 2 = segnale forte ·
  3 = validato con dati reali.
- **Sticker:** METRICHE_PRELIMINARI · KPI_DA_VALIDARE · VANITY_METRIC · KPI_EVIDENCE_BASED
- **Gate di uscita:** il founder sa quali 3-5 metriche guardare e quali ignorare.
- **Errori da evitare:** vanity metrics (download, follower); troppe metriche; nessuna soglia
  decisionale.
- **Risorse:** https://www.scalablepod.it/learn/kpi-startup/ · Lean Analytics
  (https://leananalyticsbook.com/) · YC Key Metrics
  (https://www.ycombinator.com/library/KR-key-startup-metrics) · Amplitude North Star
  (https://amplitude.com/north-star-hub) · HubSpot KPI Dashboard
  (https://www.hubspot.com/resources/templates/kpi-dashboard) · Miro KPI Tree
  (https://miro.com/templates/kpi-tree/)

---

## Strumento 12 — Unit Economics
- **Fase:** 05 Scala e raccogli capitali
- **Quando usarlo:** per capire se il modello crea o distrugge valore quando cresce.
- **Obiettivo:** verificare se la crescita puo' diventare sostenibile o amplifica perdite.
- **Input richiesti:** pricing, costi variabili, dati su acquisizione e retention (se assenti,
  marca tutto come ipotesi).
- **Domande guida:** Qual e' l'unita' economica corretta? Quanto costa acquisire un cliente?
  Quanto vale nel tempo? In quanto tempo recuperi il CAC? Qual e' il churn?
- **Output:** `12_unit_economics.md` — unita' economica corretta; pricing; ricavi per unita';
  costi variabili; contribution margin; CAC; LTV; LTV/CAC; payback period; churn; assunzioni
  aperte.
- **Regola:** se mancano dati reali, marca tutto come ipotesi e non come risultato.
- **Sticker:** UNIT_ECONOMICS_DA_VALIDARE · CAC_IPOTETICO · LTV_IPOTETICO ·
  MODELLO_NON_SCALABILE · UNIT_ECONOMICS_OK_PRELIMINARE
- **Gate di uscita:** il founder capisce se la crescita puo' essere sostenibile o sta solo
  amplificando perdite.
- **Errori da evitare:** spacciare CAC/LTV ipotetici per risultati; ignorare il churn; LTV
  gonfiato.
- **Risorse:** https://www.scalablepod.it/learn/unit-economics/ · Disciplined Entrepreneurship
  (https://www.wiley.com/en-ca/Disciplined%20Entrepreneurship%3A%2024%20Steps%20to%20a%20Successful%20Startup%2C%20Expanded%20%26%20Updated%2C%202nd%20Edition-p-9781394222513)
  · For Entrepreneurs LTV:CAC (https://www.forentrepreneurs.com/ltv-cac/) · Stripe CAC
  Payback (https://stripe.com/resources/more/what-is-the-cac-payback-period) · YC Consumer
  Metrics (https://www.ycombinator.com/library/KT-consumer-startup-metrics) · Founderpath CAC
  (https://founderpath.com/free-tools/cac-calculator)

---

## Strumento 13 — Le Fasi di una Startup (trasversale)
- **Fase:** 05 Scala e raccogli capitali, ma trasversale a tutto il metodo.
- **Quando usarlo:** in qualsiasi momento per capire in quale fase si trova davvero la startup
  e quali attivita' sono premature.
- **Obiettivo:** allineare le attivita' alla fase reale; bloccare quelle premature.
- **Fasi logiche:** idea · problem/solution fit · product/market fit · GTM fit · scale.
- **Domande guida:** Qual e' il rischio prevalente adesso? Quali evidenze ho davvero? Quale
  attivita' sto facendo che sarebbe da rimandare?
- **Output:** `13_startup_stage.md` — fase attuale; livello di rischio prevalente; evidenze
  disponibili; cosa fare ora; cosa non fare ancora; strumenti IdeaLedger consigliati;
  attivita' premature.
- **Sticker:** FASE_IDEA · PROBLEM_SOLUTION_FIT · PMF_READINESS · GTM_FIT · SCALE_NOT_READY ·
  ATTIVITA_PREMATURA
- **Gate di uscita:** il founder sa qual e' il prossimo passo giusto e cosa deve evitare.
- **Errori da evitare:** comportarsi da fase scale in fase idea; fundraising prima del
  problem/solution fit.
- **Risorse:** https://www.scalablepod.it/learn/fasi-startup/ · The Lean Startup
  (https://theleanstartup.com/book) · Startup School (https://www.startupschool.org/) · YC
  Stages (https://www.ycombinator.com/library/Ek-stages-of-startups) · Steve Blank Tools
  (https://steveblank.com/tools-and-blogs-for-entrepreneurs/) · Business Model Canvas
  (https://www.strategyzer.com/library/the-business-model-canvas)

---

## Strumento 14 — Pitch Deck
- **Fase:** 05 Scala e raccogli capitali
- **Quando usarlo:** solo dopo che c'e' qualcosa di validato da raccontare.
- **Obiettivo:** trasformare cio' che e' stato validato in una narrativa chiara.
- **Input richiesti:** evidenze raccolte, traction, mercato, team.
- **Domande guida:** Qual e' l'one-liner? Qual e' la traction reale (non vanity)? Perche'
  questo team, su questo problema, adesso?
- **Output:** `14_pitch_deck.md` — one-liner; problema; soluzione; perche' ora; mercato;
  prodotto; traction; business model; GTM; concorrenza; team; round ask / next milestone.
- **Regola:** se il problema non e' validato, il deck e' PITCH_EARLY_DRAFT, non
  investor-ready.
- **Sticker:** PITCH_EARLY_DRAFT · PITCH_VALIDATION_BASED · INVESTOR_READY_DRAFT · STORY_GAP
- **Gate di uscita:** il pitch risponde a: perche' questo team, su questo problema, adesso?
- **Errori da evitare:** deck senza evidenze; traction = vanity metrics; saltare qui prima di
  validare il problema (ATTIVITA_PREMATURA).
- **Risorse:** https://www.scalablepod.it/learn/pitch-deck/ · The Art of the Start 2.0
  (https://www.penguinrandomhouse.com/books/318082/the-art-of-the-start-20-by-guy-kawasaki/)
  · Sequoia Business Plan (https://sequoiacap.com/article/writing-a-business-plan/) · YC Seed
  Deck (https://www.ycombinator.com/library/2u-how-to-build-your-seed-round-pitch-deck) ·
  DocSend (https://www.docsend.com/startup-fundraising/) · Canva
  (https://www.canva.com/presentations/templates/pitch-deck/)

---

## Strumento 15 — Fundraising
- **Fase:** 05 Scala e raccogli capitali
- **Quando usarlo:** per capire se la startup e' pronta a raccogliere capitale e per quale
  milestone.
- **Obiettivo:** decidere se raccogliere ora, aspettare o chiudere prima gap di validazione.
- **Input richiesti:** rischi rimossi/aperti, runway, milestone, segnali.
- **Domande guida:** Quale rischio hai gia' rimosso con evidenze? Quale milestone finanzia
  questo round? Cosa manca prima di essere credibile con un investitore?
- **Output:** `15_fundraising.md` — fundraising readiness; rischio gia' rimosso; rischio
  ancora aperto; round size ipotizzato; runway; milestone finanziata; uso dei fondi;
  investitori target per tipologia; materiali necessari; gap da chiudere prima del round.
- **Regola:** il fundraising non compensa l'assenza di validazione. Serve ad accelerare
  qualcosa che ha gia' segnali.
- **Sticker:** NON_READY_FOR_FUNDRAISING · PRE_SEED_READY_PRELIMINARE · ROUND_STORY_DRAFT ·
  INVESTOR_READY_DRAFT
- **Gate di uscita:** il founder sa se raccogliere ora, aspettare o chiudere prima i gap di
  validazione.
- **Errori da evitare:** raccogliere per "comprare validazione"; round size senza milestone;
  investitori non profilati.
- **Risorse:** https://www.scalablepod.it/learn/fundraising/ · Venture Deals
  (https://onlinelibrary.wiley.com/doi/book/10.1002/9781119259794) · Sequoia Business Plan
  (https://sequoiacap.com/article/writing-a-business-plan/) · YC SAFE
  (https://www.ycombinator.com/documents) · Carta Fundraising 101
  (https://carta.com/learn/startup-fundraising-101/) · OpenVC (https://www.openvc.app/)

---

# Artefatti finali

Produce these only when the method has been worked through enough. Reflect the real Evidence
Ledger state — never inflate.

## final/validation_report.md
Contenuti: problema validato? · per chi? · con quali evidenze (con livello Evidence Ledger)? ·
quali segnali sono deboli? · quali assunzioni restano aperte? · cosa non costruire ancora? ·
prossimo test consigliato.

## final/founder_plan.md  (preferisci il nome "Founder Plan")
Il business plan moderno del metodo. Contenuti: executive summary · problema · cliente target
· soluzione · evidenze · mercato · concorrenza/status quo · business model · GTM iniziale ·
MVP · KPI · unit economics preliminari · rischi · assunzioni aperte · piano operativo 90
giorni · eventuale fundraising need.
Sticker: FOUNDER_PLAN_PRELIMINARE / FOUNDER_PLAN_VALIDATION_BASED / FOUNDER_PLAN_INVESTOR_READY.
Se il problema non e' validato, resta FOUNDER_PLAN_PRELIMINARE.

## final/next_actions.md
Contenuti: prossime 5 azioni · ordine · tempo stimato · output atteso · rischio che riduce.
