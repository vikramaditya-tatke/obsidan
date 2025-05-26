| `Format`       | `CSV`                            | `Parquet`                         | `JSON`                          | `ORC`                               | `Avro`                            |
| :------------- | :------------------------------- | :-------------------------------- | :------------------------------ | :---------------------------------- | :-------------------------------- |
| Structure      | Flat Tabular                     | Columnar Binary                   | Hierarchical Key-Value pair     | Columnar Binary                     | Row based Binary                  |
| Human Readable | Yes, simple                      | No                                | Yes, Flexible                   | No                                  | No                                |
| Schema Support | No Schema Enforcement            | Built-in Schema, Schema Evolution | Schema Optional                 | Built-in Schema, Complex types      | Built-in Schema, Schema Evolution |
| Compression    | Poor, Text-based                 | Excellent, Column based           | Moderate, Text-based            | Excellent, Column based             | Good, Row based                   |
| Performance    | Fast (simple), Slow (Complex)    | High for column queries           | Moderate, Slow (for large data) | High for column queries             | High for row based queries        |
| Use cases      | Simple Queries, Interoperability | Big Data Analytics, Data Lakes    | APIs, Web Apps                  | Big Data Analytics, Data Warehouses | Data Serialization, Streaming     |
