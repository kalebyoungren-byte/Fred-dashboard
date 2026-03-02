import plotly.graph_objects as go
from fred_client import get_series, get_series_info


def housing_starts_chart(years: int = 10) -> go.Figure:
    df = get_series("HOUST", years)
    info = get_series_info("HOUST")
    fig = go.Figure(go.Bar(x=df["date"], y=df["value"], marker_color="#8BC34A"))
    fig.update_layout(title=info["title"], yaxis_title=info["units"], template="plotly_dark")
    return fig


def home_price_chart(years: int = 10) -> go.Figure:
    df = get_series("CSUSHPISA", years)
    info = get_series_info("CSUSHPISA")
    fig = go.Figure(go.Scatter(x=df["date"], y=df["value"], mode="lines", line=dict(color="#FF5722", width=2)))
    fig.update_layout(title=info["title"], yaxis_title=info["units"], template="plotly_dark", hovermode="x unified")
    return fig
