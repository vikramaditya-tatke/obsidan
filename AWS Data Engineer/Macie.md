Macie is a fully-managed data security and privacy service that uses machine learning and pattern matching to discover, monitor and Protect Data stored in [[S3]] buckets.

- Can be made public but data leak risks if misconfigured.
- Discovery of data categorized as - PII, PHI, Finances, PGP Keys, NI numbers, Passport Numbers, Addresses, etc.
- Macie can be integrated with Security Hub and `finding events` can be sent to [[Event Bridge]] 

## Data identifiers

- **ML/Patterns _(built-in)_**: Sensitive Data Types from multiple countries. 
- **Regex Patterns _(custom)_**: Based on business requirements.

*Discovery Jobs* can be triggered in Macie that use these identifiers and look for matches in S3 buckets and generate findings. These findings an be viewed interactively or can be integrated with other AWS Services.

## Findings
- **Policy Findings**: Settings or policies on the S3 buckets or its objects are changed *after* enabling Macie on that S3 bucket.
- **Sensitive Data Findings**: 