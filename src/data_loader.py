import pandas as pd


def load_spacex_data(path="data/processed/spacex_api_clean.csv"):
    """
    Load and prepare SpaceX launch data for analysis and dashboards.
    """
    df = pd.read_csv(path)

    # Feature engineering used across the project
    df["launch_year"] = pd.to_datetime(df["launch_date"]).dt.year

    return df
