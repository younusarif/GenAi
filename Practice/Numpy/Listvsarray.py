import numpy as np

# list vs array
list_1d = [1, 2, 3, 4, 5]
array_1d = np.array([1, 2, 3, 4, 5])

print("List:")
print(list_1d)
print("Array:")
print(array_1d)

import sys
# get size of list and array
print("\nSize of list:", len(list_1d))
print("Size of array:", array_1d.size)  
print("Memory usage of list:", sys.getsizeof(list_1d))
print("Memory usage of array:", array_1d.nbytes)    

import time 

# get execution time of list and array operations
start_time = time.time()
for i in range(1000000):
    list_1d[i % 5] += 1
end_time = time.time()
print("\nExecution time of list:", end_time - start_time)

start_time = time.time()
for i in range(1000000):
    array_1d[i % 5] += 1
end_time = time.time()
print("Execution time of array:", end_time - start_time)
