# Setup


## Recommendations 
- ClickHouse tends to work more efficiently with a large number of cores at a lower clock rate than with fewer cores at a higher clock rate.
- To calculate the required volume of RAM, you may estimate the size of temporary data for [GROUP BY](https://clickhouse.com/docs/sql-reference/statements/select/group-by), [DISTINCT](https://clickhouse.com/docs/sql-reference/statements/select/distinct), [JOIN](https://clickhouse.com/docs/sql-reference/statements/select/join) and other operations you use.
- To reduce memory consumption, ClickHouse can swap temporary data to external storage. See [GROUP BY in External Memory](https://clickhouse.com/docs/sql-reference/statements/select/group-by#group-by-in-external-memory) for details.
- Disable the operating system's swap file in production environments.

###  Example - Fortune 500 B2B SaaS

| **_Storage_**                         |                         |
| ------------------------------------- | ----------------------- |
| **Monthly new data volume**           | 30TB                    |
| **Total Storage (compressed)**        | 540TB                   |
| **Data retention**                    | 18 months               |
| **Disk per node**                     | 25TB                    |
| **_CPU_**                             |                         |
| **Concurrency**                       | 200+ concurrent queries |
| **# of replicas (including HA pair)** | 44                      |
| **vCPU per node**                     | 62                      |
| **Total vCPU**                        | 2700                    |
| **_Memory_**                          |                         |
| **Total RAM**                         | 11TB                    |
| **RAM per replica**                   | 256GB                   |
| **RAM to vCPU ratio**                 | 4:1                     |
| **RAM to disk ratio**                 | 1:50                    |
