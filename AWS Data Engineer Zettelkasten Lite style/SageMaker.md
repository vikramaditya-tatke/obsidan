---
services:
  - AWS IAM
  - Amazon S3
  - Amazon SageMaker
tags: ['aws', 'general']
status: atomic
topic: AWS Data Engineering
domain: Exam Prep
created_at: 2025-12-24
---
## Amazon SageMaker

**Amazon SageMaker** is a fully managed service that provides every developer and data scientist with the ability to build, train, and deploy machine learning (ML) models quickly.

###  Active Recall
*   **What specific problem does this service solve in a data pipeline?** -> End-to-end ML workflow management.
*   **How does Feature Store ensure consistency between training and inference?** -> By syncing data between an [[SageMaker#Online Store|Online Store]] (inference) and [[SageMaker#Offline Store|Offline Store]] (training).
*   **Which Feature Store component supports real-time low-latency retrieval?** -> **Online Store**.
*   **Where does the Offline Store persist data?** -> [[Amazon S3 Fundamentals|Amazon S3]].
*   **What is the CI/CD service specifically for SageMaker ML workflows?** -> [[SageMaker#3. SageMaker Pipelines|SageMaker Pipelines]].
*   **Which tool is best for low-code data preparation and EDA?** -> [[SageMaker#2. SageMaker Data Wrangler|Data Wrangler]].
*   **Which service is used to create labeled datasets for supervised learning?** -> [[SageMaker#5. SageMaker Ground Truth|Ground Truth]].

---

###  Key Capabilities

#### 1. SageMaker Feature Store
A centralized repository to store, update, retrieve, and share ML features. It solves the **Training-Serving Skew** problem.

![[SageMaker Feature Store.excalidraw]]

**Architecture & Workflow:**
*   **Ingestion:** Data is ingested into a **Feature Group**.
*   **Dual Storage:**
    *   **Online Store:** Optimized for low-latency, real-time lookups (e.g., for [[SageMaker#Inference|Model Endpoints]]).
    *   **Offline Store:** Backed by [[Amazon S3 Fundamentals|S3]]; optimized for batch processing and historical training data.
*   **Synchronization:** Data written to the Online Store is automatically replicated to the Offline Store.
*   **Consumption:**
    *   **Training:** Models are trained using historical data from the **Offline Store** (via S3/Athena).
    *   **Inference:** Real-time endpoints query the **Online Store** for the latest feature values (millisecond latency).

#### 2. SageMaker Data Wrangler
**Data Wrangler** is a **low-code/no-code** tool that reduces data preparation time from weeks to minutes.
*   **Visual Interface:** Import, visualize, clean, and transform data without writing code.
*   **300+ Transformations:** Built-in transforms for formatting, casting, and feature engineering.
*   **Export:** Generates code (Python, PySpark, SQL) or exports flows to **SageMaker Pipelines** or **Feature Store**.

#### 3. SageMaker Pipelines
The first **CI/CD service** designed specifically for Machine Learning.
*   **Orchestration:** Automates the end-to-end ML workflow (Data Prep -> Train -> Tune -> Evaluate -> Register).
*   **Traceability:** Tracks lineage of data, code, and model artifacts.
*   **Integration:** works natively with SageMaker Processing and Training jobs.

#### 4. SageMaker Processing
A dedicated compute environment to run data processing workloads (Preprocessing or Postprocessing).
*   **Frameworks:** Supports Scikit-Learn, Hugging Face, Spark, and custom Docker containers.
*   **Decoupling:** Separates data processing logic from model training logic.

#### 5. SageMaker Ground Truth
A fully managed data labeling service.
*   **Human-in-the-loop:** Uses human labelers (private workforce, vendors, or Amazon Mechanical Turk) to label raw data (images, text, video) for supervised learning.
*   **Assisted Labeling:** Uses ML to automate the labeling of "easy" data, sending only "hard" data to humans.

#### 6. SageMaker Canvas
A **no-code** visual interface for building ML models and generating predictions.
*   **User Persona:** Designed for **Business Analysts** and non-technical users.
*   **Workflow:** Import data from S3, Redshift, or Snowflake -> Auto-join datasets -> Build models automatically (AutoML) -> Review accuracy -> Generate predictions.
*   **Capabilities:** Supports classification, regression, and forecasting. You can share models with Data Scientists (exported as SageMaker Studio notebooks).

###  Use Cases
*   **Real-time Fraud Detection:** Using [[SageMaker#1. SageMaker Feature Store|Feature Store]] to fetch user transaction history in milliseconds.
*   **MLOps Automation:** Using [[SageMaker#3. SageMaker Pipelines|Pipelines]] to automatically retrain and deploy a model when new data arrives in S3.
*   **Data Cleaning:** Using [[SageMaker#2. SageMaker Data Wrangler|Data Wrangler]] to visualize distribution and handle outliers before training.
*   **Business Forecasting:** Using **SageMaker Canvas** to predict inventory demand or customer churn without writing code.

> [!INFO] Exam Tip: Processing vs. Wrangler vs. Glue
> *   **SageMaker Data Wrangler:** UI-based, interactive, low-code. Best for **Data Scientists** doing EDA and feature engineering.
> *   **SageMaker Canvas:** Visual interface, **no-code**. Best for **Business Analysts** building models.
> *   **SageMaker Processing:** Code-based (Python/Spark scripts). Best for **ML Engineers** building automated pipeline steps.
> *   **AWS Glue:** Serverless ETL. Best for general-purpose data integration *upstream* of the ML lifecycle (e.g., creating the raw Data Lake).

> [!INFO] Exam Tip: Feature Store
> *   **Offline Store** = S3 + Glue Data Catalog (Queryable via Athena).
> *   **Online Store** = High throughput, low latency (No SQL access, key-value access).
> *   If a question asks about "sharing features across teams" or "consistent features for training and inference," choose **SageMaker Feature Store**.