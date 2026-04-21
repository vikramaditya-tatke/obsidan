---
services: ['AWS Cloud']
tags: ['aws', 'architecture']
status: atomic
topic: AWS Data Engineering
domain: Exam Prep
created_at: 2025-12-24
---
## Modern Data Architecture Patterns
###  Active Recall
- How is data secured or encrypted in this context?

---


## Inside-out Data Movement

![[Pasted image 20251005231049.png]]

## Outside-in Data Movement

![[Pasted image 20251005231119.png]]

## Around the Perimeter Data Movement

![[Pasted image 20251005231141.png]]

## Data Mesh
> Distributed, domain driven architecture centered around the concept of the data as a product

![[Pasted image 20251005231837.png]]

- Before modern data architecture data teams were formed for individual stages of the data pipeline.
- Data teams should be aligned to business domains instead of particular stages of the pipeline to create a shared data architecture.
- Each business aligned domain (team) produces and consumes data supporting their needs.
- Supports data sharing and federation across the organization.
- Provides central data discovery, security and auditing for the organization for compliance and governance.

### Architecture

![[dataMesh_diagram.svg]]

##