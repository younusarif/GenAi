# Start from 0
letter =['a','b','c','d','e','f','g','h','i','j']
print(list(enumerate(letter)))
    

# Start from 3
print(list(enumerate(letter, start=3)))



# Start from 5
for index, l in enumerate(letter, start=5):
    print(index, l)
