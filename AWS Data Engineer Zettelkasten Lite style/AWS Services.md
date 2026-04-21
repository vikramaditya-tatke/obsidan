---
services:
  - AWS Glue
  - AWS IAM
  - AWS Lake Formation
  - AWS Lambda
  - Amazon Athena
  - Amazon Aurora
  - Amazon Bedrock
  - Amazon DataZone
  - Amazon DynamoDB
  - Amazon EMR
  - Amazon Kinesis
  - Amazon Managed Service for Apache Flink
  - Amazon OpenSearch Service
  - Amazon QuickSight
  - Amazon RDS
  - Amazon Redshift
  - Amazon S3
  - Amazon SageMaker
tags: ['aws', 'general']
status: atomic
topic: AWS Data Engineering
domain: Exam Prep
created_at: 2025-12-24
---
## AWS Services

AWS services are generally categorized as [[Public vs Private AWS Services|Public or Private]].

## Variety

1. Amazon [[RDS and Aurora Fundamentals|RDS]] - Transactional and scalable database compatible with Aurora, MySQL, Postgres.
	 Amazon [[RDS and Aurora Fundamentals|RDS]] streamlines replication to enhance database availability and improve data durability. It can also scale beyond the capacity constraints of a single database instance for read-heavy database workloads.
	 
2. Amazon [[Redshift Data Loading COPY|Redshift]] - Data Warehousing
	Amazon [[Redshift Data Loading COPY|Redshift]] analyzes structured and semistructured data from databases, data lakes, and data warehouses to deliver the best price performance at any scale. You can use Amazon [[Redshift Data Loading COPY|Redshift]]'s capabilities to run analytics on structured data within the data warehouse. When using additional features like Amazon [[Redshift Data Loading COPY|Redshift]] Spectrum, you can also analyze semistructured data stored in Amazon [[Amazon S3 Fundamentals|S3]] data lakes, providing a comprehensive analytics solution.
	Queries live data across organizations, accounts, and Regions
	
3. Open Search - Real-time monitoring, alerting, searching
	OpenSearch is an open source, distributed search and analytics suite for a broad set of use cases. Amazon OpenSearch Service makes it convenient to perform interactive log analytics, real-time application monitoring, and website search. Amazon OpenSearch Service is an AWS managed service to run and scale OpenSearch clusters. OpenSearch provides a fast and highly scalable system for exploring and visualizing data, with convenient OpenSearch Dashboards. Amazon OpenSearch Service supports integration with streaming data from Amazon [[Amazon S3 Fundamentals|S3]] buckets, Amazon [[Kinesis Data Streams]], and [[DynamoDB Capacity Modes|DynamoDB]] Streams.
	
4. [[DynamoDB Capacity Modes|DynamoDB]] - NoSQL Database for high-performance
	Companies can use Amazon [[DynamoDB Capacity Modes|DynamoDB]] to create a database table that can store and retrieve any amount of data, and serve any level of request traffic. They can scale up or scale down their tables' throughput capacity without downtime or performance degradation. Reliable single-digit millisecond performance and up to 99.99999999% availability.

![[Pasted image 20250913195513.png]]

## Velocity

1. [[EMR Fundamentals|EMR]] - Petabyte scale data processing and interactive analytics.
	- Seamlessly integrates with Amazon [[SageMaker]]
	- Performs machine learning tasks on large datasets
	- Uses open-source big data frameworks ([[Spark]], Hadoop, HBase, Hive, Hudi, Presto) to distribute data processing tasks
	
2. MSK - Fully managed and scalable Apache Kafka.
3. [[Kinesis Data Streams|Kinesis]] - Propriety cost-effective service to process streaming data.
4. [[Lambda]] - Serverless, event-driven compute.

| Service                                 | Description                                                                                                                                   |
| --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Amazon [[Kinesis Data Streams]]             | A data streaming service that continuously captures data in real time from hundreds of thousands of sources.                                  |
| Amazon [[Kinesis Data Firehose]]            | Near real-time analytics with existing business intelligence tools by capturing, transforming, and loading data streams into AWS data stores. |
| Amazon [[Managed Service for Apache Flink]] | Build and run Apache Flink applications, and query and analyze streaming data without setting up infrastructure and clusters.                 |

## Veracity

1. [[EMR Fundamentals|EMR]]
	This service provides a robust data collection and processing platform to analyze vast amounts of data. Amazon [[EMR Fundamentals|EMR]] helps you focus on transforming and analyzing your data so you don't have to worry about managing infrastructure. Amazon [[EMR Fundamentals|EMR]] is a hands-on approach to creating your data pipeline and requires your team to have strong technical know-how.
	
2. [[AWS Glue Fundamentals|Glue]]
	AWS [[AWS Glue Fundamentals|Glue]] is a serverless data integration and managed ETL service. This service provides a more streamlined experience than Amazon [[EMR Fundamentals|EMR]]. AWS [[AWS Glue Fundamentals|Glue]] makes it convenient to clean and normalize data directly from data lakes, data warehouses, and databases. AWS [[AWS Glue Fundamentals|Glue]] can consume from streaming sources, clean and transform it in-flight, and share it for analysis in seconds in your desired data store. You can process event data like Internet of Things (IoT) event streams, clickstreams, and network logs, and run a variety of complex analytics and ML operations.


	AWS [[AWS Glue Fundamentals|Glue]] can be used as a metastore for your final transformed data by using the [[AWS [[AWS Glue Fundamentals|Glue]] Data Catalog]]. You can manage data quality in datasets with AWS [[AWS Glue Fundamentals|Glue]] Data Quality. This service analyzes your chosen dataset and recommends data quality rules that you can optimize.

	
3. [[AWS Glue Fundamentals|Glue]] DataBrew
	It is a visual data preparation tool that helps data analysts and data scientists clean and normalize data to prepare it for analytics and ML. With AWS [[AWS Glue Fundamentals|Glue]] DataBrew, you can to visually map the lineage of your data to understand the various data sources and transformation steps that the data has been through.


	AWS [[AWS Glue Fundamentals|Glue]] DataBrew gives prebuilt transformations to automate data preparation tasks, all without the need to write any code. You can automate filtering anomalies, converting data to standard formats and correcting invalid values, and other tasks. After your data is ready, you can immediately use it for analytics and ML projects. You only pay for what you use—no upfront commitment.

	
4. DataZone
	Amazon DataZone is a data management service to catalog, discover, govern, share, and analyze your data. An integrated analytics portal gives you a personalized view of all your data while enforcing your governance and compliance policies at scale. Administrators and data stewards who oversee your organization's data assets can manage and govern access to data using fine-grained controls.


	With Amazon DataZone, you can share and access your data across accounts and supported Regions. Amazon DataZone streamlines your experience across AWS services, including but not limited to, Amazon [[Redshift Data Loading COPY|Redshift]], AWS [[AWS Glue Fundamentals|Glue]], and AWS [[Lake Formation]]. Amazon DataZone extends governance controls through [[AWS [[AWS Glue Fundamentals|Glue]] Data Catalog]], AWS Identity and Access Management ([[AWS IAM]]), and AWS [[Lake Formation]]. The service operates within your infrastructure without relying on individual credentials.

## Value
1. QuickSight - BI
2. [[SageMaker]] - Build and Train ML Models
3. Bedrock - GenAI Applications
4. [[AWS Data Engineer Zettelkasten Lite style/Athena]] - Serverless analytics service built on top of open-source tools
	Amazon [[AWS Data Engineer Zettelkasten Lite style/Athena]] is a serverless, interactive analytics service built on open-source frameworks. [[AWS Data Engineer Zettelkasten Lite style/Athena]] helps solve data value challenges so you can conveniently query and analyze data stored in Amazon [[Amazon S3 Fundamentals|S3]] using standard SQL queries. [[AWS Data Engineer Zettelkasten Lite style/Athena]] is designed for interactive analytics, running queries, and getting results in real time. This is especially valuable for one-time queries and exploratory data analysis. [[AWS Data Engineer Zettelkasten Lite style/Athena]] supports rapid and cost-effective data exploration, which in turn helps you derive valuable insights. [[AWS Data Engineer Zettelkasten Lite style/Athena]]'s serverless and scalable structure, integration with other AWS services and support for various data formats make it a powerful tool for gaining value from data.