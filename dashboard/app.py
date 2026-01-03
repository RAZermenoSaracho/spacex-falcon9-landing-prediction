import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

import plotly.express as px
import plotly.io as pio
from dash import Dash, dcc, html, Input, Output

from src.data_loader import load_spacex_data

# ------------------------------------------------------------------
# CONFIG
# ------------------------------------------------------------------

pio.templates.default = "plotly_dark"

df = load_spacex_data()
LAUNCH_SITES = sorted(df["launchpad"].unique().tolist())

# ------------------------------------------------------------------
# APP
# ------------------------------------------------------------------

app = Dash(__name__)
server = app.server

# ------------------------------------------------------------------
# HELPERS
# ------------------------------------------------------------------

def empty_fig(title: str):
    fig = px.scatter(title=title)
    fig.update_layout(
        autosize=True,
        margin=dict(l=12, r=12, t=60, b=40),
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        annotations=[
            dict(
                text=title,
                x=0.5,
                y=0.5,
                xref="paper",
                yref="paper",
                showarrow=False,
                font=dict(size=14),
            )
        ],
    )
    return fig

# ------------------------------------------------------------------
# LAYOUT
# ------------------------------------------------------------------

app.layout = html.Div(
    className="container",
    children=[
        html.H1(
            "🚀 SpaceX Falcon 9 Landing Success Dashboard",
            className="title"
        ),

        # ---------------- Controls ----------------
        html.Div(className="controls", children=[

            html.Div(className="control-group", children=[
                html.Label("Launch Site", className="control-label"),
                dcc.Dropdown(
                    id="site-dropdown",
                    options=[{"label": s, "value": s} for s in LAUNCH_SITES],
                    value=LAUNCH_SITES[0],
                    clearable=False
                )
            ]),

            html.Div(className="control-group", children=[
                html.Label("Rocket", className="control-label"),
                dcc.Dropdown(
                    id="rocket-dropdown",
                    clearable=False
                )
            ]),
        ]),

        # ---------------- KPIs ----------------
        html.Div(className="kpi-container", children=[
            html.Div(className="kpi-card", children=[
                html.H3("Success Rate"),
                html.H2(id="kpi-success-rate"),
            ]),
            html.Div(className="kpi-card", children=[
                html.H3("Total Launches"),
                html.H2(id="kpi-total-launches"),
            ]),
            html.Div(className="kpi-card", children=[
                html.H3("Launch Years"),
                html.H2(id="kpi-years"),
            ]),
        ]),

        # ---------------- Charts ----------------
        html.Div(className="charts", children=[
            dcc.Graph(
                id="success-rate-site",
                responsive=True,
                style={"width": "100%", "height": "100%"},
                figure=empty_fig("Loading chart…")
            ),
            dcc.Graph(
                id="success-over-time",
                responsive=True,
                style={"width": "100%", "height": "100%"},
                figure=empty_fig("Loading chart…")
            ),
        ]),
    ]
)

# ------------------------------------------------------------------
# CALLBACKS
# ------------------------------------------------------------------

# Update rocket dropdown when site changes
@app.callback(
    Output("rocket-dropdown", "options"),
    Output("rocket-dropdown", "value"),
    Input("site-dropdown", "value"),
)
def update_rocket_dropdown(site):
    rockets = sorted(
        df[df["launchpad"] == site]["rocket_name"].unique().tolist()
    )

    if not rockets:
        return [], None

    return (
        [{"label": r, "value": r} for r in rockets],
        rockets[0],
    )


# Success rate bar chart
@app.callback(
    Output("success-rate-site", "figure"),
    Input("site-dropdown", "value"),
    Input("rocket-dropdown", "value"),
)
def update_success_rate_chart(site, rocket):

    if not site or not rocket:
        return empty_fig("Select a Launch Site and Rocket")

    filtered = df[
        (df["launchpad"] == site) &
        (df["rocket_name"] == rocket)
    ]

    if filtered.empty:
        return empty_fig("No data for this selection")

    success_rate = filtered["landing_success"].mean()

    fig = px.bar(
        x=["Failure", "Success"],
        y=[1 - success_rate, success_rate],
        labels={"x": "Outcome", "y": "Rate"},
        title=f"Landing Success Rate – {rocket}",
    )

    fig.update_yaxes(range=[0, 1])
    fig.update_layout(
        autosize=True,
        margin=dict(l=12, r=12, t=60, b=40),
    )

    return fig


# Success over time line chart
@app.callback(
    Output("success-over-time", "figure"),
    Input("site-dropdown", "value"),
    Input("rocket-dropdown", "value"),
)
def update_success_over_time(site, rocket):

    if not site or not rocket:
        return empty_fig("Select a Launch Site and Rocket")

    filtered = df[
        (df["launchpad"] == site) &
        (df["rocket_name"] == rocket)
    ]

    if filtered.empty:
        return empty_fig("No data for this selection")

    yearly = (
        filtered.groupby("launch_year")["landing_success"]
        .mean()
        .reset_index()
    )

    fig = px.line(
        yearly,
        x="launch_year",
        y="landing_success",
        markers=True,
        title="Landing Success Rate Over Time",
    )

    fig.update_yaxes(range=[0, 1])
    fig.update_layout(
        autosize=True,
        margin=dict(l=12, r=12, t=60, b=40),
    )

    return fig


# KPIs
@app.callback(
    Output("kpi-success-rate", "children"),
    Output("kpi-total-launches", "children"),
    Output("kpi-years", "children"),
    Input("site-dropdown", "value"),
    Input("rocket-dropdown", "value"),
)
def update_kpis(site, rocket):

    if not site or not rocket:
        return "-", "-", "-"

    filtered = df[
        (df["launchpad"] == site) &
        (df["rocket_name"] == rocket)
    ]

    if filtered.empty:
        return "-", "0", "0"

    return (
        f"{filtered['landing_success'].mean() * 100:.1f}%",
        str(filtered.shape[0]),
        str(filtered["launch_year"].nunique()),
    )

# ------------------------------------------------------------------
# CLIENTSIDE RESIZE (safe + isolated)
# ------------------------------------------------------------------

@app.callback(
    Output("resize-trigger", "data"),
    Input("site-dropdown", "value"),
    Input("rocket-dropdown", "value"),
)
def trigger_resize(site, rocket):
    return {"key": f"{site}-{rocket}"}

# ------------------------------------------------------------------
# RUN
# ------------------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=False)
