import pandas as pd

ser = pd.Series(list('abcderghijkimmopqrstt'))
pos = [0, 4, 8, 14, 20]
result = ser.iloc[pos]

print(result)