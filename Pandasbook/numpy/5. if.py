import numpy as np


arr = np.array([10, 20, 30])

arr = np.where( arr > 10, arr + 10, arr - 10)

lge = np.array([93000, 82400, 99100, 81000, 72300])

result = lge[lge <= 85000]
print(len(result))



# print(arr[true])

# print(arr)