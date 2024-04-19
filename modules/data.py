# data.py
import pandas as pd
from globals import filename

def load_data():
    data = pd.read_csv(f'../data/{filename}')
    return data
