from src.GeneticProgramming.INode import INode
import talib
import random

class Leaf(INode):
    def __init__(self, parent, function, str):
        self.function = function
        self.parent = parent
        self.str = str
    
    def mutation(self):
        pass

    def get_crossover(self):
        return self, self.parent

    def crossover(self, tree_a, tree_b):
        pass

    def calc(self, data, is_to_str= False):
        if is_to_str:
            return self.to_string()
        return self.function(data)

    def visit(self):
        pass
    
    def inorder(self):
        return self.visit()

    def to_string(self):
        return self.str
    
    

    # def make_leaf(name):
    #     def make_bbands():
    #         def bbands(timeperiod, nbdevup, nbdevdn, matype,  func_cala):
    #             def res(data):
    #                 upperband, middleband, lowerband = talib.BBANDS(data, timeperiod=timeperiod, nbdevup=nbdevup, nbdevdn=nbdevdn, matype=matype)
    #                 return func_cala(upperband, middleband ,lowerband)[-1]

    #             return res
    #         make_var = lambda: random.randrange(3, 21, 1)

    #         timeperiod = make_var()
    #         nbdevup = make_var()
    #         nbdevdn = make_var()
    #         matype = 0
    #         type_func = random.randrange(0, 3, 1)
            
    #         if type_func == 0:
    #             func_calc = lambda u, m, l: 1- ((u - m) /l)

    #             return bbands(timeperiod, nbdevup, nbdevdn, matype, func_calc)
    #         elif type_func == 1:
    #             func_calc = lambda u, m, l: 1- ((u - l) /m)
    #             return bbands(timeperiod, nbdevup, nbdevdn, matype, func_calc)
    #         else:
    #             func_calc = lambda u, m, l: 1- ((m - l) /(u - m))
    #             return bbands(timeperiod, nbdevup, nbdevdn, matype, func_calc)  
             
    #     def make_rsi():
    #         def rsi(timeperiod, upper_bound, lower_bound, weight):
    #             def res(data):
    #                 rsi = talib.RSI(data, timeperiod=timeperiod)
    #                 if rsi[-1] < lower_bound:
    #                     return -weight
    #                 elif rsi[-1] > upper_bound:
    #                     return weight
    #                 return 0
                    
    #             return res

    #         timeperiod = random.randrange(3, 28, 1)
    #         upper_bound = random.randrange(65, 94, 1)
    #         lower_bound = random.randrange(5, 44, 1)
    #         weight = random.randrange(50, 200, 1)/100
    #         return rsi(timeperiod, upper_bound, lower_bound, weight)

    #     def make_ema_sma():
    #         def ema_sma(ema_timeperiod, sma_timeperiod, weight):
    #             def res(data):
    #                 ema = talib.EMA(data, ema_timeperiod)
    #                 sma = talib.SMA(data, sma_timeperiod)
                    
    #                 if data[-1] > ema[-1] and data[-1] > sma[-1]:
    #                     return weight
    #                 elif data[-1] < ema[-1] and data[-1] < sma[-1]:
    #                     return -weight

    #                 return 0
    #             return res

    #         ema_timeperiod = random.randrange(3, 21, 1)
    #         sma_timeperiod = random.randrange(3, 21, 1)
    #         weight = random.randrange(50, 200, 1)/100
            
    #         return ema_sma(ema_timeperiod, sma_timeperiod, weight)

    #     def make_ema():
    #         def ema(t1, t2, t3, weight):
    #             def res(data):
    #                 ema_low = talib.EMA(data, timeperiod=t1)
    #                 ema_mid = talib.EMA(data, timeperiod=t2)
    #                 ema_hight = talib.EMA(data, timeperiod=t3)
                    
    #                 if ema_hight[-1] > ema_low[-1]:
    #                     return -weight
    #                 elif ema_hight[-1] < ema_low[-1]:
    #                     return weight
    #                 elif ema_hight[-1] > ema_mid[-1]:
    #                     return -0.5 * weight
    #                 elif ema_mid[-1] < ema_low[-1]:
    #                     return 0.5* weight
    #                 return 0
    #             return res

    #         t1 = random.randrange(3, 7, 1)
    #         t2 = random.randrange(t1+2, 16, 1)
    #         t3 = random.randrange(t2+2, 28, 1)

    #         weight = random.randrange(50, 200, 1)/100
    #         return ema(t1, t2, t3, weight)

    #     def make_sma():
    #         def sma(t1, t2, t3, weight):
    #             def res(data):
    #                 sma_low = talib.EMA(data, timeperiod=t1)
    #                 sma_mid = talib.EMA(data, timeperiod=t2)
    #                 sma_hight = talib.EMA(data, timeperiod=t3)
                    
    #                 if sma_hight[-1] > sma_low[-1]:
    #                     return -weight
    #                 elif sma_hight[-1] < sma_low[-1]:
    #                     return weight
    #                 elif sma_hight[-1] > sma_mid[-1]:
    #                     return -0.5 * weight
    #                 elif sma_mid[-1] < sma_low[-1]:
    #                     return 0.5* weight
    #                 return 0
    #             return res

    #         t1 = random.randrange(3, 7, 1)
    #         t2 = random.randrange(t1+2, 16, 1)
    #         t3 = random.randrange(t2+2, 28, 1)

    #         weight = random.randrange(50, 200, 1)/100
    #         return sma(t1, t2, t3, weight)
        
    #     list_of_action = [make_bbands, make_rsi, make_ema, make_sma, make_ema_sma]
    #     action = lambda: random.choice(list_of_action)
