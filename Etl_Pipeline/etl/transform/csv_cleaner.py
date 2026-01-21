import pandas as pd

def clean_csv(df):
    df["created_at"] = pd.to_datetime(df["created_at"], errors="coerce")
    df["last_login"] = pd.to_datetime(df["last_login"], unit="s", errors="coerce")
    df["is_claimed"] = df["is_claimed"].astype(str).str.lower().isin(["true", "1"])
    df["paid_amount"] = pd.to_numeric(df["paid_amount"], errors="coerce").round(2)
    df = df.drop_duplicates(subset=['id'], keep='first', inplace=False)
    return df
