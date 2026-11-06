import pandas as pd

prices = pd.read_csv("data/prices_2026-11-02.csv", index_col=0, parse_dates=True)




for ticker in prices.columns :
    serie = prices[ticker]
    premiere_date = serie.first_valid_index()
    print(premiere_date)

    serie_valide = serie.loc[premiere_date:]
    nb_miss = serie_valide.isna().sum()
    print(nb_miss)


    daily_return = serie_valide.pct_change(fill_method=None) * 100
    abs_daily_return = daily_return.abs()

    max_return = abs_daily_return.max()
    max_return_date = abs_daily_return.idxmax()

    print(max_return)
    print(max_return_date)