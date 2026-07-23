# Search Query Playbook

Generate queries from the Candidate Brief. Use synonyms and exclusions.

## Query Pattern

```text
("TITLE 1" OR "TITLE 2" OR "TITLE 3") AND (sector OR adjacent_sector) AND (location OR remote OR hybrid)
```

## Seniority Variants

- Manager
- Senior Manager
- Lead
- Head of
- Director
- VP
- Principal
- Chief of Staff
- COO

## Work Mode Variants

- remote
- hybrid
- distributed
- EMEA remote
- Europe remote
- flexible working

## Source-Specific Patterns

### Company career pages

```text
site:company.com/careers "target title" "location"
```

### Broad search

```text
"target title" "remote" "Europe" "careers"
```

### Recruiter posts

```text
"target title" "hiring" "remote" "recruiter"
```

### Negative filters

Use negative keywords to reduce noise:

```text
-intern -junior -graduate -sales -developer -engineer
```

Only use exclusions that are consistent with the Candidate Brief.
