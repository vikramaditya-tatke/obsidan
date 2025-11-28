# Apache Spark
## PySpark
https://www.linkedin.com/learning/apache-pyspark-by-example/apache-pyspark?u=241209866
## Spark Concepts

### What is an RDD?

An RDD is essentially a collection of data elements, like a list in Python, but spread out across different computers in a cluster. RDDs have some key features that make them unique:

- **Immutable**: Once an RDD is created, you can’t modify it. However, you can apply transformations to create new RDDs based on existing ones.
- **Distributed**: The data is divided into smaller parts and distributed across many machines.
- **Fault-Tolerant**: PySpark automatically tracks how the data was transformed so it can recover lost data if there’s a failure.
