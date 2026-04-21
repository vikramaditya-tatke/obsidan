---
services:
  - AWS Config
  - AWS Lambda
  - Amazon Athena
  - Amazon S3
  - Amazon SNS
tags: ['aws', 'general']
status: atomic
topic: AWS Data Engineering
domain: Exam Prep
created_at: 2025-12-24
---
## Config
###  Active Recall
- How is data secured or encrypted in this context?

---


> [!PDF|] [[AWSCertifiedDataEngineerSlides.pdf#page=631&selection=18,0,64,8|AWSCertifiedDataEngineerSlides, p.631]]
> > Helps with auditing and recording compliance of your AWS resources
> > • Helps record configurations and changes over time
> > • Questions that can be solved by AWS Config:
> > • Is there unrestricted SSH access to my security groups?
> > • Do my buckets have any public access?
> > • How has my ALB configuration changed over time?
> > • You can receive alerts (SNS notifications) for any changes
> > • AWS Config is a per-region service
> > • Can be aggregated across regions and accounts
> > • Possibility of storing the configuration data into [[Amazon S3 Fundamentals|S3]] (analyzed by [[AWS Data Engineer Zettelkasten Lite style/Athena]])

- Config is a regional service and by default monitors services in a specific account.
- Can be configured for cross-region and cross-account aggregation.
- Used for Audit and Compliance.
- DOES NOT configure permissions. It can only be used for monitoring compliance of AWS Resource and Services against defined standards and does NOTHING to stop from breaching these standards.
- Stores the change history in [[Amazon S3 Fundamentals|S3]] buckets, from when it is enabled.
- Config rules can be setup so that resources can be evaluated against them. Config rules can either be AWS managed or custom (using [[Lambda]] functions).
- Config can send a stream of notifications using [[SNS]]