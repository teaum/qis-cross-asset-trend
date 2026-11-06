import yfinance as yf
from datetime import date

TICKERS = ['SPY', 'EFA', 'IEF', 'EEM', 'TLT', 'LQD', 'GLD', 'DBC']

START_DATE = "1993-01-01"

today = date.today().isoformat()

df_ini = yf.download(TICKERS, start=START_DATE, end = today, auto_adjust=True)
df = df_ini['Close']
df.to_csv(f"data/prices_{today}.csv")

print(df.describe())
print(df.tail())
