import numpy as np


def evaluate_expression(a, b, expression):
    try:
        result = eval(expression, {'a': a, 'b': b})
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except Exception as e:
        return f"Error: {str(e)}"


def a_pows(a, expression, n):
    a_pows_set = {a}
    a_pows_list = [a]

    for i in range(n):
        temp = evaluate_expression(a, a_pows_list[-1], expression)
        a_pows_list.append(temp)
        a_pows_set.add(temp)

    return a_pows_set, a_pows_list


def powerset(input_list):
    powerset_list = []
    n = len(input_list)

    for i in range(2 ** n):
        subset = [input_list[j] for j in range(n) if (i >> j) & 1]
        powerset_list.append(subset)

    return powerset_list


class GROUP:
    def __init__(self, elements: list, expression: str):
        self.elements = elements
        self.expression = expression
        self.order = len(self.elements)
        self.cayley_table = self.get_cayley_table()
        self.identity = None
        self.identity_exist = self.is_identity()
        self.generators = []
        self.inverses = []
        self.self_invertible_elements = []
        self.not_self_invertible = self.get_not_self_invertible()
        self.centre = self.get_centre()

    def info(self):
        print("Is Group: ", self.is_group())
        print('Elements: ', self.elements)
        print('Order: ', self.order)
        print('Cayley Table: \n', self.cayley_table)
        print('Identity Exist: ', self.identity_exist)
        print('Identity: ', self.identity)
        print('Inverses exist: ', self.is_inverse())
        print('Inverses: ', self.inverses)
        print('Self Invertible Elements: ', self.self_invertible_elements)
        print('Not Self Invertible Elements: ', self.get_not_self_invertible())
        print('Is Abelian: ', self.is_abelian())
        print('Is Cyclic: ', self.is_cyclic())
        print('Subgroups: ', self.get_subgroups())
        print('Centre: ', self.centre)
        print('Generators: ', self.generators)
        print('Normal Subgroups: ', self.get_normal_subgroups())

    def get_cayley_table(self):
        matrix = np.zeros((self.order, self.order))
        row = 0
        for element1 in self.elements:
            col = 0
            for element2 in self.elements:
                matrix[row, col] = eval(self.expression, {'a': element1, 'b': element2})
                col += 1
            row += 1
        return matrix

    def is_closed(self):
        if np.array_equal(np.unique(self.cayley_table), np.array(self.elements)):
            return True
        return False

    def is_identity(self):

        for i in range(self.order):
            if (np.array_equal(self.cayley_table[i][:], self.cayley_table[:][i]) and
                    np.array_equal(self.cayley_table[i][:], self.elements)):
                self.identity = self.elements[i]
        if self.identity is not None:
            return True
        else:
            return False

    def is_inverse(self):
        for i in range(self.order):
            for j in range(self.order):
                if self.cayley_table[i, j] == self.cayley_table[j, i] == self.identity:
                    pair = [self.elements[j], self.elements[i]]
                    if pair not in self.inverses and pair[::-1] not in self.inverses:
                        self.inverses.append(pair)
                        if i == j:
                            self.self_invertible_elements.append(self.elements[i])

        length = 0
        if len(self.get_not_self_invertible()) != 0:
            length = len(self.get_not_self_invertible()) / 2

        if len(self.inverses) == len(self.self_invertible_elements) + length:
            return True
        else:
            return False

    def is_group(self):
        if self.is_inverse() and self.is_closed() and self.is_identity():
            return True
        else:
            return False

    def evaluate(self, a, b):
        try:
            result = eval(self.expression, {'a': a, 'b': b})
            return result
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."
        except Exception as e:
            return f"Error: {str(e)}"

    def a_power_n(self, a, n: int):
        if n == 0:
            return self.identity
        elif n > 0:
            return a_pows(a, self.expression, self.order)[1][(n - 1) % self.order]
        else:
            return a_pows(a, self.expression, self.order)[1][self.order - abs(n) % self.order - 1]

    def is_abelian(self):
        if np.array_equal(self.cayley_table, np.transpose(self.cayley_table)):
            return True
        return False

    def is_cyclic(self):
        for element in self.elements:
            if set(self.elements) == a_pows(element, self.expression, self.order)[0]:
                self.generators.append(element)
        if len(self.generators) > 0:
            return True

        return False

    def get_not_self_invertible(self):
        return [x for x in self.elements if x not in self.self_invertible_elements]

    def get_subgroups(self):
        subgroups = []
        trivial = [[self.identity], self.elements]
        subsets = powerset(self.elements)
        subgroups += trivial
        for subset in subsets:
            if subset not in trivial:
                subgroup = GROUP(subset, self.expression)
                subgroup.cayley_table = subgroup.get_cayley_table()

                if subgroup.is_group():
                    subgroups.append(subgroup.elements)

        return subgroups

    def is_normal(self, subgroup):
        i = 0
        for h in subgroup:
            for x in self.elements:
                if self.evaluate(x, self.evaluate(h, self.a_power_n(x, -1))) in subgroup:
                    i += 1

        if i == len(subgroup)*self.order:
            return True
        return False

    def get_normal_subgroups(self):
        normal_subgroup = []
        subgroups = self.get_subgroups()
        for subgroup in subgroups:
            # print(subgroup)
            # print(self.is_normal(subgroup))
            if self.is_normal(subgroup):
                normal_subgroup.append(subgroup)
        return normal_subgroup

    def get_centre(self):
        centre = []
        for i in range(self.order):
            if np.array_equal(self.cayley_table[i, :], self.cayley_table[:, i]):
                centre.append(self.elements[i])
        return centre
