# Cross-Asset Trend Index (QIS)

A systematic, rules-based index built on time-series momentum across asset classes, backtested in Python.

> Work in progress. The backtest does not yet include transaction costs, so results are preliminary.

## Index rules (current version)

- **Universe**: 8 ETFs covering equities, bonds, credit, gold and commodities: SPY, EFA, EEM, IEF, TLT, LQD, GLD, DBC.
- **Signal**: each month-end, an ETF is held if its 12-month return is positive, otherwise it is out (long/flat).
- **Weights**: 1/8 per ETF with a positive signal; the remainder sits in cash and earns the 3-month T-bill rate.
- **Rebalancing**: monthly. The signal uses the month-end close; trades execute at the next day's close, so new weights earn returns from the day after (no look-ahead).
- **Index level**: I_t = I_{t-1} × (1 + Σ w_i,t × r_i,t + w_cash,t × r_cash,t), base 100 on 2007-03-01, with w_cash = 1 − Σ w_i.
- **Sharpe ratio**: computed on daily returns in excess of the T-bill rate, annualised.
- **Benchmark**: the same 8 ETFs equally weighted and always invested, which isolates the value of the trend signal.

## Data

Daily dividend-adjusted closes from Yahoo Finance (`yfinance`, `auto_adjust=True`). The common history starts in February 2006 (DBC launch), so the first full 12-month signal is February 2007. The cash rate is the 13-week T-bill yield (`^IRX`), converted to a daily return and lagged by one day. Data is not committed; `src/download_data.py` writes dated snapshots to `data/`.

## Project structure

| File | Role |
|---|---|
| `src/config.py` | Data paths and the price and T-bill snapshots used by every script |
| `src/download_data.py` | Downloads ETF prices and the T-bill yield, saves dated CSV snapshots |
| `src/check_data.py` | Data quality checks: start dates, missing values, largest daily moves |
| `src/trend_signal.py` | Monthly 12-month momentum signal (0/1 per ETF) |
| `src/backtest.py` | Signal to weights, daily weights with execution lag, index level |
| `src/metrics.py` | Annualised return, volatility, Sharpe, max drawdown, Calmar |
| `src/run.py` | Runs the full pipeline and plots the index against the benchmark |

## Run it

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/download_data.py
python src/run.py
```

## Roadmap

- T-bill return as the signal threshold (12-month excess return > 0)
- Transaction costs and index fee
- 60/40 benchmark
- Inverse-volatility weighting and volatility targeting
- One-page rulebook
