from etl.db import get_engine
from etl.ingest.csv_ingest import ingest_csv
from etl.ingest.json_ingest import ingest_json
from etl.transform.csv_cleaner import clean_csv
from etl.transform.json_cleaner import clean_json
from etl.load.mysql_loader import load_df

engine = get_engine()

# CSV
raw_csv = ingest_csv("data/test.csv")
load_df(raw_csv, "raw_test", engine)

clean_csv_df = clean_csv(raw_csv)
load_df(clean_csv_df, "test", engine)

# JSON
raw_json = ingest_json("data/test.json")
raw_df = [{"raw_payload": str(r)} for r in raw_json]
load_df(pd.DataFrame(raw_df), "raw_users", engine)

users, phones, jobs = clean_json(raw_json)
load_df(users, "users", engine)
load_df(phones, "telephone_numbers", engine)
load_df(jobs, "jobs_history", engine)
