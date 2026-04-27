# End-to-End ETL Pipeline: Job Listings Data

## Overview
This project is an end-to-end ETL (Extract, Transform, Load) pipeline that collects job listing data from the Adzuna API, processes and transforms it using Python, and loads it into a PostgreSQL database for structured storage and analysis.

The pipeline demonstrates core data engineering concepts including API ingestion, data transformation, relational database modeling, and SQL validation.

---

## Architecture
Adzuna API → Python ETL (Extract & Transform) → PostgreSQL (Load) → SQL Validation

---

## Tech Stack
- Python
- PostgreSQL
- pandas
- psycopg2
- REST API (Adzuna)
- SQL

---

## Features
- Extracts job posting data from a public API
- Transforms nested JSON into structured tabular format
- Loads cleaned data into PostgreSQL
- Implements modular pipeline design (separation of extract and load steps)
- Includes logging for pipeline tracking and debugging
- Validates loaded data using SQL queries

---

## Project Structure
data-engineering-project/
│
├── src/
│   ├── fetch_data.py          # Extracts and transforms API data
│   ├── load_to_postgres.py    # Loads data into PostgreSQL
│
├── sql/
│   └── create_tables.sql      # Database schema
│
├── logs/
│   └── pipeline.log           # Pipeline logs
│
├── requirements.txt
└── README.md

---

## How to Run the Project

### 1. Install dependencies
pip install -r requirements.txt

---

### 2. Create database table

Run in PostgreSQL:
CREATE TABLE jobs (
    title TEXT,
    company TEXT,
    location TEXT
);

---

### 3. Run the pipeline
cd src
python3 load_to_postgres.py

---

## Data Validation

Run in PostgreSQL:
SELECT COUNT(*) FROM jobs;
SELECT * FROM jobs LIMIT 10;

---

## What This Project Demonstrates
- End-to-end ETL pipeline design
- Working with REST APIs
- Data transformation using Python
- Relational database design and loading
- SQL querying and validation
- Modular and maintainable code structure

---

## Notes
- API credentials are stored in code for learning purposes
- In production, secrets should be stored in environment variables (.env)