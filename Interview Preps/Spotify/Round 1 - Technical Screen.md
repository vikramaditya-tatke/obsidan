# Projects
1. Project using DataFlow -> PySpark -> BigQuery -> Looker. Use NVD API.
2. Project -> Copy some Spotify Data Engineering end to end project to get a basic understanding of the data.
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
	5. Zookeeper 
	6. KRaft.
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

# Data Ingestion Strategies
1. [[Batch Data]]
2. Streaming Data

# Question Bank

## Project
Discuss a project related to data engineering 
- Challenges 
- Conflicts
- What would you do differently?

## Coding

### LeetCode

| No. | Coding Question                                                                                        | Matching LeetCode Problem                | Difficulty | Status |
| --- | ------------------------------------------------------------------------------------------------------ | ---------------------------------------- | ---------- | ------ |
| 1 | Given an array find the sum of all records in it and scale your approach for a million records.      | 1. Two Sum                             | Easy     | [ ]    |
| 2   | Write code to find the second largest number in an array. How would you scale it to a million records? | 215. Kth Largest Element in an Array     | Medium     | [ ]    |
| 3   | How do you delete a linked list?                                                                       | 206. Reverse Linked List                 | Easy       | [ ]    |
| 4   | Fibonacci (iterative and recursive and dynamic programming)                                            | 509. Fibonacci Number                    | Easy       | [ ]    |
| 5   | Simple SQL on a single table (group by and accumulate)                                                 | 185. Department Top Three Salaries       | Hard       | [ ]    |
| 6   | Calculate the median of a window of values over an infinity data stream                                | 295. Find Median from Data Stream        | Hard       | [ ]    |
| 7   | Given multiple users and the songs they listened to in order, detect the longest common pattern of ... | 718. Maximum Length of Repeated Subarray | Medium     | [ ]    |

### SQL
1. Write a query to find the earliest date each user played their third unique song.
2. Write a SQL query to find the top 10 songs. Practice it for each of the windowing types
	1. Global Window
	2. Tumbling Window
	3. Sliding Window
	4. Session Window
3. Given a plays table, write a query to find users who listened to > 100 songs in a week.

## Technical

1. Common data structures and algorithms (search in sorted list, search in linked list, red-black-tree)
2. How would you implement [[Data Engineering Concepts#Priority Queues]]? 
3. [[Data Engineering Concepts#Hashmap collision resolution strategies]].
4. Examples of [[Data Engineering Concepts#Probabilistic Data Structures]] advantages
5. Difference between functional and imperative programming.
6. How would you represent a graph in-memory?
7. Difference between columnar and row based database. 
8. Difference between inner and outer join. 
9. Explain MapReduce.
10. What are the merits and demerits of Docker?
11. What is the difference between OLAP and OLTP?
12. What is the difference between Zookeeper and KRaft?

## System Design

## Problems
1. Design a data solution to calculate the top artists per country, given a data set of song "plays" and metadata (song, artists etc.)
2. Design a "weekly wrapped" feature (top 50 songs per country per week)
3. Design “Top 10 Songs Played” with Kafka → Spark Streaming → Cassandra, addressing scaling, latency, fault‑tolerance.
4. Dashboard Metrics: Design a system supporting a dashboard showing metrics about played songs with various filters.
5. Ingesting Live Events: Design a system to ingest billions of live events.
6. Playlist Photo Upload Service: Design a service for uploading playlist photos.
7. Recommendation Engine: Design a recommendation engine for a music streaming service.
8. In-App Notifications: Architect a system for in-app notifications of friend activity.

## Solving the problems
##### Step 1: Limit the scope of the problem to fit the discussion into an hour.

##### Step 2: Considering functional and non-functional requirements at the start of the interview is a good idea.

| ___Funtional Requirements___ | ___Non-functional Requirements___<br> |
| :--------------------------: | ------------------------------------- |
|        Core Features         | Low-latency                           |
|       Data Management        | High-availability                     |
|          Compliance          | Secure connection                     |

Consider implementing the [[CAP Theorem]] at this step as it will help in narrowing the scope even further and help us understand whether we must prioritize consistency or availability?

##### Step 3: Come up with a rough architecture and look for feedback.