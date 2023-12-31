import numpy as np
from permutation import Permutation 

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


class Z:
    def __init__(self, n: int):
        self.elements = set(range(n))
        self.n = n

    def function(self, a, b):
        return (a + b) % self.n


class U:
    def __init__(self, m: int):
        self.elements = [i for i in range(1, m) if gcd(i, m) == 1]
        self.m = m

    def function(self, a, b):
        return (a * b) % self.m


class K4:
    def __init__(self):
        self.elements = {'e', 'x', 'y', 'z'}
        self.expression = ("[['e', 'x', 'y', 'z'], ['x', 'e', 'z', 'y'], ['y', 'z', 'e', 'x'], "
                           "['z', 'y', 'x', 'e']][['e', 'x', 'y', 'z'].index(a)][['e', 'x', 'y', 'z'].index(b)]")

    def function(self, a, b):
        return eval(self.expression, {'a': a, 'b': b})


class Q8:
    def __init__(self):
        self.elements = ['1', '-1', 'i', '-i', 'j', '-j', 'k', '-k']
        self.cayley = np.array(
            [['1', '-1', 'i', '-i', 'j', '-j', 'k', '-k'], ['-1', '1', '-i', 'i', '-j', 'j', '-k', 'k'],
             ['i', '-i', '-1', '1', 'k', '-k', '-j', 'j'], ['-i', 'i', '1', '-1', '-k', 'k', 'j', '-j'],
             ['j', '-j', '-k', 'k', '-1', '1', 'i', '-i'], ['-j', 'j', 'k', '-k', '1', '-1', '-i', 'i'],
             ['k', '-k', 'j', '-j', '-i', 'i', '-1', '1'], ['-k', 'k', '-j', 'j', 'i', '-i', '1', '-1']], dtype='2<U')

    def function(self, a, b):
        r_index = self.elements.index(a)
        c_index = self.elements.index(b)
        return self.cayley[r_index][c_index]


class S:
    def __init__(self, n):
        self.elements = self.get_set(n)

    def get_set(self, n):
        elements = []
        for p in Permutation.group(n):
            elements.append(p)       
        return elements
    
    def function(self, a, b):
        return a*b

class A:
    def __init__(self, n):
        self.elements = self.get_set(n)

    def get_set(self, n):
        elements = []
        for p in Permutation.group(n):
            if p.is_even:
                elements.append(p)       
        return elements
    
    def function(self, a, b):
        return a*b
