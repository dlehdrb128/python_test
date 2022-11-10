import numpy as np
import pandas as pd
from db import config
import matplotlib.pyplot as plt


db_class = config.Database()
sql      = "SELECT * FROM kospi_005930_d WHERE day BETWEEN '2000-10-01' AND '2000-10-05'"
row      = db_class.executeAll(sql)


print(row,"test")

# print(row)

test = [{'no': 4528, 'open': 192000, 'high': 194000, 'low': 188000, 'close': 190500, 'volume': 822417, 'day': '2222'}]
test2 = [{"name":'이상호', 'age':20} ,  {"name":'공욱재', 'age':19},  {"name":'공욱재'} ]




df = pd.DataFrame(row)

# for col in df:
#     print(f"딕셔너리 키값 :{col}, 딕셔너리 값: { df[col].dtype} ")

open = df['open'].mean()

cond = df['open'] >= 200000
df = df['open'].mean()
# print(df)






# test = df['volume'].astype('int').mean()

# print(test.mean())

# print(df['volume'].mean())


          








