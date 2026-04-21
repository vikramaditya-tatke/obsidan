---
services:
  - AWS Lake Formation
  - Amazon Redshift
  - Amazon S3
tags: ['aws', 'general']
status: atomic
topic: AWS Data Engineering
domain: Exam Prep
created_at: 2025-12-24
---
## Data Storage
###  Active Recall
- How is data secured or encrypted in this context?
- How does this service integrate with other AWS components mentioned?

---

[[Amazon S3 Fundamentals|S3]] provides the following features:

- 99.999999999% durability
- 99.999% availability - 53 minutes downtime per year.
- Global resiliency
- Highly configurable access policies
- HTTP access
- Centrally manage data at scale

[[Lake Formation]] provides the following features:

- Data lake foundation on Amazon [[Amazon S3 Fundamentals|S3]]
- Streamlined and centralized data management
- Straightforward data governance and security
- Enforce permissions with built-in integrations for data integration and big data processing
- Database style fine-grained permissions on resources
- Unified Amazon [[Amazon S3 Fundamentals|S3]] permissions

Amazon [[Redshift Data Loading COPY|Redshift]] provides the following features:

- Rapidly query datasets ranging in size from gigabytes to petabytes
- Visualize queries and analysis and share anywhere
- Automate building, training, and tuning ML models for business intelligence