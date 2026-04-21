---
services:
  - AWS AppSync
  - AWS Backup
  - AWS CloudTrail
  - AWS Config
  - AWS DataSync
  - AWS Glue
  - AWS IAM
  - AWS IoT Core
  - AWS Lambda
  - AWS Step Functions
  - AWS Storage Gateway
  - AWS Transfer Family
  - AWS WAF
  - Amazon AppFlow
  - Amazon Athena
  - Amazon Aurora
  - Amazon Bedrock
  - Amazon CloudWatch
  - Amazon DynamoDB
  - Amazon EBS
  - Amazon EC2
  - Amazon EFS
  - Amazon EMR
  - Amazon EventBridge
  - Amazon FSx
  - Amazon Inspector
  - Amazon Kinesis
  - Amazon MQ
  - Amazon Macie
  - Amazon Managed Service for Apache Flink
  - Amazon OpenSearch Service
  - Amazon QuickSight
  - Amazon RDS
  - Amazon Redshift
  - Amazon Route 53
  - Amazon S3
  - Amazon SNS
  - Amazon SQS
  - Amazon SageMaker
  - Amazon Timestream
  - Amazon VPC
tags: ['aws', 'general']
status: atomic
topic: AWS Data Engineering
domain: Exam Prep
created_at: 2025-12-24
---
## AWS Services Comparison

###  Active Recall
- What is the primary difference between a [[Public vs Private AWS Services|Public]] and a [[Public vs Private AWS Services|Private]] service?
- Which services are considered "Hybrid"?
- How does the access method (Public Endpoint vs VPC Subnet) affect security design?

---

| Service | Category | Justification |
| --- | --- | --- |
| Amazon [[EC2]] | Private | Instances are launched into [[VPC Networking Fundamentals|VPC]] subnets with private IPs. Public access is optional via Internet Gateway. |
| AWS [[Lambda]] | [[Public vs Private AWS Services|Public]] | Functions run in a managed service [[VPC Networking Fundamentals|VPC]]. Triggers/API are public. Can attach to customer [[VPC Networking Fundamentals|VPC]] for outbound access. |
| Amazon ECS | Private | Container instances ([[EC2]]) or Fargate tasks run within [[VPC Networking Fundamentals|VPC]] subnets. |
| Amazon EKS | Private | Kubernetes nodes and Fargate profiles run within [[VPC Networking Fundamentals|VPC]] subnets. |
| AWS Fargate | Private | Serverless compute engine that runs tasks/pods within [[VPC Networking Fundamentals|VPC]] subnets. |
| AWS Batch | Private | Provisions compute environments ([[EC2]]/Fargate) within [[VPC Networking Fundamentals|VPC]] subnets. |
| AWS Elastic Beanstalk | Private | Provisions underlying infrastructure ([[EC2]], [[RDS and Aurora Fundamentals|RDS]], ELB) into [[VPC Networking Fundamentals|VPC]] subnets. |
| Amazon Lightsail | [[Public vs Private AWS Services|Public]] | Simplified cloud platform. Instances have public IPs by default; [[VPC Networking Fundamentals|VPC]] implementation is abstracted/peered. |
| AWS App Runner | [[Public vs Private AWS Services|Public]] | PaaS. Service is accessed via public URL. can connect to [[VPC Networking Fundamentals|VPC]] for private resource access. |
| AWS Outposts | Hybrid | Extends AWS infrastructure to on-premises. Connects back to Region via private link. |
| AWS Wavelength | Hybrid | Compute/Storage embedded in 5G networks. Connected to [[VPC Networking Fundamentals|VPC]]. |
| AWS Local Zones | Hybrid | Extensions of Regions. Resources (subnets) are part of the [[VPC Networking Fundamentals|VPC]]. |
| AWS Serverless Application Repository | [[Public vs Private AWS Services|Public]] | Repository for deploying serverless apps via public endpoints. |
| Amazon [[S3 Fundamentals|S3]] | [[Public vs Private AWS Services|Public]] | Global namespace. Buckets are accessed via public HTTPS endpoints. Private access via Gateway/Interface Endpoints. |
| Amazon EFS Fundamentals | Private | File systems are accessed via Mount Targets (ENIs) in [[VPC Networking Fundamentals|VPC]] subnets. |
| Amazon EBS Fundamentals | Private | Block storage volumes attached to [[EC2]] instances within a [[VPC Networking Fundamentals|VPC]]. |
| Amazon FSx (all types) | Private | File systems (Windows, Lustre, NetApp, OpenZFS) provisioned with ENIs in [[VPC Networking Fundamentals|VPC]] subnets. |
| AWS Storage Gateway | Hybrid | Appliance deployed on-prem or in [[VPC Networking Fundamentals|VPC]]. Connects to [[Public vs Private AWS Services|public service endpoints]]. |
| AWS [[Backup]] | [[Public vs Private AWS Services|Public]] | Control plane is public. Backs up resources which may be private. |
| AWS Elastic Disaster Recovery (DRS) | Private | Replication servers run in a staging area ([[VPC Networking Fundamentals|VPC]]). |
| Amazon [[RDS and Aurora Fundamentals|RDS]] | Private | DB instances are provisioned into [[VPC Networking Fundamentals|VPC]] subnets. |
| Amazon Aurora | Private | DB clusters are provisioned into [[VPC Networking Fundamentals|VPC]] subnets. |
| Amazon [[DynamoDB Capacity Modes|DynamoDB]] | [[Public vs Private AWS Services|Public]] | Serverless NoSQL. Accessed via public HTTPS endpoints. Private access via Gateway Endpoint. |
| Amazon ElastiCache | Private | Cache clusters (Redis/Memcached) provisioned into [[VPC Networking Fundamentals|VPC]] subnets. |
| Amazon MemoryDB | Private | Redis-compatible, durable database provisioned into [[VPC Networking Fundamentals|VPC]] subnets. |
| Amazon [[Redshift Data Loading COPY|Redshift]] | Private | Data warehouse clusters provisioned into [[VPC Networking Fundamentals|VPC]] subnets. |
| Amazon DocumentDB | Private | MongoDB-compatible clusters deployed within [[VPC Networking Fundamentals|VPC]] subnets. |
| Amazon Neptune | Private | Graph database clusters deployed within [[VPC Networking Fundamentals|VPC]] subnets. |
| Amazon Keyspaces | [[Public vs Private AWS Services|Public]] | Serverless Cassandra. Accessed via public endpoints (or Interface Endpoints). |
| Amazon [[Timestream]] | [[Public vs Private AWS Services|Public]] | Serverless time-series DB. Accessed via public endpoints. |
| Amazon [[VPC Networking Fundamentals|VPC]] | Private | The fundamental isolated network container. |
| Amazon CloudFront | [[Public vs Private AWS Services|Public]] | Global CDN with public edge locations. |
| [[Route 53]] | [[Public vs Private AWS Services|Public]] | Global DNS service accessed via public endpoints. |
| Amazon API Gateway | [[Public vs Private AWS Services|Public]] | APIs are public by default. "Private APIs" are accessible only from within a [[VPC Networking Fundamentals|VPC]] (via endpoint). |
| AWS Direct Connect | Private | Physical private dedicated network connection. |
| AWS Global Accelerator | [[Public vs Private AWS Services|Public]] | Provides static public IPs as entry points to endpoints (which can be private). |
| Elastic Load Balancing (ALB/NLB/GLB) | Private | Load Balancers are deployed into [[VPC Networking Fundamentals|VPC]] subnets (though they can be "Internet-facing"). |
| AWS PrivateLink | Private | Technology to access services privately within [[VPC Networking Fundamentals|VPC]] via Interface Endpoints. |
| AWS Transit Gateway | Private | Regional network hub connecting VPCs and on-prem networks. |
| Amazon VPC Lattice | Private | Application networking service connecting services across VPCs/accounts. |
| AWS Cloud Map | Private | Service discovery resources (namespaces) often map to [[VPC Networking Fundamentals|VPC]] private DNS. |
| AWS Client VPN | Private | VPN endpoints enable secure connections into [[VPC Networking Fundamentals|VPC]] subnets. |
| AWS Site-to-Site VPN | Private | Connects on-prem networks to VPCs (Virtual Private Gateway/Transit Gateway). |
| AWS Cloud WAN | Global/Private | Manages a global core network connecting VPCs and on-prem environments. |
| AWS Verified Access | [[Public vs Private AWS Services|Public]] | Provides secure access to corporate applications without a VPN (Zero Trust). Control plane is public. |
| AWS [[AWS IAM]] | [[Public vs Private AWS Services|Public]] | Global identity service accessed via public endpoints. |
| AWS KMS | [[Public vs Private AWS Services|Public]] | Key management accessed via public endpoints. |
| AWS Secrets Manager | [[Public vs Private AWS Services|Public]] | Secrets management accessed via public endpoints. |
| AWS [[WAF]] | [[Public vs Private AWS Services|Public]] | Web Application Firewall protecting public endpoints. |
| AWS Shield | [[Public vs Private AWS Services|Public]] | DDoS protection for public endpoints. |
| AWS Certificate Manager (ACM) | [[Public vs Private AWS Services|Public]] | Provisions certificates. Validated via DNS (public) or Email. |
| Amazon [[Inspector]] | [[Public vs Private AWS Services|Public]] | Vulnerability management. Scans resources (agents/snapshots). Control plane is public. |
| Amazon GuardDuty | [[Public vs Private AWS Services|Public]] | Threat detection service. Control plane is public. |
| Amazon [[Macie]] | [[Public vs Private AWS Services|Public]] | Data security/privacy for [[S3 Fundamentals|S3]]. Control plane is public. |
| AWS Security Hub | [[Public vs Private AWS Services|Public]] | CSPM service. Control plane is public. |
| Amazon Detective | [[Public vs Private AWS Services|Public]] | Security investigation. Control plane is public. |
| AWS Audit Manager | [[Public vs Private AWS Services|Public]] | Compliance auditing. Control plane is public. |
| AWS Signer | [[Public vs Private AWS Services|Public]] | Code signing service. Control plane is public. |
| AWS Private CA | [[Public vs Private AWS Services|Public]] | Certificate Authority service. Control plane is public (but certs often used privately). |
| AWS Network Firewall | Private | Managed firewall endpoints deployed into [[VPC Networking Fundamentals|VPC]] subnets. |
| AWS Resource Access Manager (RAM) | [[Public vs Private AWS Services|Public]] | Resource sharing service. Control plane is public. |
| Amazon Cognito | [[Public vs Private AWS Services|Public]] | Identity pools/User pools accessed via public endpoints. |
| Amazon Verified Permissions | [[Public vs Private AWS Services|Public]] | Permission management. Control plane is public. |
| AWS Directory Service | Private | Microsoft AD/Simple AD domain controllers are provisioned into [[VPC Networking Fundamentals|VPC]] subnets (ENIs). |
| AWS [[AWS IAM]] Identity Center | [[Public vs Private AWS Services|Public]] | (Formerly SSO) Global/Regional control plane accessed via public endpoints. |
| AWS Payment Cryptography | Private | Dedicated HSM service accessed primarily via Interface [[VPC Networking Fundamentals|VPC]] Endpoints. |
| AWS CloudHSM | Private | Hardware Security Modules provisioned into [[VPC Networking Fundamentals|VPC]] subnets. |
| Amazon CloudWatch | [[Public vs Private AWS Services|Public]] | Metrics/Logs sent to public endpoints. [[VPC Networking Fundamentals|VPC]] Endpoints available. |
| AWS CloudTrail | [[Public vs Private AWS Services|Public]] | Auditing service. Logs delivered to [[S3 Fundamentals|S3]]/CloudWatch. |
| AWS [[Config]] | [[Public vs Private AWS Services|Public]] | Configuration tracking. Control plane is public. |
| AWS Systems Manager | [[Public vs Private AWS Services|Public]] | Agents connect to public endpoints (SSM). [[VPC Networking Fundamentals|VPC]] Endpoints recommended for private instances. |
| AWS Service Catalog | [[Public vs Private AWS Services|Public]] | Service management. Control plane is public. |
| AWS Control Tower | [[Public vs Private AWS Services|Public]] | Multi-account governance. Control plane is public. |
| AWS Organizations | [[Public vs Private AWS Services|Public]] | Account management. Global service. |
| AWS Trusted Advisor | [[Public vs Private AWS Services|Public]] | Optimization recommendations. Control plane is public. |
| AWS Health | [[Public vs Private AWS Services|Public]] | Status information. Control plane is public. |
| AWS License Manager | [[Public vs Private AWS Services|Public]] | License tracking. Control plane is public. |
| Amazon Managed Grafana | [[Public vs Private AWS Services|Public]] | Visualization service. Accessed via public URL (SAML/SSO). |
| Amazon Managed Prometheus | [[Public vs Private AWS Services|Public]] | Metrics storage. Accessed via [[Public vs Private AWS Services|public endpoint]] (Remote Write). |
| AWS CloudShell | [[Public vs Private AWS Services|Public]] | Browser-based shell. Accessed via public Console URL. |
| AWS Resilience Hub | [[Public vs Private AWS Services|Public]] | Assessment service that scans resources. Control plane is public. |
| AWS Chatbot | [[Public vs Private AWS Services|Public]] | Integrates AWS notifications with Slack/Chime (SaaS). |
| AWS User Notifications | [[Public vs Private AWS Services|Public]] | Notification center. Control plane is public. |
| AWS Telco Network Builder | Private | Deploys network functions into VPCs. |
| Amazon [[AWS Data Engineer Zettelkasten Lite style/Athena]] | [[Public vs Private AWS Services|Public]] | Serverless query service. Accessed via public endpoints. |
| AWS [[AWS Glue Fundamentals|Glue]] | [[Public vs Private AWS Services|Public]] | Serverless ETL. Jobs run in managed [[VPC Networking Fundamentals|VPC]] (can attach to customer [[VPC Networking Fundamentals|VPC]]). API is public. |
| Amazon [[EMR Fundamentals|EMR]] | Private | Clusters ([[EC2]]-based) provisioned into [[VPC Networking Fundamentals|VPC]] subnets. |
| Amazon [[Kinesis Data Streams]] | [[Public vs Private AWS Services|Public]] | Real-time data streaming. Accessed via public endpoints. |
| Amazon [[Kinesis Data Firehose]] | [[Public vs Private AWS Services|Public]] | Data delivery service. Accessed via public endpoints. |
| Amazon Managed Streaming for Apache Kafka (MSK) | Private | Kafka brokers provisioned into [[VPC Networking Fundamentals|VPC]] subnets. |
| Amazon [[Managed Service for Apache Flink]] | [[Public vs Private AWS Services|Public]] | Serverless stream processing engine. Accessed via public endpoints. Runs in managed [[VPC Networking Fundamentals|VPC]]. |
| Amazon OpenSearch Service | Private | Domains typically deployed into [[VPC Networking Fundamentals|VPC]] subnets. |
| Amazon [[QuickSight]] | [[Public vs Private AWS Services|Public]] | Business Intelligence service. Accessed via public internet/browser. |
| AWS Clean Rooms | [[Public vs Private AWS Services|Public]] | Data collaboration. Control plane is public. |
| AWS Entity Resolution | [[Public vs Private AWS Services|Public]] | Data matching. Control plane is public. |
| Amazon CloudSearch | [[Public vs Private AWS Services|Public]] | (Legacy) Search domains have public endpoints by default. |
| AWS Data Exchange | [[Public vs Private AWS Services|Public]] | Marketplace for data. Control plane is public. |
| Amazon [[SageMaker]] | Hybrid | Notebooks/Training run in [[VPC Networking Fundamentals|VPC]]. APIs are public. Endpoints can be private (PrivateLink). |
| Amazon [[Bedrock]] | [[Public vs Private AWS Services|Public]] | Serverless GenAI. Accessed via public API endpoints. |
| Amazon Rekognition | [[Public vs Private AWS Services|Public]] | Image/Video analysis. Accessed via public API endpoints. |
| Amazon Polly | [[Public vs Private AWS Services|Public]] | Text-to-Speech. Accessed via public API endpoints. |
| Amazon Translate | [[Public vs Private AWS Services|Public]] | Translation. Accessed via public API endpoints. |
| Amazon Transcribe | [[Public vs Private AWS Services|Public]] | Speech-to-Text. Accessed via public API endpoints. |
| Amazon Comprehend | [[Public vs Private AWS Services|Public]] | NLP. Accessed via public API endpoints. |
| Amazon Textract | [[Public vs Private AWS Services|Public]] | OCR. Accessed via public API endpoints. |
| Amazon Personalize | [[Public vs Private AWS Services|Public]] | Recommendation engine. Accessed via public API endpoints. |
| Amazon Lex | [[Public vs Private AWS Services|Public]] | Conversational AI. Accessed via public API endpoints. |
| Amazon Q | [[Public vs Private AWS Services|Public]] | Generative AI assistant (Business/Developer) accessed via public interface/IDE. |
| Amazon [[SQS]] | [[Public vs Private AWS Services|Public]] | Message queuing. Accessed via public HTTPS endpoints. |
| Amazon SNS | [[Public vs Private AWS Services|Public]] | Pub/Sub messaging. Accessed via public HTTPS endpoints. |
| AWS Step Functions | [[Public vs Private AWS Services|Public]] | Workflow orchestration. Accessed via public HTTPS endpoints. |
| Amazon EventBridge | [[Public vs Private AWS Services|Public]] | Event bus. Accessed via public HTTPS endpoints. |
| [[Amazon MQ]] | Private | Managed ActiveMQ/RabbitMQ brokers provisioned into [[VPC Networking Fundamentals|VPC]] subnets. |
| AWS AppSync | [[Public vs Private AWS Services|Public]] | GraphQL API. Accessed via public endpoints. |
| Amazon Simple Workflow (SWF) | [[Public vs Private AWS Services|Public]] | Workflow service. Accessed via public endpoints. |
| Amazon [[AppFlow]] | [[Public vs Private AWS Services|Public]] | SaaS integration. Accessed via public endpoints. |
| AWS CodeBuild | [[Public vs Private AWS Services|Public]] | Build service. Runs in managed environment (can access [[VPC Networking Fundamentals|VPC]]). API is public. |
| AWS CodeDeploy | [[Public vs Private AWS Services|Public]] | Deployment service. Control plane is public. Agents on instances pull commands. |
| AWS CodePipeline | [[Public vs Private AWS Services|Public]] | CI/CD orchestration. Accessed via public endpoints. |
| AWS X-Ray | [[Public vs Private AWS Services|Public]] | Tracing service. Data sent to public endpoints. |
| AWS Fault Injection Service (FIS) env | [[Public vs Private AWS Services|Public]] | Chaos engineering. Control plane is public. |
| AWS Cloud9 | Hybrid | IDE runs on [[EC2]] (Private/[[VPC Networking Fundamentals|VPC]]) but accessed via Browser (Public/Relay). |
| Amazon CodeCatalyst | [[Public vs Private AWS Services|Public]] | Unified software development service (SaaS) accessed via public endpoints. |
| Amazon Corretto | [[Public vs Private AWS Services|Public]] | Distribution of OpenJDK (Software download/artifact). |
| AWS Amplify | [[Public vs Private AWS Services|Public]] | Hosting/Backend-as-a-Service. Accessed via public endpoints/CDNs. |
| AWS Device Farm | [[Public vs Private AWS Services|Public]] | App testing. Accessed via public endpoints. |
| Amazon Location Service | [[Public vs Private AWS Services|Public]] | Maps/Geofencing. Accessed via public endpoints. |
| AWS Elemental MediaConvert | [[Public vs Private AWS Services|Public]] | File-based transcoding. Accessed via public endpoints. |
| AWS Elemental MediaLive | [[Public vs Private AWS Services|Public]] | Live video processing. Accessed via public endpoints. |
| AWS Elemental MediaConnect | [[Public vs Private AWS Services|Public]] | Live video transport. Accessed via public endpoints (flows). |
| AWS Elemental MediaPackage v2 | [[Public vs Private AWS Services|Public]] | Video packaging. Accessed via public endpoints. |
| AWS Elemental MediaTailor | [[Public vs Private AWS Services|Public]] | Ad insertion. Accessed via public endpoints. |
| Amazon Interactive Video Service (IVS) | [[Public vs Private AWS Services|Public]] | Managed live streaming. Accessed via public endpoints. |
| Amazon Simple Email Service (SES) | [[Public vs Private AWS Services|Public]] | Email sending/receiving service accessed via public API/SMTP endpoints. |
| AWS End User Messaging | [[Public vs Private AWS Services|Public]] | (Successor to some Pinpoint features) SMS/Push APIs are public. |
| AWS [[IoT Core]] | [[Public vs Private AWS Services|Public]] | Device gateway. Accessed via public MQTT/HTTPS endpoints. |
| AWS IoT Device Management | [[Public vs Private AWS Services|Public]] | Fleet management. Control plane is public. |
| AWS IoT TwinMaker | [[Public vs Private AWS Services|Public]] | Digital twins. Control plane is public. |
| AWS IoT FleetWise | [[Public vs Private AWS Services|Public]] | Vehicle data. Control plane is public. |
| AWS IoT SiteWise | Hybrid | Edge gateways run on-prem; Cloud data storage accessed via public or [[VPC Networking Fundamentals|VPC]] endpoints. |
| AWS IoT 1-Click | [[Public vs Private AWS Services|Public]] | Simple device triggers accessed via public endpoints. |
| AWS Database Migration Service (DMS) | Private | Replication instances provisioned into [[VPC Networking Fundamentals|VPC]] subnets. |
| AWS DataSync | Hybrid | Agent (on-prem/[[VPC Networking Fundamentals|VPC]]) connects to [[Public vs Private AWS Services|public service endpoints]]. |
| AWS Transfer Family | Hybrid | SFTP/FTP endpoints. Can be Public (Elastic IP) or Private ([[VPC Networking Fundamentals|VPC]] Endpoint). |
| AWS Application Migration Service (MGN) | Private | Replication servers run in staging area ([[VPC Networking Fundamentals|VPC]]). |
| AWS Mainframe Modernization | Private | Runtime environments are provisioned into [[VPC Networking Fundamentals|VPC]] subnets. |
| AWS Migration Hub | [[Public vs Private AWS Services|Public]] | Tracking and orchestration service. Control plane is public. |
| Amazon GameLift | Hybrid | Game server fleets run in [[VPC Networking Fundamentals|VPC]] (managed). Service API is public. |
| AWS RoboMaker | [[Public vs Private AWS Services|Public]] | Simulation jobs run in managed [[VPC Networking Fundamentals|VPC]]. |
| AWS Ground Station | [[Public vs Private AWS Services|Public]] | Satellite data delivered to [[S3 Fundamentals|S3]] or [[EC2]] ([[VPC Networking Fundamentals|VPC]]). |
| Amazon Braket | [[Public vs Private AWS Services|Public]] | Quantum computing. Jobs managed via public API. |
| Amazon Connect | [[Public vs Private AWS Services|Public]] | Cloud-based contact center service (SaaS-like). Accessed via public HTTPS endpoints. |
| Amazon Chime SDK | [[Public vs Private AWS Services|Public]] | Communication APIs accessed via public endpoints. |
| AWS Wickr | [[Public vs Private AWS Services|Public]] | Encrypted communication service (SaaS) accessed via public internet. |
| AWS Supply Chain | [[Public vs Private AWS Services|Public]] | SaaS application accessed via public endpoints. |
| Amazon WorkSpaces | Private | Desktops are provisioned into [[VPC Networking Fundamentals|VPC]] subnets. |
| Amazon AppStream 2.0 | Private | Streaming instances are provisioned into [[VPC Networking Fundamentals|VPC]] subnets. |
| Amazon WorkLink | Private | (Legacy but active) Grants access to internal websites via [[VPC Networking Fundamentals|VPC]]. |
| AWS HealthOmics | Private | Bioinformatics stores and workflows. Supports Interface [[VPC Networking Fundamentals|VPC]] Endpoints. |
| AWS HealthImaging | [[Public vs Private AWS Services|Public]] | Medical imaging storage. Accessed via public APIs. |
