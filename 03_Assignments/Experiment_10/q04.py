# Write a Pandas program to get the powers of an array values element-wise.  
# Note: First array elements raised to powers from second array 
 
# Sample data: {'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]} 
# Expected Output: 
# X Y Z 
# 0 78 84 86 
# 1 85 94 97 
# 2 96 89 96 
# 3 80 83 72 
# 4 86 86 83 

import pandas as pd
import numpy as np

array1 = np.array([2, 3, 4, 5])
array2 = np.array([1, 2, 3, 2])

df_power = pd.DataFrame({
    'Base': array1,
    'Power': array2,
    'Result': np.power(array1, array2)
})
print("Element-wise Powers:\n", df_power, "\n")

data = {'X': [78, 85, 96, 80, 86], 
        'Y': [84, 94, 89, 83, 86], 
        'Z': [86, 97, 96, 72, 83]}

df_sample = pd.DataFrame(data)
print("Expected Output DataFrame:\n", df_sample)