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
