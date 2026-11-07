from config import load_prices


def main():
    prices = load_prices()

    for ticker in prices.columns :
        serie = prices[ticker]
        # Each ETF has its own launch date: ignore the NaNs before it
        premiere_date = serie.first_valid_index()
        serie_valide = serie.loc[premiere_date:]

        # Gaps after launch would mean bad data
        nb_miss = serie_valide.isna().sum()

        # Largest absolute daily move, to spot spikes or bad prints
        daily_return = serie_valide.pct_change(fill_method=None) * 100
        abs_daily_return = daily_return.abs()
        max_return = abs_daily_return.max()
        max_return_date = abs_daily_return.idxmax()

        print(f"{ticker}: start {premiere_date.date()}, missing {nb_miss}, "
              f"max move {max_return:.1f}% on {max_return_date.date()}")


if __name__ == "__main__":
    main()
