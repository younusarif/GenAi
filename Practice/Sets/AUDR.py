# Use .add(), .update(), .remove() methods to add and remove elements from a set    


my_set = {1, 2, 3, 4, 5}
print(my_set)   

# Duplicate values will be removed
my_set = {1, 2, 3, 4, 5, 1, 2, 3}
print(my_set)   

#indexing is not allowed
# print(my_set[0]) #TypeError: 'set' object is not subscriptable    

# sets are mutable, we can add new elements to a set,
my_set.add(6) # single value can be added using add() method
print(my_set)   

# to add multiple values to a set
my_set.update({7, 8, 9}) # multiple values can be added using   update() method
print(my_set)


# use remove() method to remove an element from a set
my_set.remove(9) # if the element is not present in the set, it will raise a KeyError
print(my_set)


#sort set
my_set2 = {5, 2, 1, 4, 3}
print(sorted(my_set2)) # [1, 2, 3, 4, 5] - returns a list

