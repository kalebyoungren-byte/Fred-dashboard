import plotly.graph_objects as go
from fred_client import get_series, get_series_info

# IU brand palette
_CRIMSON  = "#990000"
_CRIMSON2 = "#C8102E"
_GOLD     = "#C8A951"
_NAVY     = "#2C5282"
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
    legend=dict(bgcolor="rgba(0,0,0,0)", bordercolor=_GRID, borderwidth=1),
)


def gdp_chart(years: int = 10) -> go.Figure:
    df = get_series("GDPC1", years)
    info = get_series_info("GDPC1")
    fig = go.Figure(go.Scatter(
        x=df["date"], y=df["value"], mode="lines",
        line=dict(color=_CRIMSON, width=2.5),
        fill="tozeroy", fillcolor="rgba(153,0,0,0.08)",
    ))
    fig.update_layout(**_BASE_LAYOUT, title=info["title"], yaxis_title=info["units"])
    return fig


def unemployment_chart(years: int = 10) -> go.Figure:
    df = get_series("UNRATE", years)
    info = get_series_info("UNRATE")
    fig = go.Figure(go.Scatter(
        x=df["date"], y=df["value"], mode="lines",
        line=dict(color=_CRIMSON2, width=2.5),
        fill="tozeroy", fillcolor="rgba(200,16,46,0.08)",
    ))
    fig.update_layout(**_BASE_LAYOUT, title=info["title"], yaxis_title=info["units"])
    return fig


def inflation_chart(years: int = 10) -> go.Figure:
    cpi = get_series("CPIAUCSL", years)
    pce = get_series("PCEPILFE", years)
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=cpi["date"], y=cpi["value"], name="CPI",
        line=dict(color=_CRIMSON, width=2.5),
    ))
    fig.add_trace(go.Scatter(
        x=pce["date"], y=pce["value"], name="Core PCE",
        line=dict(color=_GOLD, width=2.5, dash="dot"),
    ))
    fig.update_layout(**_BASE_LAYOUT, title="Inflation Indicators (CPI & Core PCE)")
    return fig
