# Provisioned
- **1 WCU (Write Compute Unit)**-> 1 write per second, item up to 1 KB. If item > 1KB, more WCUs are consumed.
	- Example 1: 10 ips, item size 2 KB: 20 WCUs
	- Example 2: 6 ips, item size 4.5 KB: **4.5 gets rounded up to 5**, hence 30 WCUs are consumed.
- **RCU (Read Compute Unit)** -> 1 Strongly Consistent Read | 2 Eventually consistent reads per second, item up to 4 KB. Let's classify read types - 
	- Strongly Consistent Read: _ConsistentRead_ param needs to be set to `True` in API calls (GetItem, BatchGetItem, Query, Scan) -> Consumes 2x the RCU
	- Eventually Consistent Read (default) -> Consumes 1x RCU or the regular amount.
	- Example 1: 10 Strongly Consistent Reads per second, item size 4 KB.
			$10 * 4/4 = 40$ RCU
	- Example 2: 16 Eventually Consistent Reads per second, item size 12 KB.
			$16/2 * 12/4 = 24$ RCU

# On-demand:
No capacity planning is required.
More expensive. 2.5x more expensive
Unlimited WCU and RCU as charges are accumulated in terms of RRU and WRU
- **RRU (Read Request Unit)**: same as RCU
- **WRU (Write Request Unit)**: same as WCU

# DAX DynamoDB Accelerator

- Fully Managed highly, available in-memory cache.
- Microseconds latency for cached reads and queries
- Used to solve the **Hot Key** problem
- TTL: 5 minutes by default
- Up to 10 nodes in the cluster
- Multi-AZ (3 nodes recommended for production)
- Secure 
	- Encryption at rest
	- VPN
	- IAM
	- CloudTrail, etc.

![[DAX Elasticache]]