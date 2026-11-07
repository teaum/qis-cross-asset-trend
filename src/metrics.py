
def compute_annualized_returns(indice) :
    # Geometric annual return, 252 trading days per year
    end_price = indice.iloc[-1]
    start_price = 100
    return (end_price/start_price)**(252/len(indice)) - 1


def compute_annualized_volatility(indice) :
    # Std of daily returns, scaled by sqrt(252)
    daily_returns = indice.pct_change(fill_method=None)
    deviation = daily_returns.std()
    return deviation * 252**0.5

def compute_sharpe_ratio(returns, vol):
    # rf = 0 for now: no cash return in the index yet
    return returns/vol

def compute_max_drawdown(indice) :
    # Worst fall from a previous peak (negative number)
    maximum = indice.cummax()
    return (indice/maximum - 1).min()

def compute_calmar(returns, drawdown) :
    # Annual return per unit of max drawdown
    return abs(returns/drawdown)


