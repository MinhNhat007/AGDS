from RankTable import *
import math


class AGDSKNearest:
    def __init__(self, agds_structure, k=3):
        self.agds_structure = agds_structure
        self.k = k

    def find_similarity(self, data_input):
        rank_table = RankTable(self.k)

        indices_ordered_by_distance = self.agds_structure\
            .get_indices_ordered_by_distance(0, data_input[0])

        for index in indices_ordered_by_distance:
            relevant_objects = self.agds_structure\
                .get_relevant_objects(0, index)
            for relevant_object in relevant_objects:
                rank_table.add(
                    self.get_error(data_input, relevant_object), relevant_object)

            if self.agds_structure\
                    .get_distance(0, index, indices_ordered_by_distance[0]) > \
                    rank_table.get_max_value():
                break

        return self.get_votes(rank_table)

    def get_votes(self, rank_table):
        label = [self.agds_structure.label[x] for x in rank_table.get_all_objects()]
        return max(set(label), key=label.count)

    def get_error(self, data_input, object_index):
        error = 0.0
        for i in range(len(data_input)):
            error += (data_input[i] -
                      self.agds_structure.get_original_data(object_index, i)) ** 2

        return math.sqrt(error)
