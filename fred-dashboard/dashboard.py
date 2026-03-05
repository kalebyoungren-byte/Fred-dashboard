import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output

from charts.macro import gdp_chart, unemployment_chart, inflation_chart
from charts.rates import fed_funds_chart, yield_curve_chart, mortgage_rate_chart
from charts.housing import housing_starts_chart, home_price_chart

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Indiana University Financial Dashboard"

IU_LOGO = html.Img(
    src="/assets/IU_logo.svg.png",
    alt="Indiana University",
    style={"height": "60px", "width": "auto", "display": "block"},
)

# ------------------------------------------------------------------
# Layout
# ------------------------------------------------------------------
app.layout = html.Div(
    style={"backgroundColor": "#F2EFE8", "minHeight": "100vh"},
    children=[
        # ── Crimson header bar ──────────────────────────────────────
        html.Div(
            id="iu-header",
            children=[
                IU_LOGO,
                html.Div(className="iu-divider"),
                html.Div(
                    className="iu-header-text",
                    children=[
                        html.Span("Indiana University Bloomington", className="iu-university-name"),
                        html.Span("Financial Dashboard", className="iu-dashboard-title"),
                    ],
                ),
            ],
        ),
        # ── Dark accent subheader ───────────────────────────────────
        html.Div(
            id="iu-subheader",
            children="Macroeconomic · Interest Rates · Housing  —  Data: Federal Reserve Bank of St. Louis (FRED)",
        ),
        # ── Main content ────────────────────────────────────────────
        html.Div(
            id="main-content",
            children=[
                dbc.Row(
                    dbc.Col(
                        html.Div(
                            [
                                html.Div("Time Range", className="years-label"),
                                dbc.RadioItems(
                                    id="years-selector",
                                    options=[
                                        {"label": "5 Years", "value": 5},
                                        {"label": "10 Years", "value": 10},
                                        {"label": "20 Years", "value": 20},
                                    ],
                                    value=10,
                                    inline=True,
                                    className="mb-3",
                                ),
                            ]
                        )
                    )
                ),
                dbc.Tabs(
                    [
                        dbc.Tab(label="Macroeconomic", tab_id="macro"),
                        dbc.Tab(label="Interest Rates", tab_id="rates"),
                        dbc.Tab(label="Housing", tab_id="housing"),
                    ],
                    id="tabs",
                    active_tab="macro",
                    className="mb-3",
                ),
                html.Div(id="tab-content"),
            ],
        ),
        # ── Footer ──────────────────────────────────────────────────
        html.Div(
            id="iu-footer",
            children=[
                "© Indiana University · Data sourced from the ",
                html.A("Federal Reserve Economic Data (FRED)", href="https://fred.stlouisfed.org", target="_blank"),
                " · For educational and research purposes only",
            ],
        ),
    ],
)

# ------------------------------------------------------------------
# Callbacks
# ------------------------------------------------------------------
def _chart_col(figure, md=6):
    return dbc.Col(
        html.Div(dcc.Graph(figure=figure, config={"displayModeBar": False}), className="chart-card"),
        md=md,
    )


@app.callback(
    Output("tab-content", "children"),
    Input("tabs", "active_tab"),
    Input("years-selector", "value"),
)
def render_tab(active_tab: str, years: int):
    if active_tab == "macro":
        return dbc.Row([
            _chart_col(gdp_chart(years), md=6),
            _chart_col(unemployment_chart(years), md=6),
            _chart_col(inflation_chart(years), md=12),
        ])
    if active_tab == "rates":
        return dbc.Row([
            _chart_col(fed_funds_chart(years), md=6),
            _chart_col(mortgage_rate_chart(years), md=6),
            _chart_col(yield_curve_chart(years), md=12),
        ])
    if active_tab == "housing":
        return dbc.Row([
            _chart_col(housing_starts_chart(years), md=6),
            _chart_col(home_price_chart(years), md=6),
        ])


if __name__ == "__main__":
    app.run(debug=True)
