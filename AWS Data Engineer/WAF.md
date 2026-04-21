WAF or Web Application Firewalls helps protect web-applications or APIs against common web exploits and bots that could affect availability, compromise security or consume excessive resources.

## Web ACLs
WAF uses a component known as Web Access Control Lists (Web ACLs) and are also associated with various other web AWS services. Example of AWS services that can be protected using WAF are
- CloudFront (Global)
- ALB (Regional)
- AppSync (Regional)
- API Gateway (Regional)

Web ACLs need to be configured globally or within a region based on which AWS service needs to be protected by WAF.
Web ACLs contain *rules* and *rule groups* that can be as simple as Allow or Deny Lists or complex enough to cover XSS (Cross-site scripting attacks), SQL Injection, HTTP Flood, IP reputation or botnet attacks. Web ACLs must have rules / rule groups.

- Web ACLs cannot be used with AWS Outposts.
- One-to-many relationship with resources - One resource can only have one Web ACL but one ACL can be assigned to multiple resources.
	- Global Web ACLs cannot be assigned to regional sources.
##### Updating Web ACLs
1. Manually by humans.
2. Via Event Bridge (Scheduled Rules) and Lambda by triggering an update after detecting a change in a publicly maintained IP list to block known bad actors.

Logs can be sent to [[CloudWatch]], [[Kinesis#Kinesis Data Firehose]], [[S3]]. These logs can be used in an event-driven architecture security response architecture to extract and identify intelligence to update the Web ACLs to enhance the security of the platform.

## WAF Rules and Rule Groups

- Rules require compute based on their complexity.
- Web ACLS Compute Units AKA (WCU) are an indication of the complexity of the rule and the maximum value is 1500.
- Rule Groups contain rules and don't have a default action.
- Rule Groups can be Managed (AWS or Marketplace), ours, Shield & Firewall Manager service controls.
- Rule Groups can be reused in one or more ACLs and have a max WCU or 1500.
	- Type: Regular or rate-based.