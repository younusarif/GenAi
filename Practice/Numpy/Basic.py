import numpy as np

# Create a 1D array
array_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:")
print(array_1d)

print("=========-=========")
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:")
print(array_2d)

print("=========-=========")
# Create a 3D array
array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("3D Array:")
print(array_3d) 

print("=========-=========")

# create an array of zeros
zeros_array = np.zeros((3, 4))  
print("Array of Zeros:")
print(zeros_array)
print("=========-=========")

# create an array using identity matrix
identity_matrix = np.identity(8)
print("Identity Matrix:")
print(identity_matrix)
print("=========-=========") 

# create an array using arange
arange_array = np.arange(4, 10, 2)
print("Array using arange:")
print(arange_array)
print("=========-=========")

# create an array using linspace
linspace_array = np.linspace(0, 1, 5)
print("Array using linspace:")
print(linspace_array)   
print("=========-=========")

# create an array using copy
copy_array = np.copy(zeros_array)
print("Array using copy:")
print(copy_array)
print("=========-=========")