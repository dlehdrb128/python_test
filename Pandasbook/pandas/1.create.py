from pandas import Series


# data = [10,20,30]
# s = Series(data)
# print(s)


# s = Series(['samsung', 81000])
# print(s)

data = [1000, 2000, 3000]
s = Series(data)
print(s.index)
print(s.index.to_list())