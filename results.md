name: name: g_1_no_2, eval -199998
res: Start                     2004-08-19 00:00:00
End                       2013-03-01 00:00:00
Duration                   3116 days 00:00:00
Exposure Time [%]                   70.204842
Equity Final [$]                     458.5225
Equity Peak [$]                       10000.0
Return [%]                         -95.414775
Buy & Hold Return [%]              703.458242
Return (Ann.) [%]                  -30.344899
Volatility (Ann.) [%]                21.88561
Sharpe Ratio                              0.0
Sortino Ratio                             0.0
Calmar Ratio                              0.0
Max. Drawdown [%]                  -95.554415
Avg. Drawdown [%]                  -95.554415
Max. Drawdown Duration     3115 days 00:00:00
Avg. Drawdown Duration     3115 days 00:00:00
# Trades                                  391
Win Rate [%]                        40.920716
Best Trade [%]                      20.434293
Worst Trade [%]                    -14.503311
Avg. Trade [%]                       -0.83602
Max. Trade Duration          42 days 00:00:00
Avg. Trade Duration           7 days 00:00:00
Profit Factor                        0.728877
Expectancy [%]                      -0.709884
SQN                                  -3.21181
_strategy                     GeneticStrategy
_equity_curve                             ...
_trades                        Size  Entry...
dtype: object 
CALAC:tree operator: Operator.NOT_OR, is_rec: False, parent: None
	right_child:
operator: Operator.SMALLER, is_rec: False, parent: parent
	right_child:
ema:
	 t1:6
	 t2: 10
	 t3: 24
	 weight 1.87
	left_child:
bbands:
	timeperiod:3
	nbdevup: 4
	nbdevdn:9
	type_func:1
	left_child:
operator: Operator.XNOR, is_rec: False, parent: parent
	right_child:
rsi:
	timeperiod:12
	upper_bound: 75
	lower_bound: 21
	weight: 1.37
	left_child:
ema:
	 t1:5
	 t2: 11
	 t3: 13
	 weight 1.48

name: name: g_1_no_6, eval 159.57860200678556
res: Start                     2004-08-19 00:00:00
End                       2013-03-01 00:00:00
Duration                   3116 days 00:00:00
Exposure Time [%]                    99.90689
Equity Final [$]                    47592.192
Equity Peak [$]                    75215.6115
Return [%]                          375.92192
Buy & Hold Return [%]              703.458242
Return (Ann.) [%]                   20.084631
Volatility (Ann.) [%]               45.046058
Sharpe Ratio                         0.445869
Sortino Ratio                         0.82215
Calmar Ratio                         0.238544
Max. Drawdown [%]                  -84.196642
Avg. Drawdown [%]                   -7.708536
Max. Drawdown Duration     1908 days 00:00:00
Avg. Drawdown Duration       82 days 00:00:00
# Trades                                  472
Win Rate [%]                        52.330508
Best Trade [%]                      20.434293
Worst Trade [%]                    -13.790276
Avg. Trade [%]                       0.292536
Max. Trade Duration          56 days 00:00:00
Avg. Trade Duration           8 days 00:00:00
Profit Factor                        1.208919
Expectancy [%]                       0.412152
SQN                                  1.064448
_strategy                     GeneticStrategy
_equity_curve                            E...
_trades                        Size  Entry...
dtype: object 
CALAC:tree operator: Operator.SMALLER, is_rec: False, parent: None
	right_child:
operator: Operator.XNOR, is_rec: False, parent: parent
	right_child:
rsi:
	timeperiod:12
	upper_bound: 75
	lower_bound: 21
	weight: 1.37
	left_child:
ema:
	 t1:5
	 t2: 11
	 t3: 13
	 weight 1.48
	left_child:
operator: Operator.XOR, is_rec: False, parent: parent
	right_child:
rsi:
	timeperiod:14
	upper_bound: 83
	lower_bound: 5
	weight: 1.54
	left_child:
ema sma:
	 ema_timeperiod:15
	 sma_timeperiod: 4
	 weight: 1.64

name: name: g_1_no_10, eval 605.7561591457226
res: Start                     2004-08-19 00:00:00
End                       2013-03-01 00:00:00
Duration                   3116 days 00:00:00
Exposure Time [%]                    99.90689
Equity Final [$]                  176432.1225
Equity Peak [$]                   257398.5345
Return [%]                        1664.321225
Buy & Hold Return [%]              703.458242
Return (Ann.) [%]                   40.038207
Volatility (Ann.) [%]               53.440749
Sharpe Ratio                         0.749207
Sortino Ratio                        1.645556
Calmar Ratio                         0.710895
Max. Drawdown [%]                  -56.320831
Avg. Drawdown [%]                   -7.070093
Max. Drawdown Duration      584 days 00:00:00
Avg. Drawdown Duration       45 days 00:00:00
# Trades                                  623
Win Rate [%]                        56.982343
Best Trade [%]                      16.824919
Worst Trade [%]                    -15.305102
Avg. Trade [%]                       0.671192
Max. Trade Duration          58 days 00:00:00
Avg. Trade Duration           9 days 00:00:00
Profit Factor                        1.420455
Expectancy [%]                       0.796771
SQN                                  1.659555
_strategy                     GeneticStrategy
_equity_curve                             ...
_trades                        Size  Entry...
dtype: object 
CALAC:tree operator: Operator.AND, is_rec: False, parent: None
	right_child:
operator: Operator.SUB, is_rec: False, parent: parent
	right_child:
ema:
	 t1:5
	 t2: 14
	 t3: 20
	 weight 1.28
	left_child:
ema:
	 t1:6
	 t2: 8
	 t3: 19
	 weight 1.29
	left_child:
operator: Operator.OR, is_rec: False, parent: parent
	right_child:
ema sma:
	 ema_timeperiod:20
	 sma_timeperiod: 11
	 weight: 1.97
	left_child:
ema:
	 t1:6
	 t2: 9
	 t3: 21
	 weight 1.15

name: name: g_1_no_9, eval 636.1928960976177
res: Start                     2004-08-19 00:00:00
End                       2013-03-01 00:00:00
Duration                   3116 days 00:00:00
Exposure Time [%]                    99.90689
Equity Final [$]                   185605.874
Equity Peak [$]                    209302.425
Return [%]                         1756.05874
Buy & Hold Return [%]              703.458242
Return (Ann.) [%]                   40.873465
Volatility (Ann.) [%]               53.519536
Sharpe Ratio                         0.763711
Sortino Ratio                        1.666285
Calmar Ratio                         0.800397
Max. Drawdown [%]                  -51.066489
Avg. Drawdown [%]                    -6.39504
Max. Drawdown Duration      505 days 00:00:00
Avg. Drawdown Duration       40 days 00:00:00
# Trades                                  539
Win Rate [%]                        56.215213
Best Trade [%]                      14.503311
Worst Trade [%]                    -20.434293
Avg. Trade [%]                       0.667595
Max. Trade Duration          56 days 00:00:00
Avg. Trade Duration           8 days 00:00:00
Profit Factor                        1.416057
Expectancy [%]                       0.794275
SQN                                  1.941907
_strategy                     GeneticStrategy
_equity_curve                             ...
_trades                        Size  Entry...
dtype: object 
CALAC:tree operator: Operator.AND, is_rec: False, parent: None
	right_child:
operator: Operator.OR, is_rec: False, parent: parent
	right_child:
ema sma:
	 ema_timeperiod:20
	 sma_timeperiod: 11
	 weight: 1.97
	left_child:
ema:
	 t1:6
	 t2: 9
	 t3: 21
	 weight 1.15
	left_child:
operator: Operator.SMALLER, is_rec: False, parent: parent
	right_child:
rsi:
	timeperiod:16
	upper_bound: 66
	lower_bound: 24
	weight: 1.61
	left_child:
bbands:
	timeperiod:19
	nbdevup: 9
	nbdevdn:11
	type_func:1

name: name: g_1_no_14, eval 98.0684251621237
res: Start                     2004-08-19 00:00:00
End                       2013-03-01 00:00:00
Duration                   3116 days 00:00:00
Exposure Time [%]                    99.90689
Equity Final [$]                    31175.809
Equity Peak [$]                    57774.2955
Return [%]                          211.75809
Buy & Hold Return [%]              703.458242
Return (Ann.) [%]                   14.270446
Volatility (Ann.) [%]               43.073533
Sharpe Ratio                         0.331304
Sortino Ratio                         0.57305
Calmar Ratio                         0.213686
Max. Drawdown [%]                  -66.782455
Avg. Drawdown [%]                   -8.721284
Max. Drawdown Duration     1942 days 00:00:00
Avg. Drawdown Duration       87 days 00:00:00
# Trades                                  500
Win Rate [%]                             55.0
Best Trade [%]                      20.434293
Worst Trade [%]                    -13.435428
Avg. Trade [%]                       0.425037
Max. Trade Duration          56 days 00:00:00
Avg. Trade Duration           8 days 00:00:00
Profit Factor                        1.290647
Expectancy [%]                        0.53907
SQN                                   0.68031
_strategy                     GeneticStrategy
_equity_curve                            E...
_trades                        Size  Entry...
dtype: object 
CALAC:tree operator: Operator.AND, is_rec: False, parent: None
	right_child:
operator: Operator.AND, is_rec: False, parent: parent
	right_child:
ema:
	 t1:5
	 t2: 8
	 t3: 17
	 weight 1.81
	left_child:
ema:
	 t1:6
	 t2: 8
	 t3: 10
	 weight 1.0
	left_child:
tree operator: Operator.NOT_OR, is_rec: False, parent: parent
	right_child:
operator: Operator.OR, is_rec: False, parent: parent
	right_child:
ema sma:
	 ema_timeperiod:12
	 sma_timeperiod: 19
	 weight: 0.7
	left_child:
rsi:
	timeperiod:15
	upper_bound: 68
	lower_bound: 34
	weight: 1.39
	left_child:
operator: Operator.SMALLER, is_rec: False, parent: parent
	right_child:
rsi:
	timeperiod:12
	upper_bound: 89
	lower_bound: 22
	weight: 1.04
	left_child:
ema sma:
	 ema_timeperiod:6
	 sma_timeperiod: 6
	 weight: 1.12

name: name: g_1_no_0, eval -199998
res: Start                     2004-08-19 00:00:00
End                       2013-03-01 00:00:00
Duration                   3116 days 00:00:00
Exposure Time [%]                    99.90689
Equity Final [$]                       807.18
Equity Peak [$]                    11496.0425
Return [%]                           -91.9282
Buy & Hold Return [%]              703.458242
Return (Ann.) [%]                  -25.566665
Volatility (Ann.) [%]               25.054513
Sharpe Ratio                              0.0
Sortino Ratio                             0.0
Calmar Ratio                              0.0
Max. Drawdown [%]                  -92.984368
Avg. Drawdown [%]                  -24.352454
Max. Drawdown Duration     3101 days 00:00:00
Avg. Drawdown Duration      778 days 00:00:00
# Trades                                  467
Win Rate [%]                         42.61242
Best Trade [%]                      12.373936
Worst Trade [%]                    -20.434293
Avg. Trade [%]                       -0.74005
Max. Trade Duration          56 days 00:00:00
Avg. Trade Duration           8 days 00:00:00
Profit Factor                        0.770377
Expectancy [%]                      -0.606995
SQN                                  -3.15929
_strategy                     GeneticStrategy
_equity_curve                           Eq...
_trades                        Size  Entry...
dtype: object 
CALAC:tree operator: Operator.NOT_OR, is_rec: False, parent: None
	right_child:
tree operator: Operator.NOT_OR, is_rec: False, parent: parent
	right_child:
operator: Operator.BIGGER, is_rec: False, parent: parent
	right_child:
ema sma:
	 ema_timeperiod:17
	 sma_timeperiod: 6
	 weight: 1.36
	left_child:
bbands:
	timeperiod:17
	nbdevup: 12
	nbdevdn:15
	type_func:2
	left_child:
operator: Operator.OR, is_rec: False, parent: parent
	right_child:
rsi:
	timeperiod:20
	upper_bound: 66
	lower_bound: 7
	weight: 1.0
	left_child:
ema sma:
	 ema_timeperiod:19
	 sma_timeperiod: 18
	 weight: 1.81
	left_child:
operator: Operator.BIGGER, is_rec: False, parent: parent
	right_child:
ema:
	 t1:4
	 t2: 14
	 t3: 24
	 weight 1.23
	left_child:
ema:
	 t1:5
	 t2: 9
	 t3: 27
	 weight 1.7

name: name: g_1_no_2-t1-g0, eval 780.7602247676217
res: Start                     2004-08-19 00:00:00
End                       2013-03-01 00:00:00
Duration                   3116 days 00:00:00
Exposure Time [%]                    99.90689
Equity Final [$]                  226746.9445
Equity Peak [$]                   325680.9325
Return [%]                        2167.469445
Buy & Hold Return [%]              703.458242
Return (Ann.) [%]                   44.221498
Volatility (Ann.) [%]               54.751985
Sharpe Ratio                         0.807669
Sortino Ratio                        1.787751
Calmar Ratio                         0.813533
Max. Drawdown [%]                  -54.357369
Avg. Drawdown [%]                   -6.000793
Max. Drawdown Duration      584 days 00:00:00
Avg. Drawdown Duration       38 days 00:00:00
# Trades                                  606
Win Rate [%]                        56.270627
Best Trade [%]                      13.790276
Worst Trade [%]                    -20.434293
Avg. Trade [%]                       0.615811
Max. Trade Duration          58 days 00:00:00
Avg. Trade Duration           9 days 00:00:00
Profit Factor                        1.386095
Expectancy [%]                       0.743122
SQN                                  1.858416
_strategy                     GeneticStrategy
_equity_curve                             ...
_trades                        Size  Entry...
dtype: object 
CALAC:tree operator: Operator.NOT_OR, is_rec: False, parent: None
	right_child:
operator: Operator.AND, is_rec: False, parent: parent
	right_child:
bbands:
	timeperiod:18
	nbdevup: 15
	nbdevdn:11
	type_func:2
	left_child:
ema sma:
	 ema_timeperiod:16
	 sma_timeperiod: 15
	 weight: 1.83
	left_child:
operator: Operator.XNOR, is_rec: False, parent: parent
	right_child:
rsi:
	timeperiod:12
	upper_bound: 75
	lower_bound: 21
	weight: 1.37
	left_child:
ema:
	 t1:5
	 t2: 11
	 t3: 13
	 weight 1.48

name: name: g_1_no_9-t2-g0, eval 605.7561591457226
res: Start                     2004-08-19 00:00:00
End                       2013-03-01 00:00:00
Duration                   3116 days 00:00:00
Exposure Time [%]                    99.90689
Equity Final [$]                  176432.1225
Equity Peak [$]                   257398.5345
Return [%]                        1664.321225
Buy & Hold Return [%]              703.458242
Return (Ann.) [%]                   40.038207
Volatility (Ann.) [%]               53.440749
Sharpe Ratio                         0.749207
Sortino Ratio                        1.645556
Calmar Ratio                         0.710895
Max. Drawdown [%]                  -56.320831
Avg. Drawdown [%]                   -7.070093
Max. Drawdown Duration      584 days 00:00:00
Avg. Drawdown Duration       45 days 00:00:00
# Trades                                  623
Win Rate [%]                        56.982343
Best Trade [%]                      16.824919
Worst Trade [%]                    -15.305102
Avg. Trade [%]                       0.671192
Max. Trade Duration          58 days 00:00:00
Avg. Trade Duration           9 days 00:00:00
Profit Factor                        1.420455
Expectancy [%]                       0.796771
SQN                                  1.659555
_strategy                     GeneticStrategy
_equity_curve                             ...
_trades                        Size  Entry...
dtype: object 
CALAC:tree operator: Operator.AND, is_rec: False, parent: None
	right_child:
operator: Operator.SUB, is_rec: False, parent: parent
	right_child:
ema:
	 t1:5
	 t2: 14
	 t3: 20
	 weight 1.28
	left_child:
ema:
	 t1:6
	 t2: 8
	 t3: 19
	 weight 1.29
	left_child:
operator: Operator.SMALLER, is_rec: False, parent: parent
	right_child:
rsi:
	timeperiod:16
	upper_bound: 66
	lower_bound: 24
	weight: 1.61
	left_child:
bbands:
	timeperiod:19
	nbdevup: 9
	nbdevdn:11
	type_func:1

name: name: g_1_no_10-t3-g0, eval 598.1740430672545
res: Start                     2004-08-19 00:00:00
End                       2013-03-01 00:00:00
Duration                   3116 days 00:00:00
Exposure Time [%]                    99.90689
Equity Final [$]                   175311.749
Equity Peak [$]                     184390.76
Return [%]                         1653.11749
Buy & Hold Return [%]              703.458242
Return (Ann.) [%]                   39.933586
Volatility (Ann.) [%]                53.34038
Sharpe Ratio                         0.748656
Sortino Ratio                        1.595443
Calmar Ratio                         0.801177
Max. Drawdown [%]                  -49.843635
Avg. Drawdown [%]                   -6.279901
Max. Drawdown Duration      560 days 00:00:00
Avg. Drawdown Duration       39 days 00:00:00
# Trades                                  586
Win Rate [%]                        55.460751
Best Trade [%]                      13.315685
Worst Trade [%]                    -20.434293
Avg. Trade [%]                        0.48266
Max. Trade Duration          58 days 00:00:00
Avg. Trade Duration           9 days 00:00:00
Profit Factor                        1.303258
Expectancy [%]                        0.61158
SQN                                  2.260345
_strategy                     GeneticStrategy
_equity_curve                             ...
_trades                        Size  Entry...
dtype: object 
CALAC:tree operator: Operator.AND, is_rec: False, parent: None
	right_child:
operator: Operator.ADD, is_rec: False, parent: parent
	right_child:
ema sma:
	 ema_timeperiod:10
	 sma_timeperiod: 5
	 weight: 1.35
	left_child:
ema sma:
	 ema_timeperiod:7
	 sma_timeperiod: 16
	 weight: 1.69
	left_child:
operator: Operator.OR, is_rec: False, parent: parent
	right_child:
ema sma:
	 ema_timeperiod:20
	 sma_timeperiod: 11
	 weight: 1.97
	left_child:
ema:
	 t1:6
	 t2: 9
	 t3: 21
	 weight 1.15

name: name: g_1_no_2-t1-g0, eval -199998
res: Start                     2004-08-19 00:00:00
End                       2013-03-01 00:00:00
Duration                   3116 days 00:00:00
Exposure Time [%]                   58.193669
Equity Final [$]                      435.806
Equity Peak [$]                      10972.81
Return [%]                          -95.64194
Buy & Hold Return [%]              703.458242
Return (Ann.) [%]                  -30.758892
Volatility (Ann.) [%]               20.168788
Sharpe Ratio                              0.0
Sortino Ratio                             0.0
Calmar Ratio                              0.0
Max. Drawdown [%]                   -96.02831
Avg. Drawdown [%]                  -70.559277
Max. Drawdown Duration     2935 days 00:00:00
Avg. Drawdown Duration     1557 days 00:00:00
# Trades                                  358
Win Rate [%]                        38.268156
Best Trade [%]                      20.434293
Worst Trade [%]                    -13.790276
Avg. Trade [%]                      -0.963402
Max. Trade Duration          42 days 00:00:00
Avg. Trade Duration           6 days 00:00:00
Profit Factor                        0.683574
Expectancy [%]                      -0.839392
SQN                                 -2.465413
_strategy                     GeneticStrategy
_equity_curve                            E...
_trades                        Size  Entry...
dtype: object 
CALAC:tree operator: Operator.XOR, is_rec: False, parent: None
	right_child:
operator: Operator.AND, is_rec: False, parent: parent
	right_child:
bbands:
	timeperiod:18
	nbdevup: 15
	nbdevdn:11
	type_func:2
	left_child:
ema sma:
	 ema_timeperiod:16
	 sma_timeperiod: 15
	 weight: 1.83
	left_child:
operator: Operator.XNOR, is_rec: False, parent: parent
	right_child:
rsi:
	timeperiod:12
	upper_bound: 75
	lower_bound: 21
	weight: 1.37
	left_child:
ema:
	 t1:5
	 t2: 11
	 t3: 13
	 weight 1.48

name: name: g_1_no_9-t2-g0, eval 605.7561591457226
res: Start                     2004-08-19 00:00:00
End                       2013-03-01 00:00:00
Duration                   3116 days 00:00:00
Exposure Time [%]                    99.90689
Equity Final [$]                  176432.1225
Equity Peak [$]                   257398.5345
Return [%]                        1664.321225
Buy & Hold Return [%]              703.458242
Return (Ann.) [%]                   40.038207
Volatility (Ann.) [%]               53.440749
Sharpe Ratio                         0.749207
Sortino Ratio                        1.645556
Calmar Ratio                         0.710895
Max. Drawdown [%]                  -56.320831
Avg. Drawdown [%]                   -7.070093
Max. Drawdown Duration      584 days 00:00:00
Avg. Drawdown Duration       45 days 00:00:00
# Trades                                  623
Win Rate [%]                        56.982343
Best Trade [%]                      16.824919
Worst Trade [%]                    -15.305102
Avg. Trade [%]                       0.671192
Max. Trade Duration          58 days 00:00:00
Avg. Trade Duration           9 days 00:00:00
Profit Factor                        1.420455
Expectancy [%]                       0.796771
SQN                                  1.659555
_strategy                     GeneticStrategy
_equity_curve                             ...
_trades                        Size  Entry...
dtype: object 
CALAC:tree operator: Operator.AND, is_rec: False, parent: None
	right_child:
operator: Operator.SUB, is_rec: False, parent: parent
	right_child:
ema:
	 t1:5
	 t2: 14
	 t3: 20
	 weight 1.28
	left_child:
ema:
	 t1:6
	 t2: 8
	 t3: 19
	 weight 1.29
	left_child:
operator: Operator.SMALLER, is_rec: False, parent: parent
	right_child:
rsi:
	timeperiod:16
	upper_bound: 66
	lower_bound: 24
	weight: 1.61
	left_child:
bbands:
	timeperiod:19
	nbdevup: 9
	nbdevdn:11
	type_func:1

name: name: g_1_no_10-t3-g0, eval 277.54955039034047
res: Start                     2004-08-19 00:00:00
End                       2013-03-01 00:00:00
Duration                   3116 days 00:00:00
Exposure Time [%]                   80.540037
Equity Final [$]                   82643.0585
Equity Peak [$]                    82710.3785
Return [%]                         726.430585
Buy & Hold Return [%]              703.458242
Return (Ann.) [%]                   28.116545
Volatility (Ann.) [%]               39.086502
Sharpe Ratio                         0.719342
Sortino Ratio                         1.41502
Calmar Ratio                         0.490947
Max. Drawdown [%]                  -57.269996
Avg. Drawdown [%]                    -5.61422
Max. Drawdown Duration     1347 days 00:00:00
Avg. Drawdown Duration       57 days 00:00:00
# Trades                                  305
Win Rate [%]                        56.721311
Best Trade [%]                       13.39192
Worst Trade [%]                    -14.192626
Avg. Trade [%]                       0.652937
Max. Trade Duration          48 days 00:00:00
Avg. Trade Duration           9 days 00:00:00
Profit Factor                        1.417504
Expectancy [%]                       0.774842
SQN                                  2.390445
_strategy                     GeneticStrategy
_equity_curve                             ...
_trades                        Size  Entry...
dtype: object 
CALAC:tree operator: Operator.SUB, is_rec: False, parent: None
	right_child:
operator: Operator.ADD, is_rec: False, parent: parent
	right_child:
ema sma:
	 ema_timeperiod:10
	 sma_timeperiod: 5
	 weight: 1.35
	left_child:
ema sma:
	 ema_timeperiod:7
	 sma_timeperiod: 16
	 weight: 1.69
	left_child:
operator: Operator.OR, is_rec: False, parent: parent
	right_child:
ema sma:
	 ema_timeperiod:20
	 sma_timeperiod: 11
	 weight: 1.97
	left_child:
ema:
	 t1:6
	 t2: 9
	 t3: 21
	 weight 1.15

name: name: g_1_no_16-m0, eval 287.50762971631343
res: Start                     2004-08-19 00:00:00
End                       2013-03-01 00:00:00
Duration                   3116 days 00:00:00
Exposure Time [%]                    99.90689
Equity Final [$]                   86013.8335
Equity Peak [$]                   135542.0135
Return [%]                         760.138335
Buy & Hold Return [%]              703.458242
Return (Ann.) [%]                   28.718832
Volatility (Ann.) [%]                48.98795
Sharpe Ratio                         0.586243
Sortino Ratio                        1.149755
Calmar Ratio                         0.497096
Max. Drawdown [%]                  -57.773189
Avg. Drawdown [%]                  -10.634446
Max. Drawdown Duration      616 days 00:00:00
Avg. Drawdown Duration       72 days 00:00:00
# Trades                                  585
Win Rate [%]                        54.700855
Best Trade [%]                      14.503311
Worst Trade [%]                    -20.434293
Avg. Trade [%]                       0.439231
Max. Trade Duration          58 days 00:00:00
Avg. Trade Duration           9 days 00:00:00
Profit Factor                        1.278333
Expectancy [%]                       0.570788
SQN                                  1.200825
_strategy                     GeneticStrategy
_equity_curve                             ...
_trades                        Size  Entry...
dtype: object 
CALAC:tree operator: Operator.XOR, is_rec: False, parent: None
	right_child:
operator: Operator.ADD, is_rec: False, parent: parent
	right_child:
ema:
	 t1:6
	 t2: 13
	 t3: 25
	 weight 1.22
	left_child:
ema:
	 t1:3
	 t2: 7
	 t3: 18
	 weight 1.93
	left_child:
operator: Operator.SUB, is_rec: False, parent: parent
	right_child:
ema:
	 t1:4
	 t2: 7
	 t3: 26
	 weight 1.49
	left_child:
bbands:
	timeperiod:17
	nbdevup: 5
	nbdevdn:20
	type_func:0

name: name: g_1_no_4-m0, eval 270.31286804204933
res: Start                     2004-08-19 00:00:00
End                       2013-03-01 00:00:00
Duration                   3116 days 00:00:00
Exposure Time [%]                   67.364991
Equity Final [$]                    81234.892
Equity Peak [$]                     81300.892
Return [%]                          712.34892
Buy & Hold Return [%]              703.458242
Return (Ann.) [%]                   27.858493
Volatility (Ann.) [%]               35.223978
Sharpe Ratio                         0.790896
Sortino Ratio                        1.568115
Calmar Ratio                         0.710676
Max. Drawdown [%]                  -39.200015
Avg. Drawdown [%]                   -5.982232
Max. Drawdown Duration      685 days 00:00:00
Avg. Drawdown Duration       51 days 00:00:00
# Trades                                  233
Win Rate [%]                        60.085837
Best Trade [%]                      13.315685
Worst Trade [%]                     -9.558306
Avg. Trade [%]                       0.956828
Max. Trade Duration          54 days 00:00:00
Avg. Trade Duration           9 days 00:00:00
Profit Factor                        1.597457
Expectancy [%]                       1.078451
SQN                                  2.314559
_strategy                     GeneticStrategy
_equity_curve                            E...
_trades                        Size  Entry...
dtype: object 
CALAC:tree operator: Operator.ADD, is_rec: False, parent: None
	right_child:
operator: Operator.ADD, is_rec: False, parent: parent
	right_child:
ema:
	 t1:6
	 t2: 8
	 t3: 14
	 weight 1.48
	left_child:
ema:
	 t1:3
	 t2: 13
	 t3: 16
	 weight 0.54
	left_child:
operator: Operator.ADD, is_rec: False, parent: parent
	right_child:
bbands:
	timeperiod:18
	nbdevup: 4
	nbdevdn:9
	type_func:0
	left_child:
ema sma:
	 ema_timeperiod:20
	 sma_timeperiod: 20
	 weight: 1.39

name: name: g_1_no_0-m0, eval 152.9247494647198
res: Start                     2004-08-19 00:00:00
End                       2013-03-01 00:00:00
Duration                   3116 days 00:00:00
Exposure Time [%]                    99.90689
Equity Final [$]                    46825.814
Equity Peak [$]                     46825.814
Return [%]                          368.25814
Buy & Hold Return [%]              703.458242
Return (Ann.) [%]                   19.856141
Volatility (Ann.) [%]               44.688662
Sharpe Ratio                         0.444322
Sortino Ratio                        0.830208
Calmar Ratio                         0.294299
Max. Drawdown [%]                  -67.469179
Avg. Drawdown [%]                   -7.533966
Max. Drawdown Duration     1575 days 00:00:00
Avg. Drawdown Duration       83 days 00:00:00
# Trades                                  510
Win Rate [%]                        53.333333
Best Trade [%]                      20.434293
Worst Trade [%]                    -10.273165
Avg. Trade [%]                       0.417095
Max. Trade Duration          56 days 00:00:00
Avg. Trade Duration           8 days 00:00:00
Profit Factor                        1.275314
Expectancy [%]                       0.539919
SQN                                  1.632134
_strategy                     GeneticStrategy
_equity_curve                            E...
_trades                        Size  Entry...
dtype: object 
CALAC:tree operator: Operator.AND, is_rec: False, parent: None
	right_child:
operator: Operator.OR, is_rec: False, parent: parent
	right_child:
bbands:
	timeperiod:18
	nbdevup: 6
	nbdevdn:5
	type_func:2
	left_child:
ema:
	 t1:6
	 t2: 9
	 t3: 11
	 weight 1.47
	left_child:
operator: Operator.AND, is_rec: False, parent: parent
	right_child:
rsi:
	timeperiod:10
	upper_bound: 79
	lower_bound: 21
	weight: 1.97
	left_child:
bbands:
	timeperiod:18
	nbdevup: 7
	nbdevdn:11
	type_func:0

name: name: g_1_no_5-m0, eval 129.57919883628924
res: Start                     2004-08-19 00:00:00
End                       2013-03-01 00:00:00
Duration                   3116 days 00:00:00
Exposure Time [%]                   98.743017
Equity Final [$]                   39032.7255
Equity Peak [$]                    59944.6855
Return [%]                         290.327255
Buy & Hold Return [%]              703.458242
Return (Ann.) [%]                   17.323635
Volatility (Ann.) [%]               44.713006
Sharpe Ratio                         0.387441
Sortino Ratio                        0.686954
Calmar Ratio                         0.204923
Max. Drawdown [%]                  -84.537321
Avg. Drawdown [%]                   -8.123873
Max. Drawdown Duration     1942 days 00:00:00
Avg. Drawdown Duration       84 days 00:00:00
# Trades                                  396
Win Rate [%]                        51.515152
Best Trade [%]                      20.434293
Worst Trade [%]                    -11.491559
Avg. Trade [%]                       0.281539
Max. Trade Duration          56 days 00:00:00
Avg. Trade Duration           8 days 00:00:00
Profit Factor                        1.195311
Expectancy [%]                       0.411625
SQN                                   1.07115
_strategy                     GeneticStrategy
_equity_curve                             ...
_trades                        Size  Entry...
dtype: object 
CALAC:tree operator: Operator.SUB, is_rec: False, parent: None
	right_child:
operator: Operator.XNOR, is_rec: False, parent: parent
	right_child:
rsi:
	timeperiod:17
	upper_bound: 87
	lower_bound: 13
	weight: 1.68
	left_child:
ema:
	 t1:6
	 t2: 12
	 t3: 27
	 weight 1.13
	left_child:
operator: Operator.SUB, is_rec: False, parent: parent
	right_child:
ema:
	 t1:6
	 t2: 8
	 t3: 12
	 weight 1.01
	left_child:
rsi:
	timeperiod:19
	upper_bound: 65
	lower_bound: 26
	weight: 1.01

name: name: g_1_no_19-m0, eval 128.56914959001455
res: Start                     2004-08-19 00:00:00
End                       2013-03-01 00:00:00
Duration                   3116 days 00:00:00
Exposure Time [%]                   99.860335
Equity Final [$]                    38710.839
Equity Peak [$]                     60142.254
Return [%]                          287.10839
Buy & Hold Return [%]              703.458242
Return (Ann.) [%]                   17.209712
Volatility (Ann.) [%]               45.451029
Sharpe Ratio                         0.378643
Sortino Ratio                        0.671363
Calmar Ratio                         0.205388
Max. Drawdown [%]                  -83.791108
Avg. Drawdown [%]                   -8.543435
Max. Drawdown Duration     1942 days 00:00:00
Avg. Drawdown Duration       90 days 00:00:00
# Trades                                  411
Win Rate [%]                        51.581509
Best Trade [%]                      20.434293
Worst Trade [%]                    -13.790276
Avg. Trade [%]                       0.325484
Max. Trade Duration          56 days 00:00:00
Avg. Trade Duration           8 days 00:00:00
Profit Factor                        1.219514
Expectancy [%]                       0.454599
SQN                                  0.983534
_strategy                     GeneticStrategy
_equity_curve                            E...
_trades                        Size  Entry...
dtype: object 
CALAC:tree operator: Operator.SMALLER, is_rec: False, parent: None
	right_child:
operator: Operator.SMALLER, is_rec: False, parent: parent
	right_child:
bbands:
	timeperiod:3
	nbdevup: 20
	nbdevdn:8
	type_func:2
	left_child:
rsi:
	timeperiod:25
	upper_bound: 77
	lower_bound: 40
	weight: 0.74
	left_child:
operator: Operator.SMALLER, is_rec: False, parent: parent
	right_child:
rsi:
	timeperiod:27
	upper_bound: 92
	lower_bound: 29
	weight: 1.63
	left_child:
ema:
	 t1:3
	 t2: 10
	 t3: 14
	 weight 1.13