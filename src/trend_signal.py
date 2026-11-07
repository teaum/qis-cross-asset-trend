import pandas as pd


def create_signal(prices) :
    # Month-end closes (last business day of each month)
    last_prices = prices.resample("BME").last()


    # 12-month return; the first 12 months have no signal yet
    last_12_months = last_prices.pct_change(12, fill_method=None)
    last_12_months_pct = last_12_months.dropna()


    # Long if the 12-month return is positive, flat otherwise
    signal = last_12_months_pct>0

    signal_final = signal.astype(int)
    return signal_final

