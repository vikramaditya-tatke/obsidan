
| `Feature`              | `Columnar Database`                    | `Row-based Database`                |
| ---------------------- | -------------------------------------- | ----------------------------------- |
| Data Storage Format    | Stores data by columns                 | Stores data by rows                 |
| Best Use Case          | Analytical queries (OLAP)              | Transactional queries (OLTP)        |
| Read Performance       | Faster for aggregations across columns | Faster for reading whole rows       |
| Write Performance      | Slower for insert/update operations    | Faster for insert/update operations |
| Compression Efficiency | High (due to similar data types)       | Lower (diverse data types per row)  |
| Examples               | ClickHouse, Snowflake, Redshift        | MySQL, PostgreSQL                   |
