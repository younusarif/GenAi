# Keys are unique, if we try to add a duplicate key, it will overwrite the existing value

my_dict = {'a': 1, 'b': 2, 'c': 3, 'a': 4} # if duplicate key 'a' is added, it will overwrite the value 1 with 4
print("Original dictionary:", my_dict)

# indexing and accessing values
print("Value for key 'a':", my_dict['a']) # accessing value for key 'a'

# dictionary is not indexed, so we cannot access values using index like a list
# print(my_dict[0]) # this will raise a KeyError


# add a new key-value pair
my_dict['d'] = 5 # adding a new key-value pair
print("Dictionary after adding new key-value pair:", my_dict)   

# if key is not present, it will raise a KeyError
# print(my_dict['e']) # this will raise a KeyError

# to avoid KeyError, we can use the get() method which returns None if the key is not present
print("Value for key 'e':", my_dict.get('e')) # returns None since key 'e' is not present

# using in operator to check if a key is present in the dictionary
if 'b' in my_dict:
    print("Key 'b' is present in the dictionary with value:", my_dict['b']) 

# get all keys and values
print("All keys in the dictionary:", my_dict.keys()) # returns a view object of all keys
print("All values in the dictionary:", my_dict.values()) # returns a view object of all values