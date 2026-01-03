import pandas as pd
from src.utils import map_rocket_name
from src.preprocessing import clean_for_dashboard

def load_spacex_data(path="data/processed/spacex_api_clean.csv"):
    df = pd.read_csv(path)
    df["launch_year"] = pd.to_datetime(df["launch_date"]).dt.year

    # Human-readable rocket name
    df["rocket_name"] = df["rocket"].apply(map_rocket_name)

    df = clean_for_dashboard(df)

    return df

