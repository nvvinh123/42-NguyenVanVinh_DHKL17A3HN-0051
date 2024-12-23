import pandas as pd
import numpy as np
ser1 = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26))
df = pd.concat([ser1, ser2], axis=1)