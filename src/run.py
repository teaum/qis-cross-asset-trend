from trend_signal import create_signal
import matplotlib.pyplot as plt
import pandas as pd

from backtest import weight_signals, compute_daily_returns, compute_daily_weights, compute_indice
from metrics import compute_annualized_returns, compute_annualized_volatility, compute_sharpe_ratio, compute_max_drawdown, compute_calmar


prices = pd.read_csv("data/prices_2026-11-02.csv", index_col=0, parse_dates=True)

signal = create_signal(prices)

weights = weight_signals(signal)
daily_returns = compute_daily_returns(prices)
daily_weights = compute_daily_weights(weights, daily_returns)
indice = compute_indice(daily_weights,daily_returns)
print(indice.loc["2008":"2009"].min())

signal_benchmark = pd.DataFrame(1, index=signal.index, columns=signal.columns)
weights_benchmark = weight_signals(signal_benchmark)
daily_weights_benchmark = compute_daily_weights(weights_benchmark, daily_returns)
indice_benchmark = compute_indice(daily_weights_benchmark,daily_returns)



annu_returns = compute_annualized_returns(indice)
annu_returns_benchmark = compute_annualized_returns(indice_benchmark)
annu_vol = compute_annualized_volatility(indice)
annu_vol_benchmark = compute_annualized_volatility(indice_benchmark)

max_drawdown = compute_max_drawdown(indice)
max_drawdown_benchmark = compute_max_drawdown(indice_benchmark)

print(max_drawdown)
print(max_drawdown_benchmark)

calmar = compute_calmar(annu_returns, max_drawdown)
calmar_benchmark = compute_calmar(annu_returns_benchmark, max_drawdown_benchmark)

print(calmar)
print(calmar_benchmark)







plt.plot(indice, label="Indice")
plt.plot(indice_benchmark, label="Équipondéré")
plt.title("Trend vs équipondéré (base 100)")
plt.legend()
plt.grid()
plt.show()

