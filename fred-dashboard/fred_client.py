import os
import diskcache
import pandas as pd
from datetime import datetime, timedelta
from fredapi import Fred
from dotenv import load_dotenv
from config import CACHE_DIR, DEFAULT_YEARS

load_dotenv()

_fred = Fred(api_key=os.environ["FRED_API_KEY"])
_cache = diskcache.Cache(CACHE_DIR)


def get_series(series_id: str, years: int = DEFAULT_YEARS) -> pd.DataFrame:
    """Fetch a FRED series, returning a DataFrame with columns [date, value].

    Results are cached to disk for 1 hour to avoid redundant API calls.
    """
    cache_key = f"{series_id}_{years}"
    if cache_key in _cache:
        return _cache[cache_key]

    start = (datetime.today() - timedelta(days=365 * years)).strftime("%Y-%m-%d")
    raw = _fred.get_series(series_id, observation_start=start)

    df = raw.dropna().reset_index()
    df.columns = ["date", "value"]

    _cache.set(cache_key, df, expire=3600)
    return df


def get_series_info(series_id: str) -> dict:
    """Return metadata (title, units, frequency) for a FRED series."""
    info = _fred.get_series_info(series_id)
    return {
        "title": info.get("title", series_id),
        "units": info.get("units_short", ""),
        "frequency": info.get("frequency_short", ""),
    }
