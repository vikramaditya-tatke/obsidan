---
services:
  - AWS Glue
  - Amazon EMR
  - Apache Hive
tags: ['aws', 'glue', 'catalog']
status: atomic
topic: AWS Data Engineering
domain: Exam Prep
created_at: 2025-12-24
---
ca## AWS Glue Data Catalog
###  Active Recall
- How does Glue Data Catalog replace Hive Metastore in multi-EMR cluster scenarios?
- What is the limitation on the number of Glue Data Catalogs per region?

---


## Glue Data Catalog

**AWS Glue Data Catalog** is a fully-managed service that serves as a centralized metadata repository. It can be used as a drop-in replacement for the Apache Hive Metastore, providing a unified metadata repository across various services.
	*multiple data analytics teams each running their own Amazon [[EMR Fundamentals|EMR]] clusters.*

> Only one AWS Glue Data Catalog can be created per region
- Crawl data sources to discover schemas and populate your Catalog with new and modified table and partition definitions. Automatically keeps the metadata up-to-date, reducing the need for manual management.
- Glue Data Catalog maintains schema versioning and supports reverting back to older schema
> Glue Database is just a collection of catalogs organized together.

## Updating Partitions: API vs. ETL Property

In AWS Glue, you can update the Data Catalog with new partitions using two distinct approaches.

### `create_partition` API
- **Definition**: A standard AWS Glue Data Catalog API call (available via Boto3, CLI, or SDK).
- **Mechanism**: Manually adds a single partition to a specific table's metadata.
- **Use Case**: Used when managing partitions **outside** of a standard Glue ETL job (e.g., in an AWS Lambda function, custom script, or post-processing step).
- **Cons**: Requires explicit knowledge of partition values and S3 paths; requires one API call per partition (or `batch_create_partition` for up to 100).

### `enableUpdateCatalog` Property
- **Definition**: A configuration parameter used within **Glue ETL Spark scripts** (specifically for `DynamicFrames`).
- **Mechanism**: Automatically updates the Data Catalog (creates tables, updates schema, or adds partitions) during the job execution as data is written to S3.
- **Implementation**:
    ```python
    glueContext.write_dynamic_frame.from_catalog(
        frame=frameToWrite,
        database="dbName",
        table_name="tableName",
        additional_options={
            "enableUpdateCatalog": True,
            "updateBehavior": "UPDATE_IN_DATABASE",
            "partitionKeys": ["year", "month"]
        }
    )
    ```
- **Use Case**: Best practice for Standard Glue ETL jobs to avoid running a separate Crawler after the job completes.
- **Pros**: Zero-manual-intervention; keeps Catalog in sync with the data being written in real-time.

> [!INFO] Key Difference
> Use **`create_partition`** for manual/external metadata management. Use **`enableUpdateCatalog`** for automated, job-integrated metadata management within Glue ETL.
