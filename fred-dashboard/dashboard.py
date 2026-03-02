import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output

from charts.macro import gdp_chart, unemployment_chart, inflation_chart
from charts.rates import fed_funds_chart, yield_curve_chart, mortgage_rate_chart
from charts.housing import housing_starts_chart, home_price_chart

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])
app.title = "FRED Financial Dashboard"

# ------------------------------------------------------------------
# Layout
# ------------------------------------------------------------------
app.layout = dbc.Container(
    fluid=True,
    children=[
        dbc.Row(
            dbc.Col(html.H2("FRED Financial Dashboard", className="text-center my-3"))
        ),
        dbc.Row(
            dbc.Col(
                dbc.RadioItems(
                    id="years-selector",
                    options=[
                        {"label": "5 Years", "value": 5},
                        {"label": "10 Years", "value": 10},
                        {"label": "20 Years", "value": 20},
                    ],
                    value=10,
                    inline=True,
                    className="mb-3 text-center",
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
)

# ------------------------------------------------------------------
# Callbacks
# ------------------------------------------------------------------
@app.callback(
    Output("tab-content", "children"),
    Input("tabs", "active_tab"),
    Input("years-selector", "value"),
)
def render_tab(active_tab: str, years: int):
    if active_tab == "macro":
        return dbc.Row(
            [
                dbc.Col(dcc.Graph(figure=gdp_chart(years)), md=6),
                dbc.Col(dcc.Graph(figure=unemployment_chart(years)), md=6),
                dbc.Col(dcc.Graph(figure=inflation_chart(years)), md=12),
            ]
        )
    if active_tab == "rates":
        return dbc.Row(
            [
                dbc.Col(dcc.Graph(figure=fed_funds_chart(years)), md=6),
                dbc.Col(dcc.Graph(figure=mortgage_rate_chart(years)), md=6),
                dbc.Col(dcc.Graph(figure=yield_curve_chart(years)), md=12),
            ]
        )
    if active_tab == "housing":
        return dbc.Row(
            [
                dbc.Col(dcc.Graph(figure=housing_starts_chart(years)), md=6),
                dbc.Col(dcc.Graph(figure=home_price_chart(years)), md=6),
            ]
        )


if __name__ == "__main__":
    app.run(debug=True)
