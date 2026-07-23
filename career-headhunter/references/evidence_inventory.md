# Evidence Inventory — active document hunt (run during intake)

Purpose: candidates almost always own more evidence than they remember. Do not ask the
generic "do you have any material?" — walk them through the categories below, one block at
a time, with memory triggers about WHERE such documents usually live (old email, HR portal,
OneDrive/Drive, LinkedIn message archive, folder "Documenti/Lavoro", the drawer with the
old employment contract).

Rules:
- Ask category by category, max 2 categories per message. Wait for the answer.
- Silence is not absence: an unanswered category stays OPEN and gets re-asked once,
  explicitly ("Sulla categoria assessment non mi hai risposto: ne hai mai fatti?").
- For every "yes, somewhere": ask the candidate to go find it before the search phase —
  concrete evidence beats memory. Offer to proceed while they retrieve it, and mark the
  Candidate Brief item as PENDING_DOCUMENT.
- Record every category in `00_intake_notes.md` as: Provided / Exists-but-not-retrieved /
  Doesn't exist / Not answered.

## 1. Identity & baseline
CV (all versions, also old ones — useful for chronology), LinkedIn (profile URL + do they
have exported data?), personal site, portfolio, GitHub/Scholar/Behance.

## 2. Structured assessments & feedback  ← most often forgotten, highest signal
Ask explicitly, with examples by name:
- Assessment manageriali o di leadership (assessment center, development center)
- 360° feedback report
- Test psicometrici o di personalità: Hogan, SHL, Korn Ferry, DISC, MBTI, Insights
  Discovery, Gallup StrengthsFinder/CliftonStrengths, Predictive Index, OPQ
- Performance review / valutazioni annuali (anche solo le ultime 2-3)
- Piani di sviluppo individuali (IDP), esiti di talent review o succession planning
  se noti ("sei mai stato indicato come high potential?")
- Feedback scritti di fine progetto / fine mandato
Memory triggers: "Hai mai partecipato a un percorso di leadership o a un assessment per
una promozione? L'HR di [azienda] usava una piattaforma di performance management? Hai
mai ricevuto un report PDF dopo un questionario di personalità?"

## 3. Measurable results
Bonus/MBO letters (objectives + achievement %), KPI dashboards or business reviews they
presented, business cases won, budget/P&L figures, org charts showing team size and scope,
award/recognition emails.

## 4. Education & credentials
Degrees, certifications (with expiry), executive education, relevant courses.

## 5. Market signals
Job descriptions they liked, JDs where they were rejected (+ any rejection feedback),
recruiter messages received (LinkedIn archive!), past offers (role + compensation),
interview feedback notes.

## 6. Reputation
Reference letters, written endorsements, talks/panels, articles/publications, press
mentions, internal awards.

## 7. Constraints & context
Current contract (notice period, non-compete!), current total compensation structure,
geographic/travel constraints, family constraints affecting relocation.

## Late-arriving material (delta update)
When the candidate provides new material AFTER the Candidate Brief exists (e.g. finds an
old assessment): do NOT rebuild from scratch. Produce a short delta — what the new evidence
adds, confirms, or contradicts; which scores/role families it changes; new open questions —
then update `01_candidate_brief.md` (Evidence Base + affected sections) and log the event
in `08_learning_log.md`. Assessment reports upgrade "managerial skills" claims from
self-reported to third-party evidence: reflect that in the confidence level.
