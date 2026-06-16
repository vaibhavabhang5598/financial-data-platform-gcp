# Enterprise Financial Transaction Analytics Platform on GCP

## Overview
Production-style Data Engineering project using PySpark, Dataproc, Cloud Composer (Airflow), GCS and BigQuery.

## Architecture
Sources -> GCS -> Cloud Composer -> Dataproc(PySpark) -> BigQuery -> Dashboard

## Features
- Incremental Processing
- SCD Type 2 Customer Dimension
- Fraud Detection Rules
- Data Quality Framework
- BigQuery Partitioning & Clustering
- Cloud Composer Orchestration

## Tech Stack
PySpark, Python, GCP, Dataproc, BigQuery, Cloud Composer, Airflow, GCS

## Pipeline
ingest_customer -> ingest_transaction -> data_quality -> customer_scd2 -> fraud_detection -> load_bigquery

## Business KPIs
- Daily Revenue
- Fraud Rate
- Active Customers
- Top Merchants
