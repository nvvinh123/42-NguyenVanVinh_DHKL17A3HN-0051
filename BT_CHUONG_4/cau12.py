import pandas as pd

ser1 = pd.Series(range(5))

ser2 = pd.Series(list('abcde'))

df1 = pd.concat([ser1, ser2], ignore_index=True)

print(df1)


df2 = pd.concat([ser1, ser2], axis=1)

print(df2)