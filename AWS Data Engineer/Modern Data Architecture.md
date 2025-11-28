# Inside-out data movement

![[Pasted image 20251005231049.png]]


# Outside-in data movement

![[Pasted image 20251005231119.png]]

#  Around the perimeter data movement
![[Pasted image 20251005231141.png]]


# Data Mesh
> Distributed, domain driven architecture centered around the concept of the data as a product

![[Pasted image 20251005231837.png]]

- Before modern data architecture data teams were formed for individual stages of the data pipeline. 
- Data teams should be aligned to business domains instead of particular stages of the pipeline to create a shared data architecture.
- Each business aligned domain (team) produces and consumes data supporting their needs.
- Supports data sharing and federation across the organization. 
- Provides central data discovery, security and auditing for the organization for compliance and governance.

## Architecture 

![[dataMesh_diagram.svg]]

#### Data Mesh Catalog

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
- It can publish data assets from sources like AWS Glue Data Catalog, Amazon Redshift, and Amazon S3 into the Amazon DataZone catalog. Amazon DataZone supports querying data through Athena and Amazon Redshift. 
- It also uses Lake Formation and Amazon EventBridge to control access to data assets and integrate with other services.
- 
![[datazone-HIW.png]]