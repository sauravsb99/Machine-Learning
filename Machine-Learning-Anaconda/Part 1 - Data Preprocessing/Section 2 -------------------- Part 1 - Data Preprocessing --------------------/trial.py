import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Data.csv')
print("HI")

X = dataset.iloc[:, :-1].values

# print(X)

Y = dataset.iloc[:, 3].values

# print(Y)