# ETL Architecture Overview

This project implements a serverless ETL pipeline using AWS Glue and Amazon Redshift to support near real-time analytics.

## High-Level Flow

1. Raw transactional data is ingested into Amazon S3.
2. AWS Glue Crawler scans incoming data and automatically infers schema.
3. AWS Glue ETL Job performs:
   - Data cleansing
   - Schema standardization
   - Data quality validation
4. Transformed data is loaded into Amazon Redshift.
5. Redshift tables are optimized using distribution keys, sort keys, and partitioning.

## Design Principles

- Serverless and scalable architecture
- Automated schema discovery
- Fault-tolerant batch ingestion (15-minute cadence)
- Performance-optimized analytics layer
- Built-in data quality checks

## AWS Services Used

- Amazon S3: Raw and processed data storage
- AWS Glue: ETL processing and schema catalog
- Amazon Redshift: Analytical data warehouse
- Amazon CloudWatch: Monitoring and observability
