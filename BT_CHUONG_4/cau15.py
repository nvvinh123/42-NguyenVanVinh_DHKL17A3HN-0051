import pandas as pd


ser = pd.Series(['how', 'to', 'kick', 'ass?'])
chuoi_hoa = ser.str.capitalize()

print(chuoi_hoa)