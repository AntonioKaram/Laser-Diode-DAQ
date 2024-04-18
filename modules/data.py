# data.py
import pandas as pd

def load_data():
    data = pd.read_csv('data/data.csv')
    return data
