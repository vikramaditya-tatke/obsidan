---
services:
  - AWS IAM
  - Amazon Route 53
  - Amazon S3
  - Amazon VPC
tags: ['aws', 'route53', 'dns']
status: atomic
topic: AWS Data Engineering
domain: Exam Prep
created_at: 2025-12-24
---
## Amazon Route 53
###  Active Recall
- What specific problem does this service solve in a data pipeline?
- How does this integrate with S3 or IAM?

---

![[VPC.excalidraw]]

## Route 53

Route 53 supports - _A, AAAA, CNAME, NS_ (imp), CAA, DS, MX, NAPTR, PTR, SOA, TXT, SPF, SRV record types.

_A_: maps to hostname to IPv4

_AAAA_: maps to IPv6

_CNAME_: maps a hostname to another hostname.

_NS_: Name servers for Hosted Zones

- Public Hosted Zones - Publicly resolvable. For ex: yourname.com
- Private Hosted Zones - Privately resolvable from within the [[VPC Networking Fundamentals|VPC]].
- For ex: company.internal

Each record contains:

- **Domain / subdomain Name**: example.com
- **Record Type** - A or AAAA
- **Value** - Ex: 1.2.2.52
- **Routing Policy** - how Route 53 responds to queries
- **TTL** - Amount of time the record is cached