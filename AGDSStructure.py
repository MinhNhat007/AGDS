from AGDSElement import *
import numpy as np


class AGDSStructure:
    def __init__(self, data_frame, label):
        self.data_frame = data_frame
        self.label = label
        n_column = len(data_frame.columns)

        self.values = np.ndarray((n_column,), dtype=np.object)
        for i in range(n_column):
            self.values[i] = AGDSElement()

        for i in range(len(data_frame)):
            self.add(i, n_column, data_frame.iloc[[i]])

    def add(self, n_row, n_column, row):
        for i in range(n_column):
            self.values[i].add(n_row, row[i][n_row])

    def get_indices_ordered_by_distance(self, n_attribute, value):
        return self.values[n_attribute].get_indices_ordered_by_value_distance(value)

    def get_distance(self, n_attribute, index1, index2):
        return self.values[n_attribute].get_diff(index1, index2)

    def get_original_data(self, n_row, n_column):
        return self.data_frame[n_column][n_row]

    def get_relevant_objects(self, n_attribute, index_in_list):
        return self.values[n_attribute].get_relevant_objects(index_in_list)
