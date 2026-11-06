
def compute_annualized_returns(indice) :
    end_price = indice.iloc[-1]
    start_price = 100
    return (end_price/start_price)**(252/len(indice)) - 1


def compute_annualized_volatility(indice) :
    daily_returns = indice.pct_change(fill_method=None)
    deviation = daily_returns.std()
    return deviation * 252**0.5

def compute_sharpe_ratio(returns, vol):
    return returns/vol

def compute_max_drawdown(indice) :
    maximum = indice.cummax()
    return (indice/maximum - 1).min()

def compute_calmar(returns, drawdown) :
    return abs(returns/drawdown)


