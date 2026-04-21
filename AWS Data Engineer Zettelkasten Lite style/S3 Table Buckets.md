---
services:
  - AWS Glue
  - AWS IAM
  - AWS Lake Formation
  - Amazon Athena
  - Amazon EMR
  - Amazon Redshift
  - Amazon S3
  - Amazon SageMaker
tags: ['aws', 's3', 'table-buckets']
status: atomic
topic: AWS Data Engineering
domain: Exam Prep
created_at: 2025-12-24
---
## S3 Table Buckets
###  Active Recall
- What are the key cost drivers or pricing models for this service?
- How does this service integrate with other AWS components mentioned?

---

![[S3_1]]

## S3 Table Buckets

### Integration with AWS Analytics Services

To access table buckets from AWS query engines such as Amazon [[SageMaker]], Amazon [[AWS Data Engineer Zettelkasten Lite style/Athena]], Amazon [[Redshift Data Loading COPY|Redshift]], and Amazon [[EMR Fundamentals|EMR]], table buckets must be integrated with AWS analytics services. After this integration is enabled, all table buckets in this account and Region will automatically be available in [[AWS [[AWS Glue Fundamentals|Glue]] Data Catalog]] under the catalog named s3tablescatalog. [Learn more about the integration](https://docs.aws.amazon.com/console/s3/tables-bucket-integration) . This integration uses the AWS [[AWS Glue Fundamentals|Glue]] and AWS [[Lake Formation]] services and might incur [[AWS Glue Fundamentals|Glue]] request and storage costs. [View AWS [[AWS Glue Fundamentals|Glue]] pricing](https://aws.amazon.com/glue/pricing) 

#### AWS [[Lake Formation]] Table Bucket Registration

S3 creates an [[AWS IAM]] role named `S3TablesRoleForLakeFormation` on your behalf. By attaching `lakeformation.amazonaws.com` as a trusted entity, this role gives AWS [[Lake Formation]] access to all table buckets in your account. AWS [[Lake Formation]] also needs permission to register all table buckets in this Region. [View permission details](https://docs.aws.amazon.com/console/s3/tables-lakeformation-policy) 

#### AWS [[AWS Glue Fundamentals|Glue]] Catalog Creation

A catalog named s3tablescatalog is created in [[AWS [[AWS Glue Fundamentals|Glue]] Data Catalog]], as well as sub-catalogs within it for each table bucket in this Region.

## S3 Bucket Policy
- A form of resource policy.