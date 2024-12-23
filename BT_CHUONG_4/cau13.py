import pandas as pd

ser1 = pd.Series([10, 9, 6, 5, 3, 1, 12, 8, 13])
ser2 = pd.Series([1, 3, 10, 13])

vi_tri = [ser1[ser1 == gia_tri].index[0] for gia_tri in ser2 if gia_tri in ser1.values]

print(vi_tri)