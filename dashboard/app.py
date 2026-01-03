import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

import plotly.express as px
from dash import Dash, dcc, html, Input, Output

from src.data_loader import load_spacex_data
from src.features import success_rate_by_site, success_over_time


# Load data
df = load_spacex_data()

# App
app = Dash(__name__)
server = app.server

# Layout
app.layout = html.Div([
    html.H1(
        "SpaceX Falcon 9 Landing Success Dashboard",
        style={"textAlign": "center"}
    ),

    html.Div([
        dcc.Dropdown(
            id="site-dropdown",
            options=[
                {"label": site, "value": site}
                for site in sorted(df["launchpad"].unique())
            ],
            value=sorted(df["launchpad"].unique())[0],
            clearable=False
        )
    ], style={"width": "50%", "margin": "auto"}),

    dcc.Graph(id="success-rate-site"),
    dcc.Graph(id="success-over-time")
])


# Callbacks
@app.callback(
    Output("success-rate-site", "figure"),
    Input("site-dropdown", "value")
)
def update_site_chart(site):
    success_rate = success_rate_by_site(df, site)

    fig = px.bar(
        x=["Failure", "Success"],
        y=[1 - success_rate, success_rate],
        labels={"x": "Outcome", "y": "Rate"},
        title=f"Landing Success Rate – {site}"
    )
    fig.update_yaxes(range=[0, 1])

    return fig


@app.callback(
    Output("success-over-time", "figure"),
    Input("site-dropdown", "value")
)
def update_time_chart(site):
    yearly = success_over_time(df, site)

    fig = px.line(
        yearly,
        x="launch_year",
        y="landing_success",
        markers=True,
        title="Landing Success Rate Over Time"
    )
    fig.update_yaxes(range=[0, 1])

    return fig


if __name__ == "__main__":
    app.run(debug=True)
