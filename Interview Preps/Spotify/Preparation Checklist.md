# Python and SQL Competitive Programming questions

1. Dynamic Programming
# Projects
1. Project using DataFlow -> PySpark -> BigQuery -> Looker. Use NVD API.
2. Project -> Copy some Spotify Data Engineering end to end project to get a basic understanding of the data.

# System Design

1. Interviews -
	1. Meta Data Engineer Interview
	2. Design Spotify (ex Google EM)
	3. 
# Data Modelling Concepts
## Concepts
1. Slowly Changing Dimensions and it's types.
2. Star Schema
3. Snowflake Schema
## Data Models
1. Kimbal Data Model
2. Data Vault
3. One Big Table
4. Relational

# Technologies
1. Kakfa
	1. Brokers
	2. Topics
	3. Partitions
	4. Producers and Consumers
	5. Differences between Zookeeper and KRaft.
2. Spark
	1. Apache Spark
	2. PySpark - https://www.linkedin.com/learning/apache-pyspark-by-example/apache-pyspark?u=241209866
	3. RDDs and other concepts
3. File Formats

| `Format`       | `CSV`                            | `Parquet`                         | `JSON`                          | `ORC`                               | `Avro`                            |
| :------------- | :------------------------------- | :-------------------------------- | :------------------------------ | :---------------------------------- | :-------------------------------- |
| Structure      | Flat Tabular                     | Columnar Binary                   | Hierarchical Key-Value pair     | Columnar Binary                     | Row based Binary                  |
| Human Readable | Yes, simple                      | No                                | Yes, Flexible                   | No                                  | No                                |
| Schema Support | No Schema Enforcement            | Built-in Schema, Schema Evolution | Schema Optional                 | Built-in Schema, Complex types      | Built-in Schema, Schema Evolution |
| Compression    | Poor, Text-based                 | Excellent, Column based           | Moderate, Text-based            | Excellent, Column based             | Good, Row based                   |
| Performance    | Fast (simple), Slow (Complex)    | High for column queries           | Moderate, Slow (for large data) | High for column queries             | High for row based queries        |
| Use cases      | Simple Queries, Interoperability | Big Data Analytics, Data Lakes    | APIs, Web Apps                  | Big Data Analytics, Data Warehouses | Data Serialization, Streaming     |

# Differences between databases

## OLTP Vs OLAP
## SQL Vs NoSQL

# Data Ingestion
1. [[Batch Data]]
2. Streaming Data

# Important Questions

1. Given an array find the sum of all records in it and scale your approach for a million records.


