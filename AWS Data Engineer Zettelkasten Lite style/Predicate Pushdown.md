---
services:
  - AWS Glue
tags: ['aws', 'glue', 'optimization']
status: atomic
topic: AWS Data Engineering
domain: Exam Prep
created_at: 2025-12-24
---
## Predicate Pushdown
###  Active Recall
- What are the key cost drivers or pricing models for this service?

---



## Predicate Pushdowns

AWS [[AWS Glue Fundamentals|Glue]]’s support for server-side filtering with catalog partition predicates directly during the creation of DynamicFrames is a powerful feature for optimizing ETL processes. This capability allows the ETL job to selectively process only the necessary data by utilizing the metadata catalog’s partition indexes. Doing so significantly reduces the volume of data that needs to be read and processed, leading to reductions in execution time and cost.

Server-side filtering applies filter predicates against the partition metadata stored in the [[AWS Glue Data Catalog]]. This means that before the data is even loaded into the DynamicFrame, AWS [[AWS Glue Fundamentals|Glue]] can narrow down the data to just the relevant partitions based on the criteria specified by the ETL job. This approach is more efficient than client-side filtering, where data is first loaded into memory before being filtered, and it leverages the AWS [[AWS Glue Fundamentals|Glue]] catalog’s capabilities to minimize data scan and processing.

> Pushdown predicates are less efficient than catalog partition predicates when used directly during DynamicFrame creation. This is because pushdown predicates apply filters after the DynamicFrame has been created, leading to higher initial data loads before the filter is applied.