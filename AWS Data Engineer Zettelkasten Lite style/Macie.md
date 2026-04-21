---
services:
  - Amazon Macie
  - Amazon S3
tags: [aws, macie, security, s3]
status: atomic
topic: AWS Data Engineering
domain: Exam Prep
created_at: 2025-12-24
---
###  Active Recall
- What types of sensitive data can Macie identify automatically?
- Does Macie monitor changes to S3 bucket policies?

---

Macie is a fully-managed data security and privacy service that uses machine learning and pattern matching to discover, monitor and Protect Data stored in [[Amazon S3 Fundamentals|S3]] buckets.

- Can be made public but data leak risks if misconfigured.
- Discovery of data categorized as - PII, PHI, Finances, PGP Keys, NI numbers, Passport Numbers, Addresses, etc.
- Macie can be integrated with Security Hub and `finding events` can be sent to [[Event Bridge]]

## Data Identifiers

- **ML/Patterns _(built-in)_**: Sensitive Data Types from multiple countries.
- **Regex Patterns _(custom)_**: Based on business requirements.

_Discovery Jobs_ can be triggered in Macie that use these identifiers and look for matches in [[Amazon S3 Fundamentals|S3]] buckets and generate findings. These findings an be viewed interactively or can be integrated with other [[AWS Services]].

## Findings
- **Policy Findings**: Settings or policies on the [[Amazon S3 Fundamentals|S3]] buckets or its objects are changed _after_ enabling Macie on that [[Amazon S3 Fundamentals|S3]] bucket.
- **Sensitive Data Findings**:
