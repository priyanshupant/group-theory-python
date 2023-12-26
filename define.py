import numpy as np
from GROUP import evaluate_expression, GROUP


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


class Z:
    def __init__(self, n: int):
        self.elements = list(range(n))
        self.expression = f'(a+b)%{n}'


class U:
    def __init__(self, n: int):
        self.elements = [i for i in range(1, n) if gcd(i, n) == 1]
        self.expression = f'(a*b)%{n}'


class K4:
    def __init__(self):
        self.elements = ['e', 'x', 'y', 'z']
        self.expression = ("[['e', 'x', 'y', 'z'], ['x', 'e', 'z', 'y'], ['y', 'z', 'e', 'x'], "
                           "['z', 'y', 'x', 'e']][['e', 'x', 'y', 'z'].index(a)][['e', 'x', 'y', 'z'].index(b)]")


class S:
    def __init__(self, n):
        self.elements = []
    # in progress