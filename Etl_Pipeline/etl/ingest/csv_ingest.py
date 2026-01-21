import pandas as pd
from etl.logger import logger

def ingest_csv(path):
    logger.info("Ingesting CSV")
    return pd.read_csv(path)
