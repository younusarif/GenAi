# Union, Intersection, and Difference Operations on Sets

a= {1, 2, 3, 4, 5}
b= {4, 5, 6, 7, 8}

# Union
union_set = a | b # use the '|' operator for union      
union_set1 = a.union(b) # use the union() method for union   
print("Union using | operator:", union_set)
print("Union using method:", union_set1)    


# Intersection
intersection_set = a & b # use the '&' operator for intersection
intersection_set1 = a.intersection(b) # use the intersection() method for intersection
print("Intersection using | operator :", intersection_set)      
print("Intersection using method:", intersection_set1)

# Difference
difference_set = a - b # use the '-' operator for difference
difference_set1 = a.difference(b) # use the difference() method for difference
print("Difference using | operator:", difference_set)
print("Difference using method:", difference_set1)

# Symmetric Difference
symmetric_difference_set = a ^ b # use the '^' operator for symmetric difference
symmetric_difference_set1 = a.symmetric_difference(b) # use the symmetric_difference() method for symmetric difference
print("Symmetric Difference using | operator:", symmetric_difference_set)
print("Symmetric Difference using method:", symmetric_difference_set1)


# Subset and Superset Operations on Sets
print("\nSubset and Superset Operations on Sets")
x = {1, 2, 3}   
y = {1, 2, 3, 4, 5}
print("Is x a subset of y?", x.issubset(y)) # use the issubset() method to check if x is a subset of y
print("Is y a superset of x?", y.issuperset(x)) # use the issuperset() method to check if y is a superset of x     

# Disjoint Sets
print("\nDisjoint Sets")
z = {6, 7, 8}
print("Is x disjoint from z?", x.isdisjoint(z)) # use the isdisjoint() method to check if x and z have no elements in common
print("Is y disjoint from z?", y.isdisjoint(z)) # use the isdisjoint() method to check if y and z have no elements in common
