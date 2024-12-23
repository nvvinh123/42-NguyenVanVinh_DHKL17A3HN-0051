import numpy as np
import pandas as pd

np.random.seed(100)
ser = pd.Series(np.random.randint(1, 5, [12]))


frequencies = ser.value_counts()

most_frequent = frequencies.nlargest(2).index

ser[~ser.isin(most_frequent)] = 'Other'