import numpy as np

# array shape   

array_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:")
print(array_1d)
print("Shape of 1D Array:", array_1d.shape)

print("=========-=========")

# create an array of zeros
zeros_array = np.zeros((3, 4))  
print("Array of Zeros:")
print(zeros_array)
print("Shape of Zeros Array:", zeros_array.shape)
print("=========-=========")

# using ndim to find the number of dimensions of an array
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("Number of dimensions of 2D Array:", array_2d.ndim)


# using ndmin to create an array with a minimum number of dimensions
ndmin_array = np.array([1, 2, 3], ndmin=5)
print("Array with minimum dimensions (ndmin=5):")   
print(ndmin_array)
print("Shape of ndmin Array:", ndmin_array.shape)    

# using size to find the total number of elements in an array
print("Total number of elements in 2D Array:", array_2d.size)  

# using itemsize to find the size of each element in bytes
print("Size of each element in 2D Array (in bytes):", array_2d.itemsize)    

# using dtype to find the data type of the elements in an array
print("Data type of elements in 2D Array:", array_2d.dtype)

# using astype to change the data type of an array
float_array = array_2d.astype(float)
print("2D Array with changed data type (float):")
print(float_array)
