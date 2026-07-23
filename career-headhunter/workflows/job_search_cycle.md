# Workflow — Job Search Cycle

## Trigger

Use this workflow when the candidate asks to find suitable roles.

## Precondition

`candidate_workspace/01_candidate_brief.md` must exist and have Medium or High confidence.

## Steps

1. Read the Candidate Brief.
2. Create or refresh `candidate_workspace/02_search_strategy.md`.
3. Generate primary, adjacent, and stretch queries.
4. Search permitted sources or process user-provided links.
5. Record all sources in `candidate_workspace/09_source_log.md`.
6. Deduplicate jobs.
7. Filter obvious low-fit roles.
8. Evaluate promising roles using `evaluate_job.md`.
9. Save detailed evaluations in `candidate_workspace/03_job_evaluations.md`.
10. Build a shortlist of up to 10 roles in `candidate_workspace/04_job_shortlist.md`.
11. Update `candidate_workspace/07_application_tracker.csv` for roles marked Strong Apply, Apply, Network First, or Monitor.
12. Ask for feedback and update `candidate_workspace/06_feedback_loop.md` and `candidate_workspace/08_learning_log.md`.
