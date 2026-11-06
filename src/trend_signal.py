import pandas as pd


def create_signal(prices) :
    last_prices = prices.resample("BME").last()


    last_12_months = last_prices.pct_change(12, fill_method=None)
    last_12_months_pct = last_12_months.dropna()


    signal = last_12_months_pct>0

    signal_final = signal.astype(int)
    return signal_final

