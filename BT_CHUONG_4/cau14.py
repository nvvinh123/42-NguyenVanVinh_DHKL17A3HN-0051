import pandas as pd
import numpy as np

truth = pd.Series(range(10))
pred = pd.Series(range(10)) + np.random.random(10)
sai_so_tb = ((truth - pred) ** 2).mean()

print("Sai số bình phương trung bình của chuỗi truth và pred là:", sai_so_tb)