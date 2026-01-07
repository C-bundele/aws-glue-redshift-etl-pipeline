# Automated ETL Pipeline with AWS Glue & Redshift

## Overview
This project implements a **serverless ETL pipeline** using AWS Glue and Amazon Redshift to enable near real-time analytics on structured data. The architecture automates schema discovery, data transformation, and loading into a performance-optimized data warehouse.

The pipeline is designed to reduce operational overhead while improving data reliability and query performance.

## Architecture
The pipeline follows a modular, event-driven design:

- Amazon S3 for raw data ingestion
- AWS Glue Crawlers for automated schema inference
- AWS Glue ETL Jobs for transformation and validation
- Amazon Redshift as the analytical data warehouse
- Amazon CloudWatch for monitoring and alerting

Refer to `architecture/architecture-diagram.png` for a visual overview.

## Key Features
- Reduced end-to-end ETL processing time by ~40%
- Automated batch ingestion supporting 15-minute analytics refresh
- Built-in data quality validation
- Partitioned and optimized Redshift data models
- Scalable, serverless architecture

## Tech Stack
- AWS Glue (Jobs, Crawlers)
- Amazon S3
- Amazon Redshift
- PySpark
- SQL
- Amazon CloudWatch

## Data Flow
1. Raw data files land in Amazon S3
2. Glue Crawler updates the Data Catalog
3. Glue Job cleans, transforms, and validates data
4. Transformed data is loaded into Redshift
5. Optimized tables support downstream analytics and BI

## Future Enhancements
- Incremental loading with job bookmarks
- CI/CD automation for Glue jobs
- Integration with BI tools (QuickSight / Power BI)

