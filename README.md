# SQL with Google BigQuery

Structured Query Language, or SQL, is a powerful programming language that enables data scientists and analysts to navigate through and extract useful insights from large databases. 
BigQuery is a Google's server-less cloud based data warehouse service that lets you apply SQL queries to big datasets. 
Using Cloud Client Libraries for the BigQuery API we can efficiently query to extract insightful information from large datasets using Python.

This repository aims to provide an introduction for running SQL queries using BigQuery web service where the authentication is provided by a [service account key](https://cloud.google.com/bigquery/docs/authentication/service-account-file) file.
The project is based on Kaggle's SQL tutorials: [Intro to SQL](https://www.kaggle.com/learn/intro-to-sql) and [Advanced SQL](https://www.kaggle.com/learn/advanced-sql). 

To provide such authentication a `client` object with right credentials is generated via the `client()` function in `bq_sa_auth.py` which then called in the respective notebook files that goes through all the exercises and tutorials
in [Intro to SQL](https://www.kaggle.com/learn/intro-to-sql) and  [Advanced SQL](https://www.kaggle.com/learn/advanced-sql). 

## Dependencies

The project is developed using Python 3.10 on jupyter notebooks using VS Code. You need to install Python client for google bigquery:

- `pip install google-cloud-bigquery`

More detailed information on setting up a project using Google Clouds Web UI and authentication can be found in the following [link](https://cloud.google.com/python/docs/reference/bigquery/latest). 
