from pathlib import Path

import pandas as pd

# Repo root, so the scripts work from any working directory
ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"

# Price snapshot used by every script (change it here only)
PRICES_FILE = DATA_DIR / "prices_2026-11-02.csv"


def load_prices(path=PRICES_FILE):
    # Daily dividend-adjusted closes, one column per ETF
    return pd.read_csv(path, index_col=0, parse_dates=True)
