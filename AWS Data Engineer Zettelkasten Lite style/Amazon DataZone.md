---
services:
  - Amazon DataZone
tags:
  - aws
  - data-governance
  - analytics
status: atomic
topic: Data Governance
domain: Analytics
created_at: 2026-01-04
---
## Amazon DataZone

**Amazon DataZone** is a data management service that makes it faster and easier for customers to catalog, discover, share, and govern data stored across AWS, on-premises, and third-party sources.

![[Amazon Datazone.excalidraw]]

###  Active Recall
*   **What are the primary organizational entities in DataZone?** -> [[Amazon DataZone#Domains|Domains]]
*   **Where do users discover and subscribe to data?** -> [[Amazon DataZone#Data portal|Data Portal]]
*   **How does DataZone handle permissions?** -> Manages permissions via [[Lake Formation]] and [[Redshift]].

---

###  Key Components

The service is built around several core concepts that structure how data is governed and accessed:

*   **Domains**: Organizational entities used to group users, data, and projects together.
*   **Data Projects**: Groupings of people, data sets, and analytics tools.
*   **Data Environments**: Provide the infrastructure within projects (such as storage and analytics tools).

###  Features & Capabilities

*   **Data Portal**
    *   A web application accessible outside of the AWS console.
    *   Used to catalog, discover, govern, share, and analyze data.
    *   Supports IAM authentication.
*   **Business Data Catalog**
    *   Allows you to define a taxonomy and business glossary for your data.
*   **Governance and Access Control**
    *   Provides built-in workflows for requesting and approving data access.
    *   Automatically manages permissions via integration with [[AWS Lake Formation]] and [[Amazon Redshift]].

###  Use Cases
*   **Data Democratization**: Allowing business users to find and access data without deep technical knowledge.
*   **Unified Governance**: Managing access control across a distributed data mesh architecture.

> [!INFO] Exam Tip: Comparison
> *   **vs. [[Lake Formation]]:** Lake Formation is the underlying engine for enforcing fine-grained permissions. DataZone sits "on top" as a business layer for discovery, workflow approvals, and project organization.
> *   **vs. [[AWS Glue Data Catalog]]:** Glue Data Catalog is the technical metadata repository. DataZone adds business context (glossaries) and a user-friendly portal.
