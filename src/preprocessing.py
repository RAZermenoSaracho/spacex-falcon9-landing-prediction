import pandas as pd

def clean_for_dashboard(df: pd.DataFrame) -> pd.DataFrame:
    """
    Minimal cleaning to ensure dashboard stability.
    """
    df = df.dropna(subset=["landing_success", "launchpad", "rocket_name"])
    return df
