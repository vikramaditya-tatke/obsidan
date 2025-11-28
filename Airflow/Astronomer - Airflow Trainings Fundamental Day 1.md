# Airflow Core Components 

1. API Server
2. Metadata database
3. Scheduler
4. DAG File Processor
5. Executor
6. Queue
7. Worker(s)


|                    |                |     |
| ------------------ | -------------- | --- |
| API Server         | FastAPI Server |     |
| Metadata database  |                |     |
| DAG File Processor |                |     |
| Executor           |                |     |
| Queue              |                |     |
| Worker             |                |     |


![[Pasted image 20250530125702.png]]

DAG File Processor - 

In Astronomer, the DAG file is cached so if there is no change 
If we create a Variable and a task is created based on this Variable then the DAG file processor 

DAG Factory - Abstraction of a DAG. Builds from a Data Artefacts. Example if S3 has multiple JSON files which store info about a database such as the name of the database - the table. We say to the DAG factory that we want to build a DAG factory based on these JSON files, if they change the DAG changes. 
Such processes consume a lot of processing of the DAG File Processor which could end up costing a considerable amount of money on Astronomer Cloud. It is crucial to write optimized code in such cases to minimize the load on the DAG File Processor.