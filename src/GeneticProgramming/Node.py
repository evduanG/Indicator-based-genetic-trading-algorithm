import random
from .INode import INode
from .Operator import Operator, operator_actions

class Node(INode):
    def __init__(self, operator:Operator, right_child=None, left_child=None, parent=None, border=0.5, is_rec= False, rec_func= None):
        self.right_child = right_child
        self.left_child = left_child
        self.operator = operator
        self.border = border
        self.parent = parent
        self.is_rec = is_rec 
        self.rec_func = rec_func if is_rec else  lambda data: data
        
    def to_bool(self, var):
        return var > self.border
    
    def mutation(self):
        mutation_type = random.choice(['right_child', 'left_child', 'border', 'operator'])
        if mutation_type == 'right_child':
            if self.right_child:
                self.right_child.mutation()
        elif mutation_type == 'left_child':
            if self.left_child:
                self.left_child.mutation()
        elif mutation_type == 'border':
            self.border = random.random()
        else:
            self.operator = random.choice(list(Operator))

    def get_crossover(self):
        if not (self.right_child and self.left_child):
            return self, self.parent
        elif self.right_child and self.left_child:
            choice = random.choice(['right_child', 'left_child', 'self'])
            if choice == 'right_child':
                return self.right_child.get_crossover()
            elif choice == 'left_child':
                return self.left_child.get_crossover()
            else:
                return self
        elif self.right_child:
            choice = random.choice(['right_child', 'self'])
            if choice == 'right_child':
                return self.right_child.get_crossover()
            else:
                return self, self.parent
        else:
            choice = random.choice(['left_child', 'self'])
            if choice == 'left_child':
                return self.left_child.get_crossover()
            else:
                return self.parent

    def crossover(self, tree_b):
        node_from_a, parent_a = self.get_crossover()
        node_from_b, parent_b = tree_b.get_crossover()
        print(f'node_from_a: {node_from_a} parent_a: {parent_a}')
        print(f'node_from_b: {node_from_b} parent_b: {parent_b}')
   
    
    def calc(self, data, is_to_str= False):
        right_child_calc = self.right_child.calc(self.rec_func(data), is_to_str) if self.right_child else None
        left_child_calc = self.left_child.calc(self.rec_func(data), is_to_str) if self.left_child else None
        
        if is_to_str: 
            return f"({right_child_calc}) {str(self.operator)} ({left_child_calc})"
        return operator_actions[self.operator](right_child_calc, left_child_calc, self.to_bool)
    
    def to_string(self):
        right_child = self.right_child.to_string() if  self.right_child else "None" 
        left_child = self.left_child.to_string() if  self.left_child else "None" 
        parent = "parent" if  self.parent else "None" 

        return f"operator: {str(self.operator)}, is_rec: {self.is_rec}, parent: {parent}\n\tright_child:\n{right_child}\n\tleft_child:\n{left_child}"
