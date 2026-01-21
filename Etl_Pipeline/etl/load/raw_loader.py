import pandas as pd
import json

def load_raw_csv(df, engine):
    df.astype(str).to_sql(
        "raw_test",
        engine,
        if_exists="append",
        index=False
    )

def load_raw_json(records, engine):
    df = pd.DataFrame({
        "raw_payload": [json.dumps(r) for r in records]
    })
    df.to_sql("raw_users", engine, if_exists="append", index=False)
