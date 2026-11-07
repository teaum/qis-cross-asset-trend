import matplotlib.pyplot as plt
import pandas as pd

from config import load_prices
from trend_signal import create_signal
from backtest import weight_signals, compute_daily_returns, compute_daily_weights, compute_indice
from metrics import compute_annualized_returns, compute_annualized_volatility, compute_sharpe_ratio, compute_max_drawdown, compute_calmar

# How each metric is printed
FORMATS = {
    "Ann. return": "{:.2%}",
    "Volatility": "{:.2%}",
    "Sharpe (rf 0)": "{:.2f}",
    "Max drawdown": "{:.2%}",
    "Calmar": "{:.2f}",
}


def compute_metrics(indice):
    # Headline metrics for one index level series
    annu_returns = compute_annualized_returns(indice)
    annu_vol = compute_annualized_volatility(indice)
    max_drawdown = compute_max_drawdown(indice)
    return {
        "Ann. return": annu_returns,
        "Volatility": annu_vol,
        "Sharpe (rf 0)": compute_sharpe_ratio(annu_returns, annu_vol),
        "Max drawdown": max_drawdown,
        "Calmar": compute_calmar(annu_returns, max_drawdown),
    }


def main():
    prices = load_prices()
    daily_returns = compute_daily_returns(prices)

    # Trend index: 12-month momentum, long/flat
    signal = create_signal(prices)
    weights = weight_signals(signal)
    daily_weights = compute_daily_weights(weights, daily_returns)
    indice = compute_indice(daily_weights, daily_returns)

    # Benchmark: same ETFs and dates, always invested (signal = 1 everywhere)
    signal_benchmark = pd.DataFrame(1, index=signal.index, columns=signal.columns)
    weights_benchmark = weight_signals(signal_benchmark)
    daily_weights_benchmark = compute_daily_weights(weights_benchmark, daily_returns)
    indice_benchmark = compute_indice(daily_weights_benchmark, daily_returns)

    # Side-by-side metrics table
    results = {"Trend": compute_metrics(indice), "Equal weight": compute_metrics(indice_benchmark)}
    table = pd.DataFrame({
        name: {k: FORMATS[k].format(v) for k, v in metrics.items()}
        for name, metrics in results.items()
    })
    print(f"Backtest {indice.index[0].date()} to {indice.index[-1].date()}\n")
    print(table.to_string())

    plt.plot(indice, label="Indice")
    plt.plot(indice_benchmark, label="Équipondéré")
    plt.title("Trend vs équipondéré (base 100)")
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()
