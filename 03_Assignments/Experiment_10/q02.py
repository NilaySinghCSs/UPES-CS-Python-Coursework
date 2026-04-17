#  Create numpy array of (3,3) dimension. Now find sum of all rows & columns 
# individually. Also find 2nd maximum element in the array. 

import numpy as np

arr2 = np.array([[15, 25, 35], 
                 [45, 95, 65], 
                 [75, 85, 95]])

row_sums = np.sum(arr2, axis=1)
col_sums = np.sum(arr2, axis=0)

unique_sorted = np.unique(arr2)
second_max = unique_sorted[-2]

print("3x3 Array:\n", arr2)
print("Sum of rows:", row_sums)
print("Sum of columns:", col_sums)
print("2nd maximum element:", second_max)