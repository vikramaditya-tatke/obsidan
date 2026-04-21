
| Service                                         | Category       | Justification                                                                                                      |
| ----------------------------------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------ |
| Amazon [[EC2]]                                  | Private        | Instances are launched into VPC subnets with private IPs. Public access is optional via Internet Gateway.          |
| AWS [[Lambda]]                                  | Public         | Functions run in a managed service VPC. Triggers/API are public. Can attach to customer VPC for outbound access.   |
| Amazon ECS                                      | Private        | Container instances (EC2) or Fargate tasks run within VPC subnets.                                                 |
| Amazon EKS                                      | Private        | Kubernetes nodes and Fargate profiles run within VPC subnets.                                                      |
| AWS Fargate                                     | Private        | Serverless compute engine that runs tasks/pods within VPC subnets.                                                 |
| AWS Batch                                       | Private        | Provisions compute environments (EC2/Fargate) within VPC subnets.                                                  |
| AWS Elastic Beanstalk                           | Private        | Provisions underlying infrastructure (EC2, RDS, ELB) into VPC subnets.                                             |
| Amazon Lightsail                                | Public         | Simplified cloud platform. Instances have public IPs by default; VPC implementation is abstracted/peered.          |
| AWS App Runner                                  | Public         | PaaS. Service is accessed via public URL. can connect to VPC for private resource access.                          |
| AWS Outposts                                    | Hybrid         | Extends AWS infrastructure to on-premises. Connects back to Region via private link.                               |
| AWS Wavelength                                  | Hybrid         | Compute/Storage embedded in 5G networks. Connected to VPC.                                                         |
| AWS Local Zones                                 | Hybrid         | Extensions of Regions. Resources (subnets) are part of the VPC.                                                    |
| AWS Serverless Application Repository           | Public         | Repository for deploying serverless apps via public endpoints.                                                     |
| Amazon S3                                       | Public         | Global namespace. Buckets are accessed via public HTTPS endpoints. Private access via Gateway/Interface Endpoints. |
| Amazon EFS                                      | Private        | File systems are accessed via Mount Targets (ENIs) in VPC subnets.                                                 |
| Amazon EBS                                      | Private        | Block storage volumes attached to EC2 instances within a VPC.                                                      |
| Amazon FSx (all types)                          | Private        | File systems (Windows, Lustre, NetApp, OpenZFS) provisioned with ENIs in VPC subnets.                              |
| AWS Storage Gateway                             | Hybrid         | Appliance deployed on-prem or in VPC. Connects to public service endpoints.                                        |
| AWS Backup                                      | Public         | Control plane is public. Backs up resources which may be private.                                                  |
| AWS Elastic Disaster Recovery (DRS)             | Private        | Replication servers run in a staging area (VPC).                                                                   |
| Amazon RDS                                      | Private        | DB instances are provisioned into VPC subnets.                                                                     |
| Amazon Aurora                                   | Private        | DB clusters are provisioned into VPC subnets.                                                                      |
| Amazon DynamoDB                                 | Public         | Serverless NoSQL. Accessed via public HTTPS endpoints. Private access via Gateway Endpoint.                        |
| Amazon ElastiCache                              | Private        | Cache clusters (Redis/Memcached) provisioned into VPC subnets.                                                     |
| Amazon MemoryDB                                 | Private        | Redis-compatible, durable database provisioned into VPC subnets.                                                   |
| Amazon [[Redshift]]                             | Private        | Data warehouse clusters provisioned into VPC subnets.                                                              |
| Amazon DocumentDB                               | Private        | MongoDB-compatible clusters deployed within VPC subnets.                                                           |
| Amazon Neptune                                  | Private        | Graph database clusters deployed within VPC subnets.                                                               |
| Amazon Keyspaces                                | Public         | Serverless Cassandra. Accessed via public endpoints (or Interface Endpoints).                                      |
| Amazon Timestream                               | Public         | Serverless time-series DB. Accessed via public endpoints.                                                          |
| Amazon [[VPC]]                                  | Private        | The fundamental isolated network container.                                                                        |
| Amazon CloudFront                               | Public         | Global CDN with public edge locations.                                                                             |
| Amazon Route 53                                 | Public         | Global DNS service accessed via public endpoints.                                                                  |
| Amazon API Gateway                              | Public         | APIs are public by default. "Private APIs" are accessible only from within a VPC (via endpoint).                   |
| AWS Direct Connect                              | Private        | Physical private dedicated network connection.                                                                     |
| AWS Global Accelerator                          | Public         | Provides static public IPs as entry points to endpoints (which can be private).                                    |
| Elastic Load Balancing (ALB/NLB/GLB)            | Private        | Load Balancers are deployed into VPC subnets (though they can be "Internet-facing").                               |
| AWS PrivateLink                                 | Private        | Technology to access services privately within VPC via Interface Endpoints.                                        |
| AWS Transit Gateway                             | Private        | Regional network hub connecting VPCs and on-prem networks.                                                         |
| Amazon VPC Lattice                              | Private        | Application networking service connecting services across VPCs/accounts.                                           |
| AWS Cloud Map                                   | Private        | Service discovery resources (namespaces) often map to VPC private DNS.                                             |
| AWS Client VPN                                  | Private        | VPN endpoints enable secure connections into VPC subnets.                                                          |
| AWS Site-to-Site VPN                            | Private        | Connects on-prem networks to VPCs (Virtual Private Gateway/Transit Gateway).                                       |
| AWS Cloud WAN                                   | Global/Private | Manages a global core network connecting VPCs and on-prem environments.                                            |
| AWS Verified Access                             | Public         | Provides secure access to corporate applications without a VPN (Zero Trust). Control plane is public.              |
| AWS IAM                                         | Public         | Global identity service accessed via public endpoints.                                                             |
| AWS KMS                                         | Public         | Key management accessed via public endpoints.                                                                      |
| AWS Secrets Manager                             | Public         | Secrets management accessed via public endpoints.                                                                  |
| AWS WAF                                         | Public         | Web Application Firewall protecting public endpoints.                                                              |
| AWS Shield                                      | Public         | DDoS protection for public endpoints.                                                                              |
| AWS Certificate Manager (ACM)                   | Public         | Provisions certificates. Validated via DNS (public) or Email.                                                      |
| Amazon Inspector                                | Public         | Vulnerability management. Scans resources (agents/snapshots). Control plane is public.                             |
| Amazon GuardDuty                                | Public         | Threat detection service. Control plane is public.                                                                 |
| Amazon Macie                                    | Public         | Data security/privacy for S3. Control plane is public.                                                             |
| AWS Security Hub                                | Public         | CSPM service. Control plane is public.                                                                             |
| Amazon Detective                                | Public         | Security investigation. Control plane is public.                                                                   |
| AWS Audit Manager                               | Public         | Compliance auditing. Control plane is public.                                                                      |
| AWS Signer                                      | Public         | Code signing service. Control plane is public.                                                                     |
| AWS Private CA                                  | Public         | Certificate Authority service. Control plane is public (but certs often used privately).                           |
| AWS Network Firewall                            | Private        | Managed firewall endpoints deployed into VPC subnets.                                                              |
| AWS Resource Access Manager (RAM)               | Public         | Resource sharing service. Control plane is public.                                                                 |
| Amazon Cognito                                  | Public         | Identity pools/User pools accessed via public endpoints.                                                           |
| Amazon Verified Permissions                     | Public         | Permission management. Control plane is public.                                                                    |
| AWS Directory Service                           | Private        | Microsoft AD/Simple AD domain controllers are provisioned into VPC subnets (ENIs).                                 |
| AWS IAM Identity Center                         | Public         | (Formerly SSO) Global/Regional control plane accessed via public endpoints.                                        |
| AWS Payment Cryptography                        | Private        | Dedicated HSM service accessed primarily via Interface VPC Endpoints.                                              |
| AWS CloudHSM                                    | Private        | Hardware Security Modules provisioned into VPC subnets.                                                            |
| Amazon CloudWatch                               | Public         | Metrics/Logs sent to public endpoints. VPC Endpoints available.                                                    |
| AWS CloudTrail                                  | Public         | Auditing service. Logs delivered to S3/CloudWatch.                                                                 |
| AWS Config                                      | Public         | Configuration tracking. Control plane is public.                                                                   |
| AWS Systems Manager                             | Public         | Agents connect to public endpoints (SSM). VPC Endpoints recommended for private instances.                         |
| AWS Service Catalog                             | Public         | Service management. Control plane is public.                                                                       |
| AWS Control Tower                               | Public         | Multi-account governance. Control plane is public.                                                                 |
| AWS Organizations                               | Public         | Account management. Global service.                                                                                |
| AWS Trusted Advisor                             | Public         | Optimization recommendations. Control plane is public.                                                             |
| AWS Health                                      | Public         | Status information. Control plane is public.                                                                       |
| AWS License Manager                             | Public         | License tracking. Control plane is public.                                                                         |
| Amazon Managed Grafana                          | Public         | Visualization service. Accessed via public URL (SAML/SSO).                                                         |
| Amazon Managed Prometheus                       | Public         | Metrics storage. Accessed via public endpoint (Remote Write).                                                      |
| AWS CloudShell                                  | Public         | Browser-based shell. Accessed via public Console URL.                                                              |
| AWS Resilience Hub                              | Public         | Assessment service that scans resources. Control plane is public.                                                  |
| AWS Chatbot                                     | Public         | Integrates AWS notifications with Slack/Chime (SaaS).                                                              |
| AWS User Notifications                          | Public         | Notification center. Control plane is public.                                                                      |
| AWS Telco Network Builder                       | Private        | Deploys network functions into VPCs.                                                                               |
| Amazon Athena                                   | Public         | Serverless query service. Accessed via public endpoints.                                                           |
| AWS Glue                                        | Public         | Serverless ETL. Jobs run in managed VPC (can attach to customer VPC). API is public.                               |
| Amazon EMR                                      | Private        | Clusters (EC2-based) provisioned into VPC subnets.                                                                 |
| Amazon Kinesis Data Streams                     | Public         | Real-time data streaming. Accessed via public endpoints.                                                           |
| Amazon Kinesis Data Firehose                    | Public         | Data delivery service. Accessed via public endpoints.                                                              |
| Amazon Managed Streaming for Apache Kafka (MSK) | Private        | Kafka brokers provisioned into VPC subnets.                                                                        |
| Amazon Managed Service for Apache Flink         | Public         | Serverless stream processing engine. Accessed via public endpoints. Runs in managed VPC.                           |
| Amazon OpenSearch Service                       | Private        | Domains typically deployed into VPC subnets (Public access optional but less common for enterprise).               |
| Amazon QuickSight                               | Public         | Business Intelligence service. Accessed via public internet/browser.                                               |
| AWS Clean Rooms                                 | Public         | Data collaboration. Control plane is public.                                                                       |
| AWS Entity Resolution                           | Public         | Data matching. Control plane is public.                                                                            |
| Amazon CloudSearch                              | Public         | (Legacy) Search domains have public endpoints by default (IP-based access policies).                               |
| AWS Data Exchange                               | Public         | Marketplace for data. Control plane is public.                                                                     |
| Amazon SageMaker                                | Hybrid         | Notebooks/Training run in VPC. APIs are public. Endpoints can be private (PrivateLink).                            |
| Amazon Bedrock                                  | Public         | Serverless GenAI. Accessed via public API endpoints.                                                               |
| Amazon Rekognition                              | Public         | Image/Video analysis. Accessed via public API endpoints.                                                           |
| Amazon Polly                                    | Public         | Text-to-Speech. Accessed via public API endpoints.                                                                 |
| Amazon Translate                                | Public         | Translation. Accessed via public API endpoints.                                                                    |
| Amazon Transcribe                               | Public         | Speech-to-Text. Accessed via public API endpoints.                                                                 |
| Amazon Comprehend                               | Public         | NLP. Accessed via public API endpoints.                                                                            |
| Amazon Textract                                 | Public         | OCR. Accessed via public API endpoints.                                                                            |
| Amazon Personalize                              | Public         | Recommendation engine. Accessed via public API endpoints.                                                          |
| Amazon Lex                                      | Public         | Conversational AI. Accessed via public API endpoints.                                                              |
| Amazon Q                                        | Public         | Generative AI assistant (Business/Developer) accessed via public interface/IDE.                                    |
| Amazon SQS                                      | Public         | Message queuing. Accessed via public HTTPS endpoints.                                                              |
| Amazon SNS                                      | Public         | Pub/Sub messaging. Accessed via public HTTPS endpoints.                                                            |
| AWS Step Functions                              | Public         | Workflow orchestration. Accessed via public HTTPS endpoints.                                                       |
| Amazon EventBridge                              | Public         | Event bus. Accessed via public HTTPS endpoints.                                                                    |
| Amazon MQ                                       | Private        | Managed ActiveMQ/RabbitMQ brokers provisioned into VPC subnets.                                                    |
| AWS AppSync                                     | Public         | GraphQL API. Accessed via public endpoints.                                                                        |
| Amazon Simple Workflow (SWF)                    | Public         | Workflow service. Accessed via public endpoints.                                                                   |
| Amazon AppFlow                                  | Public         | SaaS integration. Accessed via public endpoints.                                                                   |
| AWS CodeBuild                                   | Public         | Build service. Runs in managed environment (can access VPC). API is public.                                        |
| AWS CodeDeploy                                  | Public         | Deployment service. Control plane is public. Agents on instances pull commands.                                    |
| AWS CodePipeline                                | Public         | CI/CD orchestration. Accessed via public endpoints.                                                                |
| AWS X-Ray                                       | Public         | Tracing service. Data sent to public endpoints.                                                                    |
| AWS Fault Injection Service (FIS)               | Public         | Chaos engineering. Control plane is public.                                                                        |
| AWS Cloud9                                      | Hybrid         | IDE runs on EC2 (Private/VPC) but accessed via Browser (Public/Relay).                                             |
| Amazon CodeCatalyst                             | Public         | Unified software development service (SaaS) accessed via public endpoints.                                         |
| Amazon Corretto                                 | Public         | Distribution of OpenJDK (Software download/artifact).                                                              |
| AWS Amplify                                     | Public         | Hosting/Backend-as-a-Service. Accessed via public endpoints/CDNs.                                                  |
| AWS Device Farm                                 | Public         | App testing. Accessed via public endpoints.                                                                        |
| Amazon Location Service                         | Public         | Maps/Geofencing. Accessed via public endpoints.                                                                    |
| AWS Elemental MediaConvert                      | Public         | File-based transcoding. Accessed via public endpoints.                                                             |
| AWS Elemental MediaLive                         | Public         | Live video processing. Accessed via public endpoints.                                                              |
| AWS Elemental MediaConnect                      | Public         | Live video transport. Accessed via public endpoints (flows).                                                       |
| AWS Elemental MediaPackage v2                   | Public         | Video packaging. Accessed via public endpoints.                                                                    |
| AWS Elemental MediaTailor                       | Public         | Ad insertion. Accessed via public endpoints.                                                                       |
| Amazon Interactive Video Service (IVS)          | Public         | Managed live streaming. Accessed via public endpoints.                                                             |
| Amazon Simple Email Service (SES)               | Public         | Email sending/receiving service accessed via public API/SMTP endpoints.                                            |
| AWS End User Messaging                          | Public         | (Successor to some Pinpoint features) SMS/Push APIs are public.                                                    |
| AWS IoT Core                                    | Public         | Device gateway. Accessed via public MQTT/HTTPS endpoints.                                                          |
| AWS IoT Device Management                       | Public         | Fleet management. Control plane is public.                                                                         |
| AWS IoT TwinMaker                               | Public         | Digital twins. Control plane is public.                                                                            |
| AWS IoT FleetWise                               | Public         | Vehicle data. Control plane is public.                                                                             |
| AWS IoT SiteWise                                | Hybrid         | Edge gateways run on-prem; Cloud data storage accessed via public or VPC endpoints.                                |
| AWS IoT 1-Click                                 | Public         | Simple device triggers accessed via public endpoints.                                                              |
| AWS Database Migration Service (DMS)            | Private        | Replication instances provisioned into VPC subnets.                                                                |
| AWS DataSync                                    | Hybrid         | Agent (on-prem/VPC) connects to public service endpoints. Data transfer is private/encrypted.                      |
| AWS Transfer Family                             | Hybrid         | SFTP/FTP endpoints. Can be Public (Elastic IP) or Private (VPC Endpoint).                                          |
| AWS Application Migration Service (MGN)         | Private        | Replication servers run in staging area (VPC).                                                                     |
| AWS Mainframe Modernization                     | Private        | Runtime environments are provisioned into VPC subnets.                                                             |
| AWS Migration Hub                               | Public         | Tracking and orchestration service. Control plane is public.                                                       |
| Amazon GameLift                                 | Hybrid         | Game server fleets run in VPC (managed). Service API is public.                                                    |
| AWS RoboMaker                                   | Public         | Simulation jobs run in managed VPC. Can attach to customer VPC.                                                    |
| AWS Ground Station                              | Public         | Satellite data delivered to S3 or EC2 (VPC). Control plane is public.                                              |
| Amazon Braket                                   | Public         | Quantum computing. Jobs managed via public API.                                                                    |
| Amazon Connect                                  | Public         | Cloud-based contact center service (SaaS-like). Accessed via public HTTPS endpoints.                               |
| Amazon Chime SDK                                | Public         | Communication APIs accessed via public endpoints.                                                                  |
| AWS Wickr                                       | Public         | Encrypted communication service (SaaS) accessed via public internet.                                               |
| AWS Supply Chain                                | Public         | SaaS application accessed via public endpoints.                                                                    |
| Amazon WorkSpaces                               | Private        | Desktops are provisioned into VPC subnets. Streaming protocol requires gateways/endpoints.                         |
| Amazon AppStream 2.0                            | Private        | Streaming instances are provisioned into VPC subnets.                                                              |
| Amazon WorkLink                                 | Private        | (Legacy but active) Grants access to internal websites via VPC.                                                    |
| AWS HealthOmics                                 | Private        | Bioinformatics stores and workflows. Supports Interface VPC Endpoints.                                             |
| AWS HealthImaging                               | Public         | Medical imaging storage. Accessed via public APIs.                                                                 |
