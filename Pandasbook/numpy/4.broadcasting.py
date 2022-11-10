import numpy as np


a = np.array( [ 1, 2, 3] )
b = np.array( [ 2, 3, 4] )


# print( a + b )
# print( a * b )
# print( a % b )


high = [92700, 92400, 92100, 94300, 92300]
low = [90000, 91100, 91700, 92100, 90900]

arr_high = np.array(high)
arr_low = np.array(low)

arr_diff = arr_high - arr_low
print(arr_diff)