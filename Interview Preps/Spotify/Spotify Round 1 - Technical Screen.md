# Projects
1. Project using DataFlow -> PySpark -> BigQuery -> Looker. Use NVD API.
2. Project -> Copy some Spotify Data Engineering end to end project to get a basic understanding of the data.
# Data Modelling Concepts

1. [[Data Modelling#Slowly Changing Dimensions]].
2. Snowflake Schema
3. Kimbal Data Model AKA _Dimensional Modelling_ AKA _Star Schema_
4. Data Vault
5. One Big Table
6. Relational

# Technologies

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

| No. | Coding Question                                                                                          | Matching LeetCode Problem                | Difficulty |
| --- | -------------------------------------------------------------------------------------------------------- | ---------------------------------------- | ---------- |
| *1* | *Given an array find the sum of all records in it and scale your approach for a million records.*        | *1. Two Sum*                             | *Easy*     |
| *2* | *Write code to find the second largest number in an array. How would you scale it to a million records?* | *215. Kth Largest Element in an Array*   | *Medium*   |
| 3   | How do you delete a linked list?                                                                         | 206. Reverse Linked List                 | Easy       |
| *4* | *Fibonacci (iterative and recursive and dynamic programming)*                                            | *509. Fibonacci Number*                  | *Easy*     |
| 6   | Calculate the median of a window of values over an infinity data stream                                  | 295. Find Median from Data Stream        | Hard       |
| 7   | Given multiple users and the songs they listened to in order, detect the longest common pattern of ...   | 718. Maximum Length of Repeated Subarray | Medium     |

### SQL
1. Write a query to find the earliest date each user played their third unique song.
2. Write a SQL query to find the top 10 songs. Practice it for each of the windowing types
	1. Global Window
	2. Tumbling Window
	3. Sliding Window
	4. Session Window
3. Given a plays table, write a query to find users who listened to > 100 songs in a week.


## Technical

1. How would you implement [[Data Engineering Concepts#Priority Queues]]? 
2. [[Data Engineering Concepts#Hashmap collision resolution strategies]].
3. Examples of [[Data Structures and Algorithms#Probabilistic Data Structures]]
4. Difference between functional and imperative programming - [[Programming Fundamentals]].
5. Difference between columnar and row based database - [[OLTP Vs OLAP]]. 
6. Difference between inner and outer join - [[SQL Fundamentals#Types of Joins in SQL]]. 
7. Different types of [[File Formats]].
8. Explain MapReduce.
9. What are the merits and demerits of Docker?

| **Demerit**          | **Description**                                                  |
| -------------------- | ---------------------------------------------------------------- |
| Security Risks       | Shared kernel, privilege escalation, insecure images             |
| Performance Overhead | Slower I/O and CPU-bound tasks compared to bare metal            |
| Complex Networking   | Difficult to configure and troubleshoot, especially across hosts |
| Data Persistence     | Ephemeral nature, volume management can be tricky                |
| Resource Management  | Poor isolation can lead to resource starvation                   |
| Learning Curve       | Multi-container setups and debugging can be complex              |
| GUI Limitations      | Not designed for desktop GUI apps                                |
| Platform Issues      | VM-based setup on Windows/macOS adds latency and complexity      |
| Image Bloat          | Unoptimized images can be large and inefficient                  |
| Ecosystem Lock-in    | Tight coupling with Docker tools and formats                     |

10. What is the difference between Zookeeper and KRaft?

| **Feature**                    | **ZooKeeper**                                          | **KRaft (Kafka Raft)**                              |
| ------------------------------ | ------------------------------------------------------ | --------------------------------------------------- |
| **Definition**                 | External coordination service used by Kafka            | Kafka’s built-in consensus mechanism (Raft-based)   |
| **Role in Kafka**              | Manages Kafka metadata, broker coordination, elections | Replaces ZooKeeper, handles all metadata internally |
| **Architecture**               | Kafka + ZooKeeper cluster (separate systems)           | Kafka-only cluster with internal metadata quorum    |
| **Consensus Algorithm**        | Zab (ZooKeeper Atomic Broadcast)                       | Raft                                                |
| **Metadata Storage**           | Stored in ZooKeeper                                    | Stored in special Kafka topic (`@metadata`)         |
| **Broker Controller Election** | Done via ZooKeeper                                     | Done via Raft internally                            |
| **Complexity**                 | Higher (managing two systems: Kafka + ZooKeeper)       | Lower (single system with unified management)       |
| **Scalability**                | Limited by ZooKeeper’s scalability                     | Better scalability with Kafka-native metadata       |
| **Fault Tolerance**            | Dependent on ZooKeeper availability                    | Handled internally with Raft replication            |
| **Introduced In**              | Original Kafka architecture (pre-2.8)                  | Kafka 2.8 (preview), stable in Kafka 3.3+           |
| **Deployment**                 | Requires separate ZooKeeper setup                      | ZooKeeper-free Kafka mode (`KRaft` mode)            |

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

## Steps to solve the problems
##### Step 1: Limit the scope of the problem to fit the discussion into an hour.

##### Step 2: Considering functional and non-functional requirements at the start of the interview is a good idea.

| ___Funtional Requirements___ | ___Non-functional Requirements___<br> |
| :--------------------------: | :-----------------------------------: |
|        Core Features         |              Low-latency              |
|       Data Management        |           High-availability           |
|          Compliance          |           Secure connection           |

Consider implementing the [[CAP Theorem]] at this step as it will help in narrowing the scope even further and help us understand whether we must prioritize consistency or availability.

##### Step 3: Come up with a rough architecture and look for feedback.