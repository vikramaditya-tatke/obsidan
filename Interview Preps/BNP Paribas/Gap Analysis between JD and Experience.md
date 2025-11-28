| Area                                                  | Job Requirement                                                           | Your CV Match                                                                                                | Gap/Notes                                                                                                                                      |
| ----------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| **ClickHouse Expertise**                              | Production experience managing ClickHouse, clustering, performance tuning | ✔️ Led MongoDB → ClickHouse migration; optimized analytical workloads; ClickHouse Certified Developer (2025) | ✅ Strong match                                                                                                                                 |
| **Unix/Linux Skills**                                 | Strong Unix/Linux administration for database hosting                     | ✔️ Extensive Linux experience (e.g., database migrations, optimizations)                                     | ✅ No gap                                                                                                                                       |
| **Backup & Disaster Recovery**                        | Designed/implemented DR strategies for ClickHouse                         | ➖ Not explicitly mentioned                                                                                   | **Potential gap** → Prepare to discuss backup/DR approaches you've designed, even conceptually                                                 |
| **High Availability / Fault Tolerance**               | Designed fault-tolerant clusters, HA architecture                         | ➖ Not explicitly stated in CV                                                                                | **Partial gap** → You can frame your large-scale data streaming and ingestion pipelines (10TB/week) to show reliability engineering experience |
| **DevOps (Jenkins, Ansible)**                         | Integrated databases into CI/CD pipelines with Jenkins/Ansible            | ✔️ CI/CD pipelines via GitHub Actions                                                                        | **Minor gap** → No direct Jenkins/Ansible, but GitHub Actions is transferable; show willingness to learn                                       |
| **Monitoring & Alerting (Grafana, Prometheus)**       | Advanced monitoring setups with Prometheus/Grafana                        | ➖ Not listed                                                                                                 | **Gap** → Prepare to discuss general monitoring experience (e.g., database monitoring, performance metrics) and express intent to skill up     |
| **Data Security & Compliance**                        | Data security, access control, regulatory compliance knowledge            | ➖ Not explicitly covered                                                                                     | **Gap** → Think about past experience with GDPR-sensitive data or secured environments and frame it                                            |
| **C++ Contributions**                                 | (Bonus) Enhance ClickHouse with C++                                       | ➖ Rust and Java experience, but no C++                                                                       | **Gap** → Be transparent but emphasize Rust (very close to C++) skills and ability to pick up C++                                              |
| **Star Schema / Data Modeling**                       | Analytical data models and warehouse design (star schema)                 | ✔️ Built complex pipelines, optimized query performance                                                      | ✅ Match                                                                                                                                        |
| **Soft Skills (Communication, Teamwork)**             | Strong collaboration, mentoring, and cross-team work                      | ✔️ Mentored 5 engineers, senior code reviewer                                                                | ✅ Strong match                                                                                                                                 |
| **Sustainability & Ethical Values Alignment**         | Responsiveness, Creativity, Commitment, Ambition (BNP core values)​       | ✔️ Open-source enthusiasm, proactive problem-solving, leadership in driving improvements                     | ✅ Values align naturally                                                                                                                       |
| **Mission Fit (Responsible Banking, Sustainability)** | Demonstrated commitment to sustainable, ethical practices                 | ➖ Not directly mentioned                                                                                     | **Soft gap** → Prepare to talk about interest in sustainable tech, ethical data handling, and how BNP’s mission resonates with you             |

## Probable questions around the gap

### 1. Backup & Disaster Recovery Strategy - In your previous experience migrating to ClickHouse, how did you approach backup and disaster recovery? Can you describe a backup strategy you have implemented or would propose for a distributed database like ClickHouse?
**Answer:**
In my recent migration from MongoDB to ClickHouse at SecurityHQ, I prioritized data durability and business continuity. For MongoDB, I implemented automated backups using Ops Manager. For ClickHouse, I automated regular backups to S3 using the MongoDB Ops Manager. ClickHouse's built-in tools, documented restore procedures, and tested recovery scenarios. My approach for a distributed ClickHouse cluster would include:
- Scheduled full and incremental backups to object storage (e.g., S3)
- Use of ReplicatedMergeTree tables for redundancy
- Automated restore testing and clear documentation
- Regular disaster recovery drills
- Monitoring backup job status and alerting on failures
I believe regular testing and documentation are as important as the backup process itself, and I am comfortable adapting best practices from MongoDB to ClickHouse’s distributed architecture.

| ReplicatedMergeTree Table                                                                                                  | Distributed Table                                                                                                                                       |
| -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| A storage engine that provides automatic data replication across multiple nodes for fault tolerance and high availability. | A logical table that routes queries and inserts to underlying tables (often MergeTree or ReplicatedMergeTree) on multiple nodes (shards) in a cluster.​ |
| Each replica stores a full copy of the table’s data and synchronizes changes using ZooKeeper or ClickHouse Keeper.         | Does not store data itself; it acts as a proxy for sharding and parallel query execution.                                                               |
| Used for ensuring data durability and consistency within a shard.                                                          | Used for horizontal scaling and distributing data across shards.                                                                                        |

### 2. High Availability & Fault Tolerance - Have you designed or operated a highly available or fault-tolerant database system? How would you design a fault-tolerant ClickHouse cluster?
**Answer:**
I have designed and managed a sharded, replicated MongoDB cluster (4 shards, 2 replicas each, 12 nodes) to ensure high availability and fault tolerance. For ClickHouse, I would design a cluster with multiple replicas per shard, distributed across availability zones, and use ClickHouse Keeper for coordination. I would implement:
- ReplicatedMergeTree tables for data redundancy
- Sharding for scalability
- Automated failover and health checks
- Regular failover and recovery testing
- Monitoring of node health and replication lag
My experience with high-throughput pipelines (10TB/week) has given me a strong foundation in reliability engineering, and I am actively learning ClickHouse Keeper and advanced cluster management.

### 3. Monitoring & Observability - Can you walk me through how you monitored database systems in production? Have you had any exposure to tools like Prometheus or Grafana? If not, how would you approach monitoring ClickHouse metrics?
**Answer:**
I have set up monitoring and alerting for MongoDB using Ops Manager, configuring alerts for resource usage and failures. For ClickHouse, I implemented monitoring with built-in dashboards and Grafana, tracking key metrics and configuring alerts for critical thresholds. While I have not used Prometheus directly, I am familiar with its concepts and can quickly skill up. My approach would be to:
- Expose ClickHouse metrics via exporters
- Set up Grafana dashboards for visualization
- Configure actionable alerts for key performance and health indicators
- Use logs and structured logging for troubleshooting
Proactive monitoring and clear alerting are vital for maintaining high service levels.

### 4. DevOps (Jenkins, Ansible) Familiarity - "I see you have CI/CD experience with GitHub Actions. How would you adapt your CI/CD knowledge to Jenkins and Ansible if you were tasked with integrating ClickHouse deployments?"
**Answer:**
I have built and maintained CI/CD pipelines using GitHub Actions for Airflow DAG deployments and database schema migrations. The core principles of CI/CD—automation, repeatability, and version control—are transferable across tools. I am confident I can adapt quickly to Jenkins and Ansible by leveraging my scripting and automation skills. I would:
- Map existing workflows to Jenkins pipelines
- Use Ansible for infrastructure provisioning and configuration management
- Ensure robust and automated ClickHouse deployments
- Document and share best practices with the team
I am eager to learn new DevOps tools and have a proven track record of quickly adopting new technologies.

### 5. C++ or Systems Programming Background - We value candidates who can extend ClickHouse functionality at a low level. Given your experience with Rust and Java, how comfortable are you transitioning to C++ if needed?
**Answer:**
While I have not worked professionally with C++, I have strong systems programming experience in Rust and Java. Rust’s memory management and concurrency paradigms are very close to C++. I am actively learning C++ fundamentals and am confident in my ability to pick up C++ quickly if required. I have contributed to open-source projects in Python, Java, and Rust (see my GitHub), and I am eager to contribute to ClickHouse at the code level as my C++ skills mature.

### 6. Data Security, Access Control, Compliance - Have you worked on systems requiring data security, GDPR compliance, or strict access controls? How do you ensure secure data handling in your pipelines?
**Answer:**
I have worked with sensitive data in financial and government sectors, where data security and compliance are paramount. I ensure secure data handling by:
- Implementing access controls and least-privilege principles
- Encrypting data at rest and in transit
- Using AWS Secrets Manager for credential management
- Auditing access logs and following industry best practices
- Regularly reviewing and updating security policies
I am familiar with GDPR principles and always prioritize data minimization, auditability, and secure processing in my pipeline designs.

### 7. Sustainability and Ethical Impact - BNP Paribas emphasizes responsible banking and sustainability. How do you see your technical work contributing to a more sustainable and ethical data environment?
**Answer:**
I am passionate about building efficient, cost-effective, and sustainable data solutions. My migration from MongoDB to ClickHouse reduced infrastructure costs by 80% and improved resource utilization. I believe in ethical data handling, transparency, and supporting open-source initiatives. BNP Paribas’s mission of responsible banking resonates with me, and I am committed to aligning my work with sustainability and ethical best practices. I actively follow industry trends in sustainable tech and am motivated to contribute to BNP Paribas’s goals.

### 8. Monitoring Production Incidents - Have you ever handled a production incident related to a database? If so, how did you detect it, respond to it, and prevent recurrence?
**Answer:**
Yes, I have managed production incidents involving database performance and availability. I detected issues through monitoring tools and alerting systems, performed root cause analysis using logs and metrics, and coordinated with stakeholders for resolution. I documented incidents, implemented preventive measures (e.g., improved monitoring, automated failover), and shared learnings with the team to avoid recurrence. Staying calm, methodical, and communicative is vital in high-pressure situations.