# Perform Matrix multiplication of any 2 n*n matrices. 

import numpy as np

matrix_a = np.array([[1, 2], 
                     [3, 4]])
matrix_b = np.array([[5, 6], 
                     [7, 8]])

result = matrix_a @ matrix_b

print("Matrix A:\n", matrix_a)
print("Matrix B:\n", matrix_b)
print("Matrix Multiplication Result:\n", result)