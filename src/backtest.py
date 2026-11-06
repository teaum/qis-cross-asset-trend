import pandas as pd

def weight_signals(signal) :
    n = len(signal.columns)
    return signal * 1/n


def compute_daily_returns(price) :
    daily_return = price.pct_change(fill_method=None)
    return daily_return


def compute_daily_weights(weights, daily_returns) :
    daily_weights = weights.reindex(daily_returns.index, method="ffill")
    daily_weights = daily_weights.shift(2)
    return daily_weights

def compute_indice(daily_weights, daily_returns) :
    indice_returns = daily_weights * daily_returns
    premiere_date = indice_returns.first_valid_index()
    serie_valide = indice_returns.loc[premiere_date:]
    returns = serie_valide.sum(axis=1)
    indice_price = (1 + returns).cumprod() * 100
    return indice_price

