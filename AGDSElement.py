from sortedcontainers import SortedList
import numpy as np


class AGDSElement:
    def __init__(self):
        self.element = dict()
        self.min_value = None
        self.max_value = None
        self.values = SortedList()

    def add(self, position, value):
        if value not in self.element:
            self.values.add(value)

        self.element.setdefault(value, []).append(position)
        self.min_value = value if self.min_value is None \
            else min(self.min_value, value)
        self.max_value = value if self.max_value is None \
            else max(self.max_value, value)

    def get_indices_ordered_by_value_distance(self, value):
        diff_values = abs(self.values - value)
        return np.argsort(diff_values)

    def get_relevant_objects(self, index_in_list):
        return self.element[self.values[index_in_list]]

    def get_diff(self, index1, index2):
        return abs(self.values[index1] - self.values[index2])

    def get_neighbour_weights(self, value1, value2):
        return 1 - (abs(value1 - value2) / abs(self.max_value - self.min_value))

    def get_interaction_weights(self, value1):
        if type(value1) == int:
            return 1

        return 1/len(self.element[value1])
