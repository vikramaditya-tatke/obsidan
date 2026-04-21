---
services:
  - AWS Glue
  - AWS Lake Formation
  - Amazon Athena
  - Amazon DataZone
  - Amazon EventBridge
  - Amazon Redshift
  - Amazon S3
tags: ['aws', 'data-mesh', 'datazone']
status: atomic
topic: AWS Data Engineering
domain: Exam Prep
created_at: 2025-12-24
---
## Data Mesh and DataZone
###  Active Recall
- How does this service integrate with other AWS components mentioned?

---


## Data Mesh Catalog

- Data moves from business processes to operational systems and is stored in unique domain lakes.
- Data is cataloged and schematized in the individual lake's catalogs.
- Consuming applications can get the data they need from one or more data lakes through the mesh catalog.
- The mesh catalog provides central governance and connects consumers directly to data lakes to form a mesh pattern.

![[Pasted image 20251005231837.png]]

## Data Gravity

Purpose built data stores cause the problem of data gravity.

Moving data becomes expensive and time consuming due to data volume.

Using data mesh architecture and help over come these issues by ensuring that data is available where it is needed for analytics.

## Amazon DataZone
> AWS implements the data mesh pattern through Amazon DataZone.

- It provides fine-grained access controls to ensure the right users can access the right data.
- Amazon DataZone also helps organizations discover, catalog, and collaborate around data to drive insights.
- Amazon DataZone integrates with various AWS services.
- It can publish data assets from sources like [[AWS [[AWS Glue Fundamentals|Glue]] Data Catalog]], Amazon [[Redshift Data Loading COPY|Redshift]], and Amazon [[Amazon S3 Fundamentals|S3]] into the Amazon DataZone catalog. Amazon DataZone supports querying data through [[AWS Data Engineer Zettelkasten Lite style/Athena]] and Amazon [[Redshift Data Loading COPY|Redshift]].
- It also uses [[Lake Formation]] and Amazon EventBridge to control access to data assets and integrate with other services.
![[datazone-HIW.png]]