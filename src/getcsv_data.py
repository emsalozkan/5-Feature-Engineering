import os
import pandas as pd

def get_dataset(path):
    data = pd.read_csv(path)
    return data
