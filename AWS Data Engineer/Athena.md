## Athena Federated Queries
- Query data from sources other than S3.
- Data source connectors translate between source and Athena - Data source connectors run on Lambda
- Views can be created that are stored in Glue.
- AWS Secrets Manager can be used to manage the credentials for the external data sources.
- Cross account federated queries
- Pass through queries - Using query language native to the data source.

![[Athena 2025-10-10 18.30.08.excalidraw]]