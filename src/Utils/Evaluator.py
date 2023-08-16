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
        drop_pack_final = self.equity_peak / self.equity_peak

        # Calculate individual scores for each metric
        return_score = self.return_pct * self.weights['return']
        drawdown_score = (1 -self.max_drawdown) * self.weights['drawdown']
        risk_adjusted_return_score = (self.sharpe_ratio + self.sortino_ratio + self.calmar_ratio) / 3 * self.weights['risk_adjusted_return']
        win_rate_score = self.win_rate * self.weights['win_rate']
        
        # Calculate the overall strategy score
        strategy_score = return_score + drawdown_score + risk_adjusted_return_score 
        
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
        # strategy_score += trade_off
        # factor = self.profit_factor  / self.sqn
        # Additional checks and considerations can be added here
        
        return drop_pack_final * (strategy_score +  win_rate_score * self.avg_trade_pct)
    
    def evaluate_strategy(params):
        not_good_res = -99999
        if params['# Trades'] < 10:
            return not_good_res
        elif  params['Return [%]'] < 0:
            return 2* not_good_res
        
        return Evaluator(params).eval()