# Ricerca web per colmare i dati mancanti

Quando manca un'informazione chiave, **prima di dichiarare `MATERIALE_INSUFFICIENTE`** tenta
di trovarla su fonti pubbliche con gli strumenti di ricerca disponibili. La ricerca completa,
non sostituisce, l'intake e le domande all'utente.

## Quando attivarla

Dopo aver fatto l'intake e chiesto all'utente quale materiale ha, per ogni **gap rimasto**
(es. anno di fondazione, team, round/funding, clienti, competitor, sede, traction). Non per
dati che l'utente può darti subito: quelli chiedili.

## Dove cercare (in ordine)

1. **Sito ufficiale della startup** — pagine About / Team / Product / Pricing / Customers /
   Press. È la fonte primaria pubblica.
2. **Stampa e ecosistema** — testate di settore, comunicati, articoli sui round.
3. **Registri e profili pubblici** — LinkedIn (azienda e founder), database startup, registro
   imprese se disponibile.
4. **Dataset Scalable** (`api_client.py`) — per comparabili/benchmark di settore, non per i
   fatti specifici della singola startup.

## Come usare gli strumenti

Usa la ricerca web e il fetch di pagine se l'assistente li ha (`WebSearch`, fetch del dominio
ufficiale). Se non hai strumenti di ricerca disponibili, **non inventare**: dichiara il gap e
indica all'utente cosa cercare.

## Regole non negoziabili

1. **Solo informazioni pubbliche.** Cerca per nome startup, dominio, founder. **Non inviare
   MAI ai motori di ricerca il materiale riservato dell'utente** (pitch, numeri privati,
   documenti). La promessa "non carico i tuoi dati" resta vera: si cerca solo ciò che è già
   pubblico.
2. **Etichetta la provenienza.** Ogni dato trovato online è `DA_VERIFICARE` (Evidence Ledger
   basso) con la **fonte tra parentesi (URL/testata)**. Mai presentarlo come `FATTO`.
3. **Distingui le fonti.** Sito ufficiale = dichiarazione dell'azienda (di parte); stampa =
   secondaria; dataset Scalable = comparabili. Pesa di conseguenza.
4. **Niente certezze finte.** Se i dati pubblici sono incoerenti o assenti, dillo: è di per sé
   un finding (e una domanda per il founder).
5. **La ricerca non scavalca l'intake né l'hard gate.** Prima chiedi all'utente, poi cerchi i
   buchi; e comunque non produci il deliverable finale senza aver chiuso il punto sul materiale.

## Output

Nei deliverable, separa chiaramente: *dati forniti dall'utente* · *dati trovati online
(DA_VERIFICARE + fonte)* · *comparabili Scalable* · *tue ipotesi/giudizi*. Così chi legge sa
sempre quanto è solida ogni affermazione.
