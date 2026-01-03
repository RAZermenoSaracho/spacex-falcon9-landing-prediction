def success_rate_by_site(df, site):
    """
    Compute landing success rate for a given launch site.
    """
    filtered = df[df["launchpad"] == site]
    return filtered["landing_success"].mean()


def success_over_time(df, site):
    """
    Compute yearly landing success rate for a given launch site.
    """
    filtered = df[df["launchpad"] == site]

    return (
        filtered.groupby("launch_year")["landing_success"]
        .mean()
        .reset_index()
    )
