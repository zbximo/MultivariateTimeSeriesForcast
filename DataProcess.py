import csv

import numpy as np
import pandas as pd

filename = "./data/AirQualityUCI.csv"
data = pd.read_csv(filename)
data2 = pd.read_excel("./data/AirQualityUCI.xlsx")
print(data2.shape)
# for i in range(data2.shape[0]):
#     for j in range(data2.shape[1]):
#         if data2.iloc[i, j] == -200:
#             if i == data2.shape[0]-1:
#                 data2.iloc[i, j] = data2.iloc[i - 1, j]
#             else: data2.iloc[i, j] = data2.iloc[i + 1, j]

print(data2.iloc[:,[13,14]])