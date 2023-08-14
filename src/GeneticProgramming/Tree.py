from .Operator import Operator, rend_operator
from .Node import Node
from .Leaf import Leaf
from src.Utils.Evaluator import Evaluator


import talib
import random

class Tree(Node):

    def __init__(self, operator: Operator,name = None , right_child=None, left_child=None, parent=None, border=0.5):
        super().__init__(operator, right_child, left_child, parent, border)
        self.stats = None
        self.name = name
    
    # def __init__(self, tree):
    #     super().__init__(tree.operator, tree.right_child, tree.left_child, tree.parent, tree.border)
    #     self.stats = tree.stats
    #     self.name = tree.name

    def make_tree(name, is_rec=False):
        def make_bbands():
            def bbands(timeperiod, nbdevup, nbdevdn, matype,  func_cala):
                def res(data):
                    upperband, middleband, lowerband = talib.BBANDS(data, timeperiod=timeperiod, nbdevup=nbdevup, nbdevdn=nbdevdn, matype=matype)
                    return func_cala(upperband, middleband ,lowerband)[-1]

                return res

            timeperiod = random.randrange(3, 21, 1)
            nbdevup = random.randrange(3, 21, 1)
            nbdevdn = random.randrange(3, 21, 1)
            matype = 0
            type_func = random.randrange(0, 3, 1)

            str = f"bbands:\n\ttimeperiod:{timeperiod}\n\tnbdevup: {nbdevup}\n\tnbdevdn:{nbdevdn}\n\ttype_func:{type_func}"
            if type_func == 0:
                func_calc = lambda u, m, l: 1- ((u - m) /l)
            elif type_func == 1:
                func_calc = lambda u, m, l: 1- ((u - l) /m)
            else:
                func_calc = lambda u, m, l: 1- ((m - l) /(u - m))
            return bbands(timeperiod, nbdevup, nbdevdn, matype, func_calc)  ,str
             
        def make_rsi():
            def rsi(timeperiod, upper_bound, lower_bound, weight):
                
                def res(data):
                    rsi = talib.RSI(data, timeperiod=timeperiod)
                    if rsi[-1] < lower_bound:
                        return -weight
                    elif rsi[-1] > upper_bound:
                        return weight
                    return 0
                    
                return res

            timeperiod = random.randrange(3, 28, 1)
            upper_bound = random.randrange(65, 94, 1)
            lower_bound = random.randrange(5, 44, 1)
            weight = random.randrange(50, 200, 1)/100
            str = f"rsi:\n\ttimeperiod:{timeperiod}\n\tupper_bound: {upper_bound}\n\tlower_bound: {lower_bound}\n\tweight: {weight}"

            return rsi(timeperiod, upper_bound, lower_bound, weight), str

        def make_ema_sma():
            def ema_sma(ema_timeperiod, sma_timeperiod, weight):
                def res(data):
                    ema = talib.EMA(data, ema_timeperiod)
                    sma = talib.SMA(data, sma_timeperiod)
                    
                    if data[-1] > ema[-1] and data[-1] > sma[-1]:
                        return weight
                    elif data[-1] < ema[-1] and data[-1] < sma[-1]:
                        return -weight

                    return 0
                return res

            ema_timeperiod = random.randrange(3, 21, 1)
            sma_timeperiod = random.randrange(3, 21, 1)
            weight = random.randrange(50, 200, 1)/100
            str = f"ema sma:\n\t ema_timeperiod:{ema_timeperiod}\n\t sma_timeperiod: {sma_timeperiod}\n\t weight: {weight}"

            return ema_sma(ema_timeperiod, sma_timeperiod, weight), str


        def make_ema():
            def ema(t1, t2, t3, weight):
                def res(data):
                    ema_low = talib.EMA(data, timeperiod=t1)
                    ema_mid = talib.EMA(data, timeperiod=t2)
                    ema_hight = talib.EMA(data, timeperiod=t3)
                    
                    if ema_hight[-1] > ema_low[-1]:
                        return -weight
                    elif ema_hight[-1] < ema_low[-1]:
                        return weight
                    elif ema_hight[-1] > ema_mid[-1]:
                        return -0.5 * weight
                    elif ema_mid[-1] < ema_low[-1]:
                        return 0.5* weight
                    return 0
                return res

            t1 = random.randrange(3, 7, 1)
            t2 = random.randrange(t1+2, 16, 1)
            t3 = random.randrange(t2+2, 28, 1)
            weight = random.randrange(50, 200, 1)/100
            str = f"ema:\n\t t1:{t1}\n\t t2: {t2}\n\t t3: {t3}\n\t weight {weight}"

            return ema(t1, t2, t3, weight), str

        def make_sma():
            def sma(t1, t2, t3, weight):
                def res(data):
                    sma_low = talib.EMA(data, timeperiod=t1)
                    sma_mid = talib.EMA(data, timeperiod=t2)
                    sma_hight = talib.EMA(data, timeperiod=t3)
                    
                    if sma_hight[-1] > sma_low[-1]:
                        return -weight
                    elif sma_hight[-1] < sma_low[-1]:
                        return weight
                    elif sma_hight[-1] > sma_mid[-1]:
                        return -0.5 * weight
                    elif sma_mid[-1] < sma_low[-1]:
                        return 0.5* weight
                    return 0
                return res

            t1 = random.randrange(3, 7, 1)
            t2 = random.randrange(t1+2, 16, 1)
            t3 = random.randrange(t2+2, 28, 1)

            weight = random.randrange(50, 200, 1)/100
            str = f"ema:\n\t t1:{t1}\n\t t2: {t2}\n\t t3: {t3}\n\t weight {weight}"

            return sma(t1, t2, t3, weight), str
        
        
        list_of_action = [make_bbands, make_rsi, make_ema, make_sma, make_ema_sma]
        action = lambda: random.choice(list_of_action)
        t = Tree(operator=rend_operator(), name=name)
        if is_rec:
            arr = [lambda data: talib.LINEARREG_SLOPE(data, random.randrange(3,21,1)),
                   lambda data: talib.HT_DCPERIOD(data, random.randrange(3,21,1)),
                   lambda data: talib.HT_TRENDLINE(data, random.randrange(3,21,1)),]
            
            n1 = Node(rend_operator(), parent=t, is_rec=is_rec, rec_func=random.choice(arr))
            n2 = Node(rend_operator(), parent=t, is_rec=is_rec, rec_func=random.choice(arr))

        else:
            n1 = Node(rend_operator(), parent=t)
            n2 = Node(rend_operator(), parent=t)


        function , str = action()()
        n1.left_child = Leaf(n1, function, str)

        function , str = action()()
        n1.right_child = Leaf(n1, function, str)
        t.right_child = n1

        function , str = action()()
        n2.left_child = Leaf(n2, function, str)

        function , str = action()()
        n2.right_child = Leaf(n2, function, str)
        t.left_child = n2

        return t
    
    def to_string(self):
        return f"tree {super().to_string()}" 

    def print(self):
        return f"name: {self.name}, eval {self.eval}"
    
    def set_stats(self, _stats):
        self.stats = _stats
        self.eval =  Evaluator.evaluate_strategy(self.stats)

    def crossover(self, tree_b):
        choice = random.choice(['RR', 'RL', 'LR', 'LL'])
        if choice == 'RR':
            node = self.right_child
            self.right_child = tree_b.right_child
            self.right_child.parent = self.right_child

            tree_b.right_child = node
            tree_b.right_child.parent = tree_b.right_child

        elif choice == 'RL':
            node = self.right_child
            self.right_child = tree_b.left_child
            self.right_child.parent = self.right_child

            tree_b.left_child = node
            tree_b.left_child.parent = tree_b.right_child

        elif choice == 'LR':
            node = self.left_child
            self.right_child = tree_b.right_child
            self.left_child.parent = self.left_child

            tree_b.right_child = node
            tree_b.right_child.parent = tree_b.right_child

        else:
            node = self.left_child
            self.left_child = tree_b.left_child
            self.left_child.parent = self.left_child

            tree_b.left_child = node
            tree_b.left_child.parent = tree_b.left_child
        #     pass
         
    def random_swap_trees(tree1, tree2):
        if not tree1 or not tree2:
            return None

        new_tree1 = Tree(tree1)
        new_tree2 = Tree(tree2)

        def recursive_swap(node1, node2):
            if not node1 or not node2:
                return

            if random.choice([True, False]):
                new_tree1.left = node1.left
                node1.parent =new_tree1
                new_tree1.right = node1.right
                
                new_tree2.left = node2.left
                new_tree2.right = node2.right

            else:
                new_tree1.left = node2.left
                new_tree1.right = node2.right

                new_tree2.left = node1.left
                new_tree2.right = node1.right

            recursive_swap(node1.left, node2.left)
            recursive_swap(node1.right, node2.right)

        recursive_swap(tree1, tree2)
        return new_tree1, new_tree2