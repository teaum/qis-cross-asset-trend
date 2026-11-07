import yfinance as yf
from datetime import date

from config import DATA_DIR

# Equities (SPY, EFA, EEM), Treasuries (IEF, TLT), credit (LQD), gold (GLD), commodities (DBC)
TICKERS = ['SPY', 'EFA', 'IEF', 'EEM', 'TLT', 'LQD', 'GLD', 'DBC']

# As far back as possible; the common history starts with DBC (2006)
START_DATE = "1993-01-01"


def main():
    today = date.today().isoformat()

    # auto_adjust=True: closes adjusted for dividends and splits
    df_ini = yf.download(TICKERS, start=START_DATE, end = today, auto_adjust=True)
    df = df_ini['Close']

    # Dated snapshot, so each backtest can be reproduced
    DATA_DIR.mkdir(exist_ok=True)
    df.to_csv(DATA_DIR / f"prices_{today}.csv")

    print(df.describe())
    print(df.tail())


if __name__ == "__main__":
    main()
