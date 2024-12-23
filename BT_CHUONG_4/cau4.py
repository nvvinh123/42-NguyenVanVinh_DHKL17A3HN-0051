import pandas as pd
import numpy as np
ser1 = pd.Series([1, 2, 3, 4, 5,])
ser2 = pd.Series([ 6, 7, 8, 9, 10])
series_u = pd.Series(np.union1d(ser1, ser2))
series_i = pd.Series(np.intersect1d(ser1, ser2))
ser_u_not_i = series_u[~series_u.isin(series_i)]