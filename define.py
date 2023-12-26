
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
        self.elements = ['e', 'x', 'y', 'z']
        self.expression = ("[['e', 'x', 'y', 'z'], ['x', 'e', 'z', 'y'], ['y', 'z', 'e', 'x'], "
                           "['z', 'y', 'x', 'e']][['e', 'x', 'y', 'z'].index(a)][['e', 'x', 'y', 'z'].index(b)]")

    def function(self, a, b):
        return eval(self.expression, {'a': a, 'b': b})


class S:
    def __init__(self, n):
        self.elements = []
    # in progress
