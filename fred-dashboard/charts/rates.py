import plotly.graph_objects as go
from fred_client import get_series, get_series_info


def fed_funds_chart(years: int = 10) -> go.Figure:
    df = get_series("FEDFUNDS", years)
    info = get_series_info("FEDFUNDS")
    fig = go.Figure(go.Scatter(x=df["date"], y=df["value"], mode="lines", line=dict(color="#4CAF50", width=2)))
    fig.update_layout(title=info["title"], yaxis_title=info["units"], template="plotly_dark", hovermode="x unified")
    return fig


def yield_curve_chart(years: int = 10) -> go.Figure:
    t10 = get_series("DGS10", years)
    t2 = get_series("DGS2", years)

    # Align on common dates
    merged = t10.merge(t2, on="date", suffixes=("_10y", "_2y"))
    spread = merged.copy()
    spread["spread"] = spread["value_10y"] - spread["value_2y"]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=merged["date"], y=merged["value_10y"], name="10-Year", line=dict(color="#2196F3")))
    fig.add_trace(go.Scatter(x=merged["date"], y=merged["value_2y"], name="2-Year", line=dict(color="#FF5722")))
    fig.add_trace(go.Scatter(x=spread["date"], y=spread["spread"], name="Spread (10Y-2Y)", line=dict(color="#FFEB3B", dash="dot")))
    fig.add_hline(y=0, line_dash="dash", line_color="red", opacity=0.5)
    fig.update_layout(title="Yield Curve (10Y vs 2Y Treasury)", yaxis_title="%", template="plotly_dark", hovermode="x unified")
    return fig


def mortgage_rate_chart(years: int = 10) -> go.Figure:
    df = get_series("MORTGAGE30US", years)
    info = get_series_info("MORTGAGE30US")
    fig = go.Figure(go.Scatter(x=df["date"], y=df["value"], mode="lines", line=dict(color="#00BCD4", width=2)))
    fig.update_layout(title=info["title"], yaxis_title=info["units"], template="plotly_dark", hovermode="x unified")
    return fig
