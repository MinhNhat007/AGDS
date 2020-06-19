from DataReader import *
from AGDSStructure import *
from AGDSKNearest import *
import numpy as np


def classify(data_holder, model, X):
    predicted_label = model.find_similarity(np.array(X))
    win_class = data_holder.get_real_label(predicted_label)
    print(win_class)


if __name__ == '__main__':
    data_reader = DataReader("IrisData.xls")
    agds_structure = AGDSStructure(data_reader.data_frame, data_reader.label)
    k_nearest = AGDSKNearest(agds_structure, 3)

    classify(data_reader, k_nearest, [4.5, 3.0, 1.1, 0.1])
    classify(data_reader, k_nearest, [7.0, 3.2, 4.7, 1.4])
    classify(data_reader, k_nearest, [5.0, 2.0, 4.0, 1.0])
    classify(data_reader, k_nearest, [5.7, 2.5, 4.8, 1.6])
