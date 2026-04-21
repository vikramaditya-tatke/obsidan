- VPC is a regional resource.
- Subnets allow partitioning of network within the VPC.
- VPCs have a CIDR range like 10.0.0.128/16 

![[VPC.excalidraw]]


## Gateways

## Internet Gateway
Public subnets have a direct route to the internet gateway.
## NAT
This allows instances in Private Subnets to access the internet while remaining private.

**NAT Gateways**: Managed by AWS.
**NAT Instances**: Self Managed.
### Network ACL and Security Groups
- These are attached at the subnet level.
- Firewall which controls traffic from and to subnet
- Can have ALLOW and DENY rules
- Rules can only include IP Addresses

### Security Groups

- A firewall that controls traffic to and from an ENI / an EC2 instance.
- Can only have ALLOW rules
- Rules can include either IP addresses or other security groups.

| **Security Group**                                                                                                                                           | **Network ACL**                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Operates at the instance level                                                                                                                               | Operates at the subnet level                                                                                                                          |
| Supports allow rules only                                                                                                                                    | Supports allow rules and deny rules                                                                                                                   |
| *Is stateful*: It evaluates the conversation between the entities. <br>Hence, return traffic is automatically allowed, regardless of any rules.              | *Is stateless*: It considers the traffic flow as separate parts - request and response. <br>Hence, return traffic must be explicitly allowed by rules |
| We evaluate all rules before deciding whether to allow traffic                                                                                               | We process rules in number order when deciding whether to allow traffic                                                                               |
| Applies to an instance only if someone specifies the security group when launching the instance, or associates the security group with the instance later on | Automatically applies to all instances in the subnets it's associated with (therefore, you don't have to rely on users to specify the security group) |
## VPC Flow Logs
Captures information about IP traffic going into your interfaces.
- VPC Flow Logs
- Subnet Flow Logs
- ENI Flow Logs
- Data Flow could be like follows for storing / processing the logs data
	- VPC Flow Logs -> [[S3]] 
	- VPC Flow Logs -> [[CloudWatch]] 
	- VPC Flow Logs -> [[Kinesis# Kinesis Data Firehose]] 

### Log Fields Structure
The standard VPC Flow Log entry consists of the following fields in order:
interface-id
- srcaddr
- dstaddr
- srcport
- dstport
- protocol
- packets
- bytes
- start
- end
- action
- log-status

### Example Log Entries
##### Allowed Traffic (ACCEPT)
2 ACC-ID eni-ID 119.18.34.78 10.16.48.20 0 0   1   4 336 1432917027 1432917142 ACCEPT OK
                *srcaddr*       *dstaddr*       *ICMP*                              *Action*

##### Blocked Traffic (REJECT)
2 ACC-ID eni-ID 10.16.48.20 119.18.34.78 0 0 1 4 336 1432917094 1432917142 REJECT OK
                *srcaddr*       *dstaddr*       *ICMP*                              *Action*

### Protocol Reference
The `protocol` field uses standard IANA protocol numbers:
ICMP = 1
TCP = 6
UDP = 17

> VPC Flow logs DO NOT log the traffic to and from 169.254.169.254, 169.254.169.123, DHCP, Amazon DNS Server, Amazon Windows License Server.
## VPC Peering
- VPC Peering is used to *privately connect* VPCs using the AWS Network, then the VPCs will behave as if they were the same network.
- VPCs must not have overlapping IP ranges.
- VPC Peering is not transitive - needs to be established for EACH VPC that needs to communicate with another. 
- **For Example**:  `VPC A <-> VPC B, VPC A <-> VPC C: VPC  B <-X-> VPC C` 

## VPC Endpoints

- Endpoints allow you to connect to AWS Services privately.
- All AWS Services are have an option to attach a default VPC which makes the resources publicly accessible by assigning them a public IPS address - The default VPC has an Internet Gateway attached to it.
- The AWS Control Plane is public, while the resources themselves are not (unless attached to the default VPC).

## VPC Endpoint Services (AWS PrivateLink)

- Most secure able scalable way to expose a service to 1000s of VPCs.
- Requires a NLB in the service VPC and an ENI in the Customer VPC
 
### VPC Endpoint Gateway: S3 and DynamoDB
### VPC Endpoint Interface: most AWS services including S3 and DynamoDB

## Site-to-Site VPN
- Connect an on-prem VPC to AWS.
- The connection is automatically encrypted.
- Goes over the public internet.
## Direct Connect

- Establishes a physical connection between on-prem and AWS.
- Connection is private, secure and fast.
- Goes over a private network.
- Takes a month to establish.
## Route 53
Route 53 supports - _A, AAAA, CNAME, NS_ (imp), CAA, DS, MX, NAPTR, PTR, SOA, TXT, SPF, SRV record types.
_A_: maps to hostname to IPv4
_AAAA_: maps to IPv6
_CNAME_: maps a hostname to another hostname.
_NS_: Name servers for Hosted Zones
- Public Hosted Zones - Publically resolvable. For ex: yourname.com
- Private Hosted Zones - Privately resolvable from within the VPC. For ex: company.internal

Each record contains:
- **Domain / subdomain Name**: example.com 
- **Record Type** - A or AAAA
- **Value** - Ex: 1.2.2.52
- **Routing Policy** - how Route 53 responds to queries
- **TTL** - Amount of time the record is cached 