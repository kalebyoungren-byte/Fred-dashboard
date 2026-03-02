import plotly.graph_objects as go
from fred_client import get_series, get_series_info


def gdp_chart(years: int = 10) -> go.Figure:
    df = get_series("GDPC1", years)
    info = get_series_info("GDPC1")
    fig = go.Figure(go.Scatter(x=df["date"], y=df["value"], mode="lines", line=dict(color="#2196F3", width=2)))
    fig.update_layout(title=info["title"], yaxis_title=info["units"], template="plotly_dark", hovermode="x unified")
    return fig


def unemployment_chart(years: int = 10) -> go.Figure:
    df = get_series("UNRATE", years)
    info = get_series_info("UNRATE")
    fig = go.Figure(go.Scatter(x=df["date"], y=df["value"], mode="lines", line=dict(color="#F44336", width=2)))
    fig.update_layout(title=info["title"], yaxis_title=info["units"], template="plotly_dark", hovermode="x unified")
    return fig


def inflation_chart(years: int = 10) -> go.Figure:
    cpi = get_series("CPIAUCSL", years)
    pce = get_series("PCEPILFE", years)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=cpi["date"], y=cpi["value"], name="CPI", line=dict(color="#FF9800")))
    fig.add_trace(go.Scatter(x=pce["date"], y=pce["value"], name="Core PCE", line=dict(color="#9C27B0")))
    fig.update_layout(title="Inflation Indicators", template="plotly_dark", hovermode="x unified")
    return fig
