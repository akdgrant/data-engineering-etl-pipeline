# 🚀 Data Engineering ETL Pipeline (Adzuna API → PostgreSQL)

## 📌 Overview

This project is a complete **end-to-end ETL (Extract, Transform, Load) pipeline** that extracts real-time job data from the Adzuna API, transforms it using Python (Pandas), and loads it into a PostgreSQL database for structured querying and analysis.

It demonstrates practical data engineering skills including API ingestion, data cleaning, relational database design, environment-based configuration, logging, and reproducible pipeline execution.

---

## 🏗️ Architecture

Adzuna API  
→ Python (requests)  
→ Data Transformation (Pandas)  
→ Structured DataFrame  
→ PostgreSQL (jobs table)  
→ SQL Queries / Analytics  

---

## ⚙️ Tech Stack

- Python  
- Pandas  
- Requests (API calls)  
- PostgreSQL  
- psycopg2  
- python-dotenv  
- Logging module  

---

## 📊 Features

- Extracts live job listings from Adzuna API  
- Parses nested JSON into structured tabular format  
- Cleans and transforms job data using Pandas  
- Loads data into PostgreSQL database  
- Implements environment variables for secure API handling  
- Logging system for pipeline tracking and debugging  
- Handles real-world API responses and edge cases  

---

## 🔐 Security (Important)

This project uses environment variables to protect sensitive credentials.

Create a `.env` file:

ADZUNA_API_ID=your_api_id  
ADZUNA_API_KEY=your_api_key  

The `.env` file is excluded from version control using `.gitignore`.

---

## 🗄️ Database Schema

CREATE TABLE jobs (
    title TEXT,
    company TEXT,
    location TEXT
);

---

## ▶️ How to Run

### 1. Install dependencies
pip install -r requirements.txt

### 2. Set up PostgreSQL
CREATE DATABASE job_pipeline;

### 3. Run ETL pipeline
python3 src/fetch_data.py  
python3 src/load_to_postgres.py  

---

## 📈 Example Output

- Job title  
- Company name  
- Job location  

Stored in PostgreSQL for querying and analysis.

---

## 🧠 Key Engineering Concepts Demonstrated

- ETL pipeline design  
- API integration  
- Data transformation with Pandas  
- Relational database design (PostgreSQL)  
- Secure credential management (.env)  
- Logging and monitoring  
- Error handling in data pipelines  
- Git version control workflow  

---

## 🚀 Future Improvements

- Add Apache Airflow for scheduling automation  
- Dockerize the pipeline for deployment  
- Add data validation layer (Great Expectations)  
- Build dashboard using Power BI / Tableau  
- Expand to multi-source ingestion pipelines  

---

## 👤 Author

Built as a data engineering portfolio project demonstrating production-style ETL pipeline development using Python and PostgreSQL.