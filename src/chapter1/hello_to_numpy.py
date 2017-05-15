import numpy as np

array1 = np.array([0, 2])
array2 = np.array([3, 4])
print(array1 + array2)
print(array1 - array2)
print(array1 * array2)
print(array1 / array2)

print(array1 / 2)

mat1 = np.array([[1, 2], [3, 4], [5, 6]])
mat2 = np.array([10, 20])
mat3 = mat1 + mat2
print(mat3)

print(mat3[0][1])
print(mat3[(0, 1)])
print(mat3[array1])

array3 = mat3.flatten()
print(array3)
print(array3 > 20)
print(array3[array3 > 20])
