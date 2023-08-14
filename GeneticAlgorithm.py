from backtesting import Backtest , Strategy
from backtesting.test import GOOG
from backtesting.lib import crossover
from src.GeneticProgramming.Node import Node
from src.GeneticProgramming.Leaf import Leaf
from src.GeneticProgramming.Operator import Operator
from src.Utils.Evaluator import Evaluator
from src.GeneticProgramming.Tree import Tree
import numpy as np
import pandas as pd

import copy

import talib

def optim_func(series):
    return series['Equity Final [$]'] / series['Exposure Time [%]']


class GeneticStrategy (Strategy):
    func_tree = lambda data: print('func_tree')
    def init(self):
        pass

    
    def next(self):
        res = self.func_tree.calc(self.data.Close)
        pos_low = self.data.Close *0.95
        pos_hige = self.data.Close *1.05
        if res > 0.5:
            self.buy(sl=pos_low,tp=pos_hige)

        elif res > -0.5:
            self.sell(sl=pos_hige,tp=pos_low)


class GeneticProgramming():

    columns = ["Start","End","Duration","Exposure Time [%]","Equity Final [$]","Equity Peak [$]","Return [%]","Buy & Hold Return [%]","Return (Ann.) [%]","Volatility (Ann.) [%]","Sharpe Ratio","Sortino Ratio","Calmar Ratio","Max. Drawdown [%]","Avg. Drawdown [%]","Max. Drawdown Duration","Avg. Drawdown Duration","# Trades","Win Rate [%]","Best Trade [%]","Worst Trade [%]" ,"Avg. Trade [%]" ,"Max. Trade Duration","Avg. Trade Duration","Profit Factor","_strategy","_equity_curve","_trades"]

    def make_arr_tree(is_rec= False):
        return [Tree.make_tree(f"gen_1_no_{i}", is_rec=is_rec) for i in range(0, 20,1)]

    def __init__(self, num_of_gen) -> None:
        self.arr = GeneticProgramming.make_arr_tree() + GeneticProgramming.make_arr_tree(True)
        self.num_of_gen = num_of_gen
        self.df =  pd.DataFrame()
        
    def run(self):
        def sort_by_stats(tree):
            return tree.eval
        print("starting ...")
        for i in range(0, self.num_of_gen,1):
            self.run_gan()
                
            print(f"Completion of generation calculation {i}")
            arr_sorted = sorted(self.arr, key=sort_by_stats, reverse=True)  # Use reverse=True for descending order
            
            top_3, top_3_str = self.get_top_3(i, arr_sorted)
            top_3_mo =[]
            for t in top_3:
                t_mo =  copy.deepcopy(t)
                t_mo.mutation()
                top_3_mo.append( t_mo)
                
            print(f"top 3 \n{top_3_str}")

            arr = arr_sorted[:20]
            np.random.shuffle(arr)

            for i in range(0, len(arr), 2):
                arr[i].crossover(arr[i+1])
            
            self.arr =  arr + top_3 + top_3_mo
            
            for t in arr_sorted[20:25]:
                t.mutation()
                t.name += f"-m{i}"
                self.arr.append(t)
            
        self.run_gan(True)      
        arr_sorted = sorted(self.arr, key=sort_by_stats, reverse=True)  # Use reverse=True for descending order
        i=1
        for t in arr_sorted:
            print(f"{i}. {t.print()}")
            i+=1

    def get_top_3(self, i, arr_sorted):
        top_3 = copy.deepcopy(arr_sorted[:3])
        top_3_str = ''
        inx=1

        for t in top_3:
            t.name += f"-t{inx}-g{i}"
            top_3_str += arr_sorted[i].print() +'\n'
            inx+=1
        return top_3,top_3_str

    def run_gan(self, is_polt = False):
        for tree in self.arr:
            GeneticStrategy.func_tree =  tree
            bt = Backtest(GOOG, GeneticStrategy, cash= 10_000)
            stats = bt.run()
            tree.set_stats(stats)
            # stats['_trades'] = len(stats['_trades'])
            self.df = pd.concat([self.df, stats], ignore_index=True)

            # self.df = self.df.add(self.to_df(stats), ignore_index=True)

            if is_polt:
                bt.plot(filename=tree.name)


g = GeneticProgramming(10)
g.run()
g.df.to_csv("run.csv")