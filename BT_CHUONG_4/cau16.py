import pandas as pd

ser = pd.Series([1, 3, 6, 10, 15, 21, 27, 35])

hieu_so_dau = ser[1:].values - ser[:-1].values

hieu_so_cua_hieu_so = hieu_so_dau[1:] - hieu_so_dau[:-1]

print("Hiệu số của hiệu số:", hieu_so_cua_hieu_so)