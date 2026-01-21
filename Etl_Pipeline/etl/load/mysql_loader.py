def load_df(df, table, engine):
    df.to_sql(table, engine, if_exists="append", index=False)
