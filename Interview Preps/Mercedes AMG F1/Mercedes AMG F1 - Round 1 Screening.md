## 1. Why are you interested in Mercedes AMG F1 and the role - Data Platform Engineer?

The story starts from 15 years ago when I discovered my interests - Mechanical Engineering and Computer Science. I was specifically interested in the automotive industry and I didn't really understand the distinction between automotive and motorsport industries back in the day but I always wanted to be a part of the motorsport industry. I have always been interested in both. As I progressed in my education I realized I have a stronger inclination towards Computer Science, which put me on the career path I am on right now. However, I've always felt the void of not following the other path. This opportunity blends both of my interests and this is not just a job for me. It is an emotion, a realization of a forgotten dream. This job presents me with an opportunity to contribute to one of the best F1 teams in the world. God knows I've worked 80 hours a week for lesser dreams and I am willing to give my best. 
My interest in this role is deeply personal and started long before I saw the job description. 

That’s why I’m so drawn to **Mercedes-AMG F1**. I have immense respect for high-performance engineering cultures where the standards are incredibly high. Mercedes represents the pinnacle of this. It’s clear your success comes from a culture of relentless innovation. For a data professional, an environment where data is the lifeblood of performance is the ultimate motivator.

And it's why this **Data Platform Engineer role** resonates so strongly. My expertise lies in architecting the 'how' behind the data—building the robust, scalable, and high-velocity platforms that enable analysis. This role isn't standard corporate warehousing; it’s about handling the complex data diversity from the factory and the track, and ensuring the unquestionable reliability of a platform where downtime is not an option. It's the challenge of building the central nervous system for the team's data strategy that excites me.

 
## 2. Tell me about yourself.

Worked with diverse sets of data coming from various SIEM tools, public APIs, proprietary applications, OLTP databases and data streams.
Architected data pipelines by writing Airflow DAGs and custom Python ETL pipelines in Python.
Example of combining data from multiple sources - 
Data enrichment for event logs coming from a real-time event log data stream from IBM QRadar  over Cribl Stream using data from Qualys, NVD and CriminalIP.
Created CI/CD workflows for the team so that we could use a paramterized Dockerfile based on which environment we are deploying the code to, enforcing coding best practices via precommit hooks and linting and formating code styles to identify soon to be deprecated functions. Integrated AI into everyday coding tasks using AI agents, MCP servers and created reusable dev containers for the wider organization.
Set up sharded MongoDB cluster in a self-hosted environment as a database administrator, optimized queries by looking at query execution plans. Deep knowledge of creating and mounting disks to partitions, expanding disks on ec2 instances without downtime. 
Created dashboards using BI as Code and PowerBI. Tableau Desktop Specialist.

At Amazon and at SecurityHQ I have taken the ownership of my work from Day 1. As I gained trust from the leaders I became comfortable pushing my own ideas and I made sure I have the technical expertise to back me up by upskilling ahead of time. 

Migrated database from MongoDB to ClickHouse Cloud using AWS DMS. Restructured the Data to conform to ClickHouse best practices, upskilled and identified areas of improvement to bring down the costs by 40%, effectively reducing costs by 90% in a span of 6 months, ensuring that costs won't increase linearly with the size of our data.

As Data Engineering function is a supporting function in SecrutiyHQ the requirements amd priorities were always shifting according to the bussiness and my team needed to be flexible enough to adapt and deliver in the accepted timelines.

ITIL - took up the project of migrating away from mongodb to clickhouse and conducted pocs demonstrating significant performance gains, new opportunities and cost reduction. Similarly migrated legacy Python ETL jobs to Airflow. Completed 2 projects in under a year - result was increased productivity for the team, less strain to review code as Airflow gave the team a framework + CI/CD was in place. Significantly lower costs and move to SQL means all of our analysts could extract all the insights they needed without the challenge of learning a new query language. With a modern data warehouse we under my technical guidance we are integrating openwebui + bedrock and mcp to provide on demand dashboards to our customers. 

Frequently broken CRON jobs were replaced iwth Airflow so on-shift engineers could now spend time on new integrations and understanding business requirements and creating documentation, setting correct expectations and delivering on time.

At Amazon, my foundations are all about performance and resource optimization because I learnt from a team of extremely talented people the skill of approaching a problem from an optimization perspective, was a part of the  DynamoDB meta data team where the workflows were highly methodical and sprint planning and retrospectives were hosted were the best I have seen so far. 

*****

##### Variety of Data Sources
I've had the chance to work with a really wide range of data—everything from SIEM tools and public APIs to proprietary apps, OLTP databases, and real-time data streams. A lot of my day-to-day involves architecting data pipelines using Airflow DAGs and custom Python scripts.

One example that stands out: we were working with real-time event log data coming in from IBM QRadar via Cribl Stream. I built an enrichment pipeline that pulled in threat intelligence from sources like Qualys, NVD, and CriminalIP to add more context to those logs.

On the dev side, I set up CI/CD workflows for our team with a parameterized Dockerfile setup—tailored for different environments. We enforced good coding practices through pre-commit hooks, linting, and formatting, and I integrated AI tooling using agents, MCP servers, and reusable dev containers. This made our whole workflow faster and smarter.

##### Working with Linux
As a database admin, I setup from scratch and managed a self-hosted, sharded MongoDB cluster—optimizing queries using execution plans, mounting and expanding disks on EC2 without downtime. I’ve also built dashboards using BI as Code, Power BI, and I’m certified in Tableau Desktop.

At both Amazon and SecurityHQ, I’ve taken ownership of my work from Day 1. As I earned trust, I felt confident pitching my own ideas and made sure I had the technical chops to support them—constantly learning and upskilling.

One project I’m really proud of was migrating our database from MongoDB to ClickHouse Cloud using AWS DMS. I restructured the data model based on ClickHouse best practices and helped the team cut costs by 40%—and eventually by 90% over six months. This was huge, especially since our data was scaling quickly, and we needed costs to stay flat.

Working in a support function at SecurityHQ, our priorities often shifted with business needs. We had to stay flexible and still hit deadlines, which really sharpened my ability to deliver under changing requirements.

At Amazon, I built a strong foundation in performance and resource optimization. I was part of the DynamoDB metadata team, where I learned to look at problems through an optimization lens. The team’s sprint planning and retrospectives were some of the most methodical and effective I’ve experienced, and that discipline still influences how I approach work today.

##### Data modelling

```mermaid
graph LR
    A(Bronze Layer) --> B(Silver Layer)
    B --> C(Gold Layer)
```

##### Proven ability to execute operations and changes within an ITIL environment.  

I led initiatives that significantly enhanced our data infrastructure. I spearheaded the migration from MongoDB to ClickHouse, including conducting POCs to validate performance gains, cost reduction, and scalability. These efforts demonstrated clear business value—improved query speed, reduced storage costs, and better resilience.

I also transitioned legacy ETL workflows to Airflow, establishing a standardized, observable, and fault-tolerant data orchestration system. This enhanced reliability, eliminated repetitive failures seen with cron jobs, and freed up our engineering team to focus on value-adding tasks like integrations, stakeholder communication, and documentation.

These projects embodied key ITIL practices, especially change management and service operation. By introducing a modern data warehouse and making analytics SQL-accessible, we improved service accessibility and enabled non-engineering teams to self-serve insights. Under my technical guidance, we began integrating AI tools like OpenWebUI and Bedrock through MCP to create on-demand, interactive dashboards—further aligning with ITIL’s emphasis on service value realization.

---

# Containerize an Application

1. **Create a Dockerfile**:
	- Use Python 3.11 slim image as base
	- Install Poetry for dependency management
	- Copy only necessary files (pyproject.toml, poetry.lock first)
	- Install dependencies via Poetry
	- Copy application code
	- Set up a non-root user for security
	- Define the entry point command
2. **Create docker-compose.yml**:
	- Define your application service
	- Include ClickHouse service if needed for local development
	- Set up environment variables via .env file
	- Configure volumes for persistent data
3. **Externalize Configuration**:
	- Move all credentials and connection details to environment variables
	- Create a template .env file with placeholders
4. **Build and Test**:
	- Build the Docker image
	- Test running a single console extraction
	- Verify data flows correctly
5. **Deployment Strategy**:
    - Use Airflow or Kubernetes CronJobs to schedule daily runs
    - Create separate jobs for each console
    - Stagger execution times to distribute load
6. **Monitoring and Logging**:
    - Configure container logging
    - Set up health checks
    - Implement alerting for failures