# Workflow — Intake to Candidate Brief

## Trigger

Use this workflow when starting with a new candidate or when the current Candidate Brief is missing, stale, or low confidence.

## Steps

1. Ask for candidate materials using the mandatory opening message in `SKILL.md`.
2. If materials are provided, ingest them and extract facts.
3. If no materials are provided, run interview-only intake.
4. Record notes in `candidate_workspace/00_intake_notes.md`.
5. Distinguish facts, assumptions, and missing data.
6. Ask targeted follow-up questions, maximum 5 at a time.
7. Create `candidate_workspace/01_candidate_brief.md`.
8. Assign confidence level.
9. If confidence is Low, do not start broad job search yet. Ask for missing evidence or preferences.
10. If confidence is Medium or High, proceed to `job_search_cycle.md`.
