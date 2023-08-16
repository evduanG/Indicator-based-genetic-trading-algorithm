from enum import Enum
import numpy as np
import types

import random
class Operator(Enum):
    AND = 1
    OR = 2
    BIGGER = 3
    SMALLER = 4
    NOT_AND = 5
    NOT_OR = 6 
    XOR = 7 
    XNOR = 8
    ADD = 9
    SUB = 10

def rend_operator():
    return random.choice(list(Operator))

def and_operation(a, b, to_bool):
    is_err, res = error_prevention(a, b, 0)
    if is_err:
        return to_bool(res)
    return to_bool(a) and to_bool(b)   

def or_operation(a, b, to_bool):
    is_err, res = error_prevention(a, b, 0)
    if is_err:
        return to_bool(res)
    return to_bool(a) or to_bool(b)  

def bigger_operation(a, b, to_bool):
    return a if to_bool(a) > to_bool(b) else b  

def smaller_operation(a, b, to_bool):
    is_err, res = error_prevention(a, b, 0)
    if is_err:
        return res
    return a if to_bool(a) < to_bool(b) else b  

def not_and_operation(a, b, to_bool):
    return not and_operation(a, b, to_bool)

def not_or_operation(a, b, to_bool):
    return not or_operation(a, b, to_bool)

def xor_operation(a, b, to_bool):
    is_err, res = error_prevention(a, b, 0)
    if is_err:
        return to_bool(res)
    return to_bool(a) ^ to_bool(b)

def xnor_operation(a, b, to_bool):
    return not xor_operation(a, b, to_bool)

def add_operation(a, b, to_bool):
    is_err, res = error_prevention(a, b, 0)
    if is_err:
        return res
    return a + b

def sub_operation(a, b, to_bool):
    try:
        is_err, res = error_prevention(a, b, 0)
        if is_err:
            return res
        if bool(a) and  bool(b):
            return np.logical_xor(a, b)
        else:
            return a - b
    except:
        print (f"a: {a}, b: {b}")
        return 0

def error_prevention(a, b, defullt):
    if not a and not b:
        return False, defullt
    elif a:
        return True, a
    elif b:
        return True, b
    else:
        return True, defullt

operator_actions = {
    Operator.AND: and_operation,
    Operator.OR: or_operation,
    Operator.BIGGER: bigger_operation,
    Operator.SMALLER: smaller_operation,
    Operator.NOT_AND: not_and_operation,
    Operator.NOT_OR: not_or_operation,
    Operator.XOR: xor_operation,
    Operator.XNOR: xnor_operation,
    Operator.ADD: add_operation,
    Operator.SUB: sub_operation,
}

# # Usage
# selected_operator = Operator.ADD
# operator_actions[selected_operator](5, 3)  # Calls the corresponding function with parameters
