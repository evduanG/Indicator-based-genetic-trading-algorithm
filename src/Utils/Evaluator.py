class Evaluator:
    
    def __init__(self, params, weights = None) -> None:
        self.duration = params['Duration']
        self.equity_final = params['Equity Final [$]']
        self.equity_peak = params['Equity Peak [$]']
        self.return_pct = params['Return [%]']
        self.max_drawdown = params['Max. Drawdown [%]']
        self.sharpe_ratio = params['Sharpe Ratio']
        self.sortino_ratio = params['Sortino Ratio']
        self.calmar_ratio = params['Calmar Ratio']
        self.win_rate = params['Win Rate [%]']
        self.avg_trade_pct = params['Avg. Trade [%]']
        self.max_trade_duration = params['Max. Trade Duration'].days
        self.profit_factor = params['Profit Factor']
        self.sqn = params['SQN']
        self.weights = Evaluator.weights_congif(weights)
    
    def weights_congif(weights):
        is_defullt = weights and weights['return'] and weights['drawdown'] and  weights['drawdown'] and weights['win_rate']
        if is_defullt:
            return weights
        else:
            return {
            'return': 0.35,
            'drawdown': 0.3,
            'risk_adjusted_return': 0.3,
            'win_rate': 0.15,
        }

    def eval(self):
        # Calculate individual scores for each metric
        return_score = self.return_pct / 100 * self.weights['return']
        drawdown_score = (1 - self.max_drawdown / 100) * self.weights['drawdown']
        risk_adjusted_return_score = (self.sharpe_ratio + self.sortino_ratio + self.calmar_ratio) / 3 * self.weights['risk_adjusted_return']
        win_rate_score = self.win_rate / 100 * self.weights['win_rate']
        
        # Calculate the overall strategy score
        strategy_score = return_score + drawdown_score + risk_adjusted_return_score + win_rate_score
        
        # Define some trade-off conditions
        if self.avg_trade_pct < 0:
            trade_off = -0.1  # Penalize strategies with negative average trade return
        else:
            trade_off = 0
        
        if self.max_trade_duration > 10:
            trade_off -= 0.2 * (self.max_trade_duration - 10) # Penalize long trades
        
        if self.equity_final < self.equity_peak:
            trade_off -= 0.2  # Penalize strategies with declining equity
        
        # Apply trade-off conditions
        strategy_score += trade_off
        factor = self.profit_factor  / self.sqn
        # Additional checks and considerations can be added here
        
        return strategy_score *factor
    
    def evaluate_strategy(params):
        if params['# Trades'] < 10:
            return -99999
        
        return Evaluator(params).eval()
        # Extract parameters
        duration = params['Duration']
        equity_final = params['Equity Final [$]']
        equity_peak = params['Equity Peak [$]']
        return_pct = params['Return [%]']
        max_drawdown = params['Max. Drawdown [%]']
        sharpe_ratio = params['Sharpe Ratio']
        sortino_ratio = params['Sortino Ratio']
        calmar_ratio = params['Calmar Ratio']
        win_rate = params['Win Rate [%]']
        avg_trade_pct = params['Avg. Trade [%]']
        max_trade_duration = params['Max. Trade Duration'].days
        profit_factor = params['Profit Factor']
        sqn = params['SQN']


    # # Example usage
    # strategy_params = {
    #     'Duration': 365,
    #     'Equity Final [$]': 12000,
    #     'Equity Peak [$]': 15000,
    #     'Return [%]': 15,
    #     'Max. Drawdown [%]': 10,
    #     'Sharpe Ratio': 1.5,
    #     'Sortino Ratio': 1.2,
    #     'Calmar Ratio': 1.8,
    #     'Win Rate [%]': 60,
    #     'Avg. Trade [%]': 2,
    #     'Max. Trade Duration': pd.Timedelta(days=5),
    #     'Profit Factor': 1.5,
    #     'SQN': 2.0,
    #     '# Trades' : 25
    # }
