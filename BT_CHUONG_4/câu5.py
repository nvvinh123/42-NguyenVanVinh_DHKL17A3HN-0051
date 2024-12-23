import pandas as pd
import numpy as np
ser = pd.Series(np.random.normal(10, 5, 25))

print("Series:", ser)

min_value = ser.min()
print("Giá trị tối thiểu:", min_value)

percentile_25 = ser.quantile(0.25)
print("Phần centile thứ 25:", percentile_25)

median_value = ser.median()
print("Trung vị:", median_value)

percentile_75 = ser.quantile(0.75)
print("Phần centile thứ 75:", percentile_75)

max_value = ser.max()
print("Giá đa:", max_value)