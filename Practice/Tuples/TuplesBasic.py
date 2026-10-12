#tuples
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple) #ordered

# allow duplicates
my_tuple2 = (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
print(my_tuple2)    

# tuple is indexed
print(my_tuple[0]) #1
print(my_tuple[2]) #3   
print(my_tuple[4]) #5   

# tuple is immutable
# my_tuple[0] = 10 #TypeError: 'tuple' object does not support item assignment 
print(my_tuple) 

# sort tuple
my_tuple3 = (5, 2, 1, 4, 3)
print(sorted(my_tuple3)) # [1, 2, 3, 4, 5] - returns a list

