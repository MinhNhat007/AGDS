import pandas as pd
from pathlib import Path
import numpy as np


class DataReader:
    def __init__(self, file_name):
        self.data_frame = pd.read_excel(Path(file_name), header=None, index_col=None)
        label = self.data_frame[len(self.data_frame.columns) - 1]

        unique_label = label.unique()
        identity = np.linspace(0, len(unique_label) - 1, len(unique_label)).astype(int)

        self.label_identity_dictionary = dict(zip(unique_label, identity))
        self.identity_label_dictionary = dict(zip(identity, unique_label))
        self.label = label.replace(unique_label, identity)
        self.data_frame[len(self.data_frame.columns) - 1] = self.label

    def get_real_label(self, identity):
        return self.identity_label_dictionary[identity]
