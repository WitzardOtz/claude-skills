# Workflow — Evaluate One Job

## Trigger

Use this workflow when the candidate provides one job description or link, or when a job is discovered during search.

## Steps

1. Read the current Candidate Brief.
2. Extract job facts:
   - title;
   - company;
   - location;
   - work mode;
   - seniority;
   - responsibilities;
   - required skills;
   - preferred skills;
   - compensation if available;
   - source and date.
3. Score the job using `references/scoring_rubric.md`.
4. Apply penalties for hard blockers.
5. Assign decision band.
6. Write evaluation in `candidate_workspace/03_job_evaluations.md`.
7. If the decision is Strong Apply, Apply, Network First, or Monitor, update `candidate_workspace/07_application_tracker.csv`.
8. If the candidate selects the role, proceed to the Application Pack workflow.
