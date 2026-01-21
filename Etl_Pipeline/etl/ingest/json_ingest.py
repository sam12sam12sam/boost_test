import json
import pandas as pd
from etl.logger import logger

def ingest_json(path):
    logger.info("Ingesting JSON")
    with open(path) as f:
        records = [json.loads(line) for line in f]
    return records
