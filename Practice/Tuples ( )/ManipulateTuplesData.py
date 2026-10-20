#create tuples
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple) 

# allow duplicates
my_tuple2 = (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
print(my_tuple2)    

# tuple is indexed
print('index 0:', my_tuple[0]) #1
print('index 2:', my_tuple[2]) #3   
print('index 4:', my_tuple[4]) #5   

# Slicing
print('Slicing:', my_tuple[1:4]) #(2, 3, 4) - returns a new tuple

# tuple is immutable means its elements cannot be changed after creation
# my_tuple[0] = 10 #TypeError: 'tuple' object does not support item assignment 
print('Immutable:',my_tuple) 

# sort tuple
my_tuple3 = (5, 2, 1, 4, 3)
print('Sorted:', sorted(my_tuple3)) # [1, 2, 3, 4, 5] - returns a list

