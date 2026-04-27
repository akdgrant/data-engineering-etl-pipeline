import psycopg2
import logging
from fetch_data import fetch_jobs

logging.basicConfig(
    filename="../logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def load_data():
    logging.info("Starting load step")

    df = fetch_jobs()
    print("Rows fetched:", len(df))

    conn = psycopg2.connect(
        dbname="job_pipeline",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432"
    )

    cur = conn.cursor()

    for _, row in df.iterrows():
        cur.execute(
            """
            INSERT INTO jobs (title, company, location)
            VALUES (%s, %s, %s)
            """,
            (row["title"], row["company"], row["location"])
        )

    conn.commit()

    cur.close()
    conn.close()

    print("Inserted rows:", len(df))
    logging.info(f"Inserted {len(df)} rows into database")


if __name__ == "__main__":
    load_data()