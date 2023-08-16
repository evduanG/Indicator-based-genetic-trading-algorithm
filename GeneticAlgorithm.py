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
import inspect


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

    columns = ["Start","End","Duration","Exposure Time [%]","Equity Final [$]","Equity Peak [$]","Return [%]","Buy & Hold Return [%]","Return (Ann.) [%]","Volatility (Ann.) [%]","Sharpe Ratio","Sortino Ratio","Calmar Ratio","Max. Drawdown [%]","Avg. Drawdown [%]","Max. Drawdown Duration","Avg. Drawdown Duration","# Trades","Win Rate [%]","Best Trade [%]","Worst Trade [%]" ,"Avg. Trade [%]" ,"Max. Trade Duration","Avg. Trade Duration","Profit Factor","_strategy","_equity_curve"]

    def make_arr_tree(num_of_obj = 20 ,is_rec= False):
        name = "r_" if is_rec else "g_"
        return [Tree.make_tree(f"{name}1_no_{i}", is_rec=is_rec) for i in range(0, num_of_obj,1)]

    def __init__(self, num_of_gen, num_of_obj) -> None:
        self.arr = GeneticProgramming.make_arr_tree() + GeneticProgramming.make_arr_tree(True)
        self.num_of_gen = num_of_gen
        self.df =  pd.DataFrame(columns=self.columns)
        self.num_of_obj = num_of_obj
        
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

            arr = arr_sorted[:self.num_of_obj]
            np.random.shuffle(arr)

            for j in range(0,  len(arr), 2):
                _j = 1+ j
                size = len(arr)
                is_over = _j >= size

                if  is_over:
                    new_trees = GeneticProgramming.make_arr_tree(num_of_obj=3)
                    t = new_trees[0]
                    t.right_child = new_trees[1]
                    t.left_child = new_trees[2]
                    t.right_child.parent = t
                    t.left_child.parent = t
                    arr.append(t)
                    arr[j].crossover(arr[j+1])
                    break

                arr[j].crossover(arr[j+1])
            
            self.arr =  arr + top_3 + top_3_mo
            
            for t in arr_sorted[self.num_of_obj:5+ self.num_of_obj]:
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
           
            self.add_to_df(stats)

            if is_polt:
                bt.plot(filename=tree.name)

    def add_to_df(self, stats):
        new_row = {'Start' : stats['Start'],
                'End' : stats['End'],
                'Duration' : stats['Duration'],
                'Exposure Time [%]' : stats['Exposure Time [%]'],
                'Equity Final [$]' : stats['Equity Final [$]'],
                'Equity Peak [$]' : stats['Equity Peak [$]'],
                'Return [%]' : stats['Return [%]'],
                'Buy & Hold Return [%]' : stats['Buy & Hold Return [%]'],
                'Return (Ann.) [%]' : stats['Return (Ann.) [%]'],
                'Volatility (Ann.) [%]' : stats['Volatility (Ann.) [%]'],
                'Sharpe Ratio' : stats['Sharpe Ratio'],
                'Sortino Ratio' : stats['Sortino Ratio'],
                'Calmar Ratio' : stats['Calmar Ratio'],
                'Max. Drawdown [%]' : stats['Max. Drawdown [%]'],
                'Avg. Drawdown [%]' : stats['Avg. Drawdown [%]'],
                'Max. Drawdown Duration' : stats['Max. Drawdown Duration'],
                'Avg. Drawdown Duration' : stats['Avg. Drawdown Duration'],
                '# Trades' : stats['# Trades'],
                'Win Rate [%]' : stats['Win Rate [%]'],
                'Best Trade [%]' : stats['Best Trade [%]'],
                'Worst Trade [%]' : stats['Worst Trade [%]'],
                'Avg. Trade [%]' : stats['Avg. Trade [%]'],
                'Max. Trade Duration' : stats['Max. Trade Duration'],
                'Avg. Trade Duration' : stats['Avg. Trade Duration'],
                'Profit Factor' : stats['Profit Factor'],
                '_strategy' : stats['_strategy'],
                '_equity_curve' : stats['_equity_curve']}
 
        self.df.loc[len(self.df)] = new_row

    def write_top_x_strategy(self, x=3):
        print(f'write top {x} strategy')
        for t in self.arr[:x]:
            t.write_strategy(GOOG)
        
    def write_results(self):
        results = '\n\n'.join([f"name: {str(t.print())}\nres: {str(t.stats)} \nCALAC:{t.to_string()}" for t in self.arr])

        f = open("results.md", "w")
        f.write(results)
        f.close()
        g.df.to_csv("run.csv")



g = GeneticProgramming(num_of_gen=1, num_of_obj=5)
g.run()
g.write_results()
g.write_top_x_strategy()
