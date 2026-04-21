**AWS Glue** is a fully managed extract, transform, and load (ETL) service that makes it easy for customers to prepare and load data for analytics. It provides capabilities for schema detection, ETL jobs, and crawlers that make it useful for working with dynamic or changing schemas.

AWS Glue provides real-time, continuous logging for AWS Glue jobs. You can view real-time **Apache Spark job logs** in Amazon CloudWatch, including **driver logs, executor logs, and an Apache Spark job progress ba**r.


## Predicate Pushdowns

AWS Glue’s support for server-side filtering with catalog partition predicates directly during the creation of DynamicFrames is a powerful feature for optimizing ETL processes. This capability allows the ETL job to selectively process only the necessary data by utilizing the metadata catalog’s partition indexes. Doing so significantly reduces the volume of data that needs to be read and processed, leading to reductions in execution time and cost.

Server-side filtering applies filter predicates against the partition metadata stored in the AWS Glue Data Catalog. This means that before the data is even loaded into the DynamicFrame, AWS Glue can narrow down the data to just the relevant partitions based on the criteria specified by the ETL job. This approach is more efficient than client-side filtering, where data is first loaded into memory before being filtered, and it leverages the AWS Glue catalog’s capabilities to minimize data scan and processing.


 Pushdown predicates are less efficient than catalog partition predicates when used directly during DynamicFrame creation. This is because pushdown predicates apply filters after the DynamicFrame has been created, leading to higher initial data loads before the filter is applied.

## Job Metrics
**AWS Glue** provides a feature called job metrics, which can be used to estimate the number of DPUs that can be used to scale out an AWS Glue job. This feature is particularly useful in understanding the resource utilization of your jobs and can help in making informed decisions about scaling.

When you run a job, AWS Glue provides metrics such as the total number of actively running executors, the number of completed stages, and the number of maximum needed executors. These metrics can give you insights into whether your job is under-provisioned or over-provisioned.

For example, if the number of maximum needed executors is significantly higher than the number of active executors, it indicates that the job is under-provisioned. In such a case, you can increase the maximum capacity job parameter, which effectively increases the number of DPUs allocated to the job.
# Glue Workflows

Glue Workflows is primarily used to create and visualize complex ETL activities

# Glue DataBrew
- Visual data preparation tool that helps data analysts with data preparation tasks such as data profiling, cleaning, and normalizing
- Offers a streamlined solution for data quality management, particularly beneficial in scenarios requiring precise and automated data validation
- Ability to define specific data quality rules within a ruleset makes it an optimal choice for scenarios like ensuring inventory data accuracy.

# Glue in [[AWS Data Engineer/CloudWatch]]
When you start an AWS Glue job, it sends the real-time logging information to CloudWatch (every 5 seconds and before each executor termination) after the Spark application starts running. You can view the logs on the AWS Glue console or the CloudWatch console dashboard.

The continuous logging feature includes the following capabilities:

– Continuous logging with a default filter to reduce high verbosity in the logs

– Continuous logging with no filter

– A custom script logger to log application-specific messages

– A console progress bar to track the running status of the current AWS Glue job


# Glue Data Catalog

**AWS Glue Data Catalog** is a fully-managed service that serves as a centralized metadata repository. It can be used as a drop-in replacement for the Apache Hive Metastore, providing a unified metadata repository across various services. 
	*multiple data analytics teams each running their own Amazon EMR clusters.*

> Only one AWS Glue Data Catalog can be created per region
- Crawl data sources to discover schemas and populate your Catalog with new and modified table and partition definitions. Automatically keeps the metadata up-to-date, reducing the need for manual management.
- Glue Data Catalog maintains schema versioning and supports reverting back to older schema
> Glue Database is just a collection of catalogs organized together.