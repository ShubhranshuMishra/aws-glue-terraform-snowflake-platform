# AWS Glue Terraform Snowflake Platform

Portfolio project that shows how to provision a lightweight AWS data platform with Terraform and use AWS Glue to land curated data into Snowflake.

## Stack
- AWS S3
- AWS Glue
- AWS IAM
- Terraform
- Snowflake
- Python

## Scenario
An organization receives partner sales files in S3. Glue jobs normalize and enrich the data before loading it into Snowflake for analytics.

## Repository Layout
```text
terraform/main.tf
glue/jobs/partner_sales_etl.py
snowflake/schema.sql
```

## What This Demonstrates
- Infrastructure as code for data platforms
- IAM-aware cloud design
- Batch ETL with AWS Glue
- Cross-cloud warehousing pattern into Snowflake

## How To Demo
1. Run `terraform init` and `terraform apply`.
2. Upload sample partner files to the input S3 bucket.
3. Trigger the Glue job.
4. Run the Snowflake schema script and validate the target table load.
