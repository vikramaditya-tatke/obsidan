# Technical Interview Questions for BNP Paribas Data Platform Engineer (AVP)

### 1. Can you describe your experience with ClickHouse in a production environment? What were the main challenges you faced and how did you overcome them?
**Situation:** At SecurityHQ, I led the migration from MongoDB to ClickHouse Cloud to address the need for scalable, high-performance analytics.
**Task:** My responsibility was to ensure a seamless transition to ClickHouse, optimizing for cost, performance, and reliability in a production environment.
**Action:** I set up secure network access, integrated S3 storage, and implemented monitoring with Grafana and ClickHouse dashboards. I applied best practices for table engine selection and query optimization, and collaborated with stakeholders to ensure the solution met business needs.
**Result:** The migration resulted in a 75% reduction in annual costs and over 1000x improvement in analytical query performance. The platform supported rapid analytics for diverse clients.
**Learning:** I learned the importance of iterative testing, stakeholder engagement, and leveraging community best practices for successful production deployments.

### 2. How have you designed and implemented high availability and *disaster recovery* strategies for ClickHouse or other distributed databases?
**Situation:** At SecurityHQ, we needed to ensure our data platform could withstand failures and recover quickly, especially as our data volumes and client expectations grew.
**Task:** I was responsible for designing and implementing high availability and disaster recovery for our core databases.
**Action:** While I have not set up a ClickHouse cluster, I have designed and managed a sharded, replicated MongoDB cluster in production. This involved configuring replica sets for automatic failover, sharding for scalability, and using Ops Manager for automated backups and restores. I conducted capacity planning, query and data size estimations, documented all procedures and tested failover and recovery scenarios to ensure operational readiness.
**Result:** The MongoDB cluster provided robust high availability and disaster recovery, with minimal downtime during node failures and rapid recovery from backups. This setup met our business continuity requirements and client SLAs.
**Learning:** I learned the importance of regular testing, clear documentation, and automation in building resilient data platforms. I am actively learning ClickHouse Keeper and cluster management to extend these principles to ClickHouse in the future.

### 3. Walk us through a recent ClickHouse migration project you led or contributed to. What was your approach to data modelling and performance optimization?
**Situation:** The migration from MongoDB to ClickHouse at SecurityHQ required a new approach to data modelling for analytics.
**Task:** My goal was to design a schema that enabled fast, flexible analytics while minimizing storage costs.
**Action:** I created a test environment similar to the production setup. I leveraged de-normalized schemas, materialized views, and the appropriate MergeTree engines. I benchmarked query performance and iterated on the model based on real-world workloads and user feedback.
**Result:** The new model enabled sub-second analytics and reduced infrastructure costs by 80%.
**Learning:** I learned that close collaboration with end users and iterative benchmarking are essential for effective data modelling.

### 4. What steps do you take to ensure data security and compliance in your data platforms?
**Situation:** Working with sensitive client data at SecurityHQ required strict security and compliance measures.
**Task:** I was responsible for implementing controls to protect data and meet regulatory requirements.
**Action:** I used AWS Secrets Manager for credential management, enforced access controls, and enabled encryption for data at rest and in transit. I faciliated the integration of audit logs with SIEM tools used in the organization.
**Result:** The platform met client and regulatory expectations for security and compliance.
**Learning:** I learned that security is an ongoing process that requires vigilance, automation, and regular review.

### 5. How do you monitor and troubleshoot performance issues in ClickHouse? Are you familiar with tools like Prometheus and Grafana?
**Situation:** Performance monitoring was essential to ensure the reliability of our analytics platform.
**Task:** My role was to set up effective monitoring and quickly resolve any issues.
**Action:** I implemented monitoring with Grafana and ClickHouse dashboards, tracked key metrics, and configured alerts for critical thresholds. I troubleshot issues by analyzing logs and collaborating with the team.
**Result:** Issues were detected and resolved quickly, minimizing downtime and ensuring consistent performance.
**Learning:** I learned that proactive monitoring and clear alerting are vital for maintaining high service levels.

### 6. Can you explain your experience integrating databases into DevOps pipelines (e.g., using Jenkins, Ansible, or GitHub Actions)?
**Situation:** Automating deployments was a priority to support rapid development and reduce errors.
**Task:** I was responsible for integrating database changes into our CI/CD workflows.
**Action:** I built CI/CD pipelines using GitHub Actions for Airflow DAG deployment and database schema migrations. I used Docker for containerized testing and deployment.
**Result:** Deployment times were reduced, and the risk of manual errors was minimized.
**Learning:** I learned that automation and reproducibility are key to efficient, reliable operations.

### 7. What is your approach to backup and restore strategies for large-scale analytical databases?
**Situation:** Data loss or downtime could have significant business impact for our clients.
**Task:** I needed to ensure reliable backup and restore processes.
**Action:** I automated regular backups to S3 using ClickHouse tools, documented restore procedures, and tested recovery scenarios. I also applied similar strategies in MongoDB using Ops Manager.
**Result:** The platform was resilient to data loss, and recovery could be performed quickly and confidently.
**Learning:** I learned that regular testing and documentation are as important as the backup process itself.

### 8. Have you contributed to or customized ClickHouse at the code level (e.g., with C++ or other languages)? If not, how would you approach learning this?
**Situation:** My experience with ClickHouse has focused on deployment, configuration, and optimization rather than core code contributions.
**Task:** I am eager to deepen my understanding of ClickHouse internals and contribute to the open-source community.
**Action:** I have contributed to open-source projects in Python, Java, and Rust (see my GitHub), and I am actively learning C++ fundamentals. My approach would be to study the ClickHouse codebase, start with documentation or plugin contributions, and engage with the community.
**Result:** I am well-prepared to contribute to ClickHouse in the future as my C++ skills mature.
**Learning:** I learned that a growth mindset and willingness to learn new languages are essential for long-term technical impact.

### 9. Describe your experience administering databases on Unix/Linux systems. How do you monitor system resources and ensure optimal performance?
**Situation:** All my database deployments, including MongoDB and ClickHouse, have been on Linux systems.
**Task:** I was responsible for ensuring optimal performance and reliability.
**Action:** I used native tools (top, htop, iostat), automated monitoring, and Grafana dashboards to track CPU, memory, and disk I/O. I tuned system parameters and responded proactively to alerts.
**Result:** Systems remained stable and performant, supporting business needs without interruption.
**Learning:** I learned that deep familiarity with the OS and proactive monitoring are foundational for database reliability.

### 10. What are some common issues you’ve encountered with Linux-based database hosting, and how did you resolve them?
**Situation:** Hosting databases on Linux presented challenges such as disk space exhaustion and high I/O latency.
**Task:** My role was to identify and resolve these issues quickly.
**Action:** I implemented disk usage alerts, optimized storage layouts, and tuned kernel parameters. I also automated failover and recovery procedures where possible.
**Result:** Issues were resolved before they could impact users, and system reliability improved.
**Learning:** I learned that automation and early detection are key to preventing outages.

### 11. Tell us about a time you optimized an ETL pipeline for high throughput and reliability. What tools and techniques did you use?
**Situation:** At SecurityHQ, our event log ingestion pipeline was responsible for processing over 10TB of data weekly, and we were experiencing bottlenecks and reliability issues as data volumes grew.
**Task:** My responsibility was to redesign the pipeline to maximize throughput and ensure reliability, minimizing downtime and manual intervention.
**Action:** I re-architected the pipeline using Apache Airflow for orchestration and asynchronous Python for ingestion, which allowed for parallel processing of large data batches. I adopted efficient data formats like Parquet to reduce I/O overhead and containerized the pipeline for reproducibility and easier deployment. I also implemented structured logging for better monitoring and troubleshooting.
**Result:** The new pipeline achieved reliable, high-throughput ingestion with minimal downtime, supporting the business’s growing data needs without additional operational burden.
**Learning:** I learned that combining the right orchestration tools with efficient data formats and containerization can dramatically improve both scalability and reliability. This experience also reinforced the value of observability in production pipelines.

### 12. How do you approach data modelling for analytical workloads (e.g., star schemas, denormalization)?
**Situation:** When migrating from MongoDB to ClickHouse at SecurityHQ, we needed to support fast, flexible analytics for large-scale event data.
**Task:** My task was to design a data model that would enable sub-second analytics and support complex reporting requirements.
**Action:** I leveraged denormalized schemas and materialized views in ClickHouse, applying star schema principles where appropriate. I benchmarked different models using real-world queries and iterated based on performance data and feedback from analytics users.
**Result:** The resulting models enabled sub-second query performance and made it easy for business users to generate reports, directly supporting our analytics goals.
**Learning:** I learned that iterative design, benchmarking, and close collaboration with end users are crucial for effective data modelling in analytical systems.

### 13. How do you collaborate with development teams to optimize database schemas and queries?
**Situation:** At SecurityHQ, optimizing database performance required close collaboration between data engineering and development teams.
**Task:** I was responsible for ensuring that database schemas and queries were efficient and scalable as new features were developed.
**Action:** I led design reviews, provided training on ClickHouse best practices, and created clear documentation. I encouraged open feedback and peer code reviews, and shared insights from my own side projects and open-source contributions to foster a culture of learning.
**Result:** Teams adopted optimized schemas and queries, which led to measurable improvements in system performance and developer productivity.
**Learning:** I learned that open communication, documentation, and a willingness to share practical experience are key to successful cross-team collaboration.

### 14. Can you give an example of how you have trained or mentored others in new technologies or platforms?
**Situation:** As Lead Data Engineer at SecurityHQ, I was expected to upskill my team as we adopted new technologies like ClickHouse and Airflow.
**Task:** My goal was to ensure the team could confidently use these tools and follow best practices.
**Action:** I mentored five engineers through hands-on workshops, created onboarding materials, and led by example by sharing my own learning from open-source projects and GitHub. I encouraged team members to participate in side projects and open-source contributions to deepen their skills.
**Result:** The team became more self-sufficient and innovative, successfully adopting new technologies and contributing their own improvements to our data platform.
**Learning:** I learned that mentorship is most effective when it combines structured guidance with opportunities for independent exploration and real-world application.
