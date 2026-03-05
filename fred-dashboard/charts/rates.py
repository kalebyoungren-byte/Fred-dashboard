import plotly.graph_objects as go
from fred_client import get_series, get_series_info

_CRIMSON  = "#990000"
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


def fed_funds_chart(years: int = 10) -> go.Figure:
    df = get_series("FEDFUNDS", years)
    info = get_series_info("FEDFUNDS")
    fig = go.Figure(go.Scatter(
        x=df["date"], y=df["value"], mode="lines",
        line=dict(color=_CRIMSON, width=2.5),
        fill="tozeroy", fillcolor="rgba(153,0,0,0.08)",
    ))
    fig.update_layout(**_BASE_LAYOUT, title=info["title"], yaxis_title=info["units"])
    return fig


def yield_curve_chart(years: int = 10) -> go.Figure:
    t10 = get_series("DGS10", years)
    t2 = get_series("DGS2", years)

    merged = t10.merge(t2, on="date", suffixes=("_10y", "_2y"))
    spread = merged.copy()
    spread["spread"] = spread["value_10y"] - spread["value_2y"]

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=merged["date"], y=merged["value_10y"], name="10-Year Treasury",
        line=dict(color=_CRIMSON, width=2.5),
    ))
    fig.add_trace(go.Scatter(
        x=merged["date"], y=merged["value_2y"], name="2-Year Treasury",
        line=dict(color=_NAVY, width=2.5),
    ))
    fig.add_trace(go.Scatter(
        x=spread["date"], y=spread["spread"], name="Spread (10Y − 2Y)",
        line=dict(color=_GOLD, width=2, dash="dot"),
    ))
    fig.add_hline(y=0, line_dash="dash", line_color="#999999", opacity=0.6)
    fig.update_layout(**_BASE_LAYOUT, title="Yield Curve — 10Y vs 2Y Treasury", yaxis_title="%")
    return fig


def mortgage_rate_chart(years: int = 10) -> go.Figure:
    df = get_series("MORTGAGE30US", years)
    info = get_series_info("MORTGAGE30US")
    fig = go.Figure(go.Scatter(
        x=df["date"], y=df["value"], mode="lines",
        line=dict(color=_NAVY, width=2.5),
        fill="tozeroy", fillcolor="rgba(44,82,130,0.08)",
    ))
    fig.update_layout(**_BASE_LAYOUT, title=info["title"], yaxis_title=info["units"])
    return fig
