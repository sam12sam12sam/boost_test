import json
import pandas as pd
from etl.logger import logger

def ingest_json(path):
    logger.info("Ingesting JSON")
    with open(path) as f:
        records = [json.loads(line) for line in f]
    raw_df = pd.DataFrame({'raw_payload': records})
    raw_df['raw_payload'] = raw_df['raw_payload'].apply(json.dumps)
    return raw_df
