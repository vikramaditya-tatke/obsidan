---
services:
  - Amazon EC2
  - Amazon VPC
tags: ['aws', 'vpc', 'security']
status: atomic
topic: AWS Data Engineering
domain: Exam Prep
created_at: 2025-12-24
---
## VPC Security (SG Vs NACL)
###  Active Recall
- How is data secured or encrypted in this context?

---

![[VPC.excalidraw]]

### Network ACL and Security Groups
- These are attached at the subnet level.
- Firewall which controls traffic from and to subnet
- Can have ALLOW and DENY rules
- Rules can only include IP Addresses

### Security Groups

- A firewall that controls traffic to and from an ENI / an [[EC2|EC2]] instance.
- Can only have ALLOW rules
- Rules can include either IP addresses or other security groups.

| **Security Group**                                                                                                                                           | **Network ACL**                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Operates at the instance level                                                                                                                               | Operates at the subnet level                                                                                                                          |
| Supports allow rules only                                                                                                                                    | Supports allow rules and deny rules                                                                                                                   |
| *Is stateful*: It evaluates the conversation between the entities. <br>Hence, return traffic is automatically allowed, regardless of any rules.              | *Is stateless*: It considers the traffic flow as separate parts - request and response. <br>Hence, return traffic must be explicitly allowed by rules |
| We evaluate all rules before deciding whether to allow traffic                                                                                               | We process rules in number order when deciding whether to allow traffic                                                                               |
| Applies to an instance only if someone specifies the security group when launching the instance, or associates the security group with the instance later on | Automatically applies to all instances in the subnets it's associated with (therefore, you don't have to rely on users to specify the security group) |