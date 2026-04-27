import requests
import pandas as pd
import logging
from dotenv import load_dotenv
import os

load_dotenv()

API_ID = os.getenv("ADZUNA_API_ID")
API_KEY = os.getenv("ADZUNA_API_KEY")

logging.basicConfig(
    filename="../logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def fetch_jobs():
    logging.info("Fetching data from API")

    url = f"https://api.adzuna.com/v1/api/jobs/us/search/1?app_id={API_ID}&app_key={API_KEY}&what=data+engineer"

    response = requests.get(url)
    data = response.json()

    jobs = data.get("results", [])
    rows = []

    for job in jobs:
        rows.append({
            "title": job.get("title"),
            "company": job.get("company", {}).get("display_name"),
            "location": job.get("location", {}).get("display_name")
        })

    df = pd.DataFrame(rows)

    logging.info(f"Fetched {len(df)} rows")

    return df


if __name__ == "__main__":
    df = fetch_jobs()
    print(df.head())