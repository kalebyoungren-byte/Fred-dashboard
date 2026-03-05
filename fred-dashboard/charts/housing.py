import plotly.graph_objects as go
from fred_client import get_series, get_series_info

_CRIMSON  = "#990000"
_GOLD     = "#C8A951"
_CREAM    = "#F2EFE8"
_GRID     = "#E0D8CE"

_BASE_LAYOUT = dict(
    template="plotly_white",
    paper_bgcolor=_CREAM,
    plot_bgcolor="#FFFFFF",
    font=dict(family="Arial, sans-serif", color="#333333", size=12),
    title_font=dict(family="Georgia, serif", color=_CRIMSON, size=15),
    hovermode="x unified",
    xaxis=dict(gridcolor=_GRID, linecolor="#cccccc", showgrid=True),
    yaxis=dict(gridcolor=_GRID, linecolor="#cccccc", showgrid=True),
    margin=dict(l=60, r=20, t=50, b=40),
)


def housing_starts_chart(years: int = 10) -> go.Figure:
    df = get_series("HOUST", years)
    info = get_series_info("HOUST")
    fig = go.Figure(go.Bar(
        x=df["date"], y=df["value"],
        marker_color=_CRIMSON,
        marker_opacity=0.85,
    ))
    fig.update_layout(**_BASE_LAYOUT, title=info["title"], yaxis_title=info["units"])
    return fig


def home_price_chart(years: int = 10) -> go.Figure:
    df = get_series("CSUSHPISA", years)
    info = get_series_info("CSUSHPISA")
    fig = go.Figure(go.Scatter(
        x=df["date"], y=df["value"], mode="lines",
        line=dict(color=_GOLD, width=2.5),
        fill="tozeroy", fillcolor="rgba(200,169,81,0.12)",
    ))
    fig.update_layout(**_BASE_LAYOUT, title=info["title"], yaxis_title=info["units"])
    return fig
