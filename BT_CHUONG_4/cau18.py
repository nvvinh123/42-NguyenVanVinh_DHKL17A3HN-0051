import pandas as pd
import re

emails = pd.Series(['buying books at amazom.com', 'rameses@egypt.com', 'matt@t.co', 'narendra@modi.com'])

pattern ='[A-Za-z0-9.%+-]+@[A-Za-z0-9.-]+.[A-Za-z]{2,4}'

matches = emails.str.extract(pattern)

print(matches)