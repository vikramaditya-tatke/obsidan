specifics of my skillset as relevant to the  Database position at BNP Paribas. discussed on the call on Monday. With extensive hands-on experience in both MongoDB and ClickHouse environments, I have successfully designed, deployed, and optimized large-scale data architectures in production, tailored to the unique needs of multiple stakeholders across development, infrastructure, and management teams. In my most recent role, I architected and deployed a self-hosted MongoDB cluster from the ground up. This included: 

    Capacity planning by engaging with SMEs, developers, and management to forecast growth and performance needs. Infrastructure coordination for resource allocation and budget alignment. 
    Manual setup of data nodes, config servers (similar to ClickHouse Keeper), and routers using UNIX. 
    Deployment of MongoDB Ops Manager for comprehensive backup, monitoring, and alerting. 
    Configuration of alerts for critical events such as disk usage >80%, CPU and RAM usage >90% for over 5 minutes, and discovery failures on config servers. Alerts were routed to email and Microsoft Teams. 


Post-deployment, I managed the cluster primarily via Ops Manager, with SSH used only for tasks like disk expansion or node replacement. Troubleshooting involved in-depth analysis of system and MongoDB logs, and when necessary, I liaised with MongoDB professional services, maintaining detailed documentation of issues, hypotheses, and resolutions. 
The sharded replicated cluster comprised 4 shards with 2 replicas each, totaling 12 nodes. 
I created performant Python scripts for various DB admin tasks including table/index/user management and metric extraction to validate ongoing capacity plans. 

Furthermore, I led the migration from MongoDB to ClickHouse Cloud using AWS DMS. Key responsibilities included: 

    Setting up secure network access and S3 storage integration. 
    Learning and applying ClickHouse best practices.
    Implementing monitoring solutions using built-in dashboards and Grafana. 
    Cost optimization using S3Table Engine and smart usage of table engines like Merge, MergeTree, SummingMergeTree, and AggregatingMergeTree. 
    PostgreSQL integration using Postgre Table Engine with scheduled refreshes via Refreshable Materialized Views. 


In my role as a Data Engineer, I also architected and maintained ETL pipelines written in pure Python and Apache Airflow to ingest data from diverse sources such as TCP streams, REST APIs, relational databases, and object storage. I played a key role in transitioning from pure Python ETL scripts to Apache Airflow, significantly improving maintainability, observability, and scheduling. Throughout the process, I performed extensive testing of data ingestion and query optimization by running both the databases and Python ETL processes within containerized environments using Docker. 

Adopting ClickHouse for analytics in place of MongoDB reduced infrastructure costs by 80% and cut down data readiness time by 65%. I also implemented CI/CD pipelines for Airflow using GitHub Actions. I can provide some of the scripts I developed for MongoDB administration and the migration from MongoDB to ClickHouse upon request. These are currently hosted in my organization’s internal repositories and contain specific business logic. 

Beyond the technical work, I: Mentored junior engineers and participated in peer code reviews. Translated complex architectural and performance insights into clear, actionable summaries for management. Successfully advocated for necessary system upgrades and process improvements. 

My interests align strongly with cutting-edge trends in analytics and AI. I actively explore Business Intelligence as Code platforms like Rill Data and Evidence.dev, and regularly attend ClickHouse webinars hosted by CTO Alexey Milovidov, alongside events such as AWS Summit, MongoDB .local, Airflow Roadshow, etc. 