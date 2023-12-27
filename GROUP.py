import numpy as np


def a_pows(a, function, n):
    a_pows_set = {a}
    a_pows_list = [a]

    for i in range(n):
        temp = function(a, a_pows_list[-1])
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
    def __init__(self, elements: list, func):
        self.elements = list(elements)
        self.function = func
        self.order = len(self.elements)
        self.cayley_table = self.get_cayley_table()
        self.identity = None
        self.identity_exist = self.is_identity()
        self.generators = set()
        self.inverses = set()
        self.self_invertible_elements = set()
        self.not_self_invertible = self.get_not_self_invertible()
        self.centre = self.get_centre()

    def info(self):
        info_dict = {
            "Is Group": self.is_group(),
            "Elements": set(self.elements),
            "Order": self.order,
            "Cayley Table": self.cayley_table,
            "Identity Exist": self.identity_exist,
            "Identity": self.identity,
            "Inverses exist": self.is_inverse(),
            "Inverses": self.inverses,
            "Self Invertible Elements": self.self_invertible_elements,
            "Not Self Invertible Elements": self.get_not_self_invertible(),
            "Is Abelian": self.is_abelian(),
            "Is Cyclic": self.is_cyclic(),
            "Subgroups": self.get_subgroups(),
            "Centre": self.centre,
            "Generators": self.generators,
            "Normal Subgroups": self.get_normal_subgroups(),
            "Is Simple": self.is_simple()
        }

        return info_dict

    def get_cayley_table(self):
        if type(self.elements[0]) is str:
            matrix = np.zeros((self.order, self.order), dtype='2<U')
        else:
            matrix = np.zeros((self.order, self.order))
        row = 0
        for element1 in self.elements:
            col = 0
            for element2 in self.elements:
                matrix[row, col] = self.function(element1, element2)
                col += 1
            row += 1
        return matrix

    def is_closed(self):
        if set(list(np.unique(self.cayley_table))) == set(list(self.elements)):
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
                    pair = (self.elements[j], self.elements[i])
                    if pair not in list(self.inverses) and pair[::-1] not in list(self.inverses):
                        self.inverses.add(pair)
                        if i == j:
                            self.self_invertible_elements.add(self.elements[i])

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

    def a_power_n(self, a, n: int):
        if n == 0:
            return self.identity
        elif n > 0:
            return a_pows(a, self.function, self.order)[1][(n - 1) % self.order]
        else:
            return a_pows(a, self.function, self.order)[1][self.order - abs(n) % self.order - 1]

    def is_abelian(self):
        if np.array_equal(self.cayley_table, np.transpose(self.cayley_table)):
            return True
        return False

    def is_cyclic(self):
        for element in self.elements:
            if set(self.elements) == a_pows(element, self.function, self.order)[0]:
                self.generators.add(element)
        if len(self.generators) > 0:
            return True

        return False

    def get_not_self_invertible(self):
        return set([x for x in self.elements if x not in self.self_invertible_elements])

    def get_subgroups(self):
        subgroups = []
        subsets = [subset for subset in powerset(self.elements) if subset]
        for subset in subsets:
            subgroup = GROUP(subset, self.function)
            subgroup.cayley_table = subgroup.get_cayley_table()

            if subgroup.is_group():
                subgroups.append(set(subgroup.elements))

        return subgroups

    def is_normal(self, subgroup):
        i = 0
        for h in subgroup:
            for x in self.elements:
                if self.function(x, self.function(h, self.a_power_n(x, -1))) in subgroup:
                    i += 1

        if i == len(subgroup) * self.order:
            return True
        return False

    def get_normal_subgroups(self):
        normal_subgroup = []
        subgroups = self.get_subgroups()
        for subgroup in subgroups:

            if self.is_normal(list(subgroup)):
                normal_subgroup.append(subgroup)
        return normal_subgroup

    def is_simple(self):
        if len(self.get_normal_subgroups()) == 2:
            return True
        return False

    def get_centre(self):
        centre = set()
        for i in range(self.order):
            if np.array_equal(self.cayley_table[i, :], self.cayley_table[:, i]):
                centre.add(self.elements[i])
        return centre
