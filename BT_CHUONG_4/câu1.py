import pandas as pd
mylist = [1, 2, 3, 4, 5]
ser1 = pd.Series(mylist)
print(ser1)

myarr = pd.array([1, 2, 3, 4, 5])
ser2 = pd.Series(myarr)
print(ser2)

mydict = {'a': 1, 'b': 2, 'c': 3}
ser3 = pd.Series(mydict)
print(ser3)