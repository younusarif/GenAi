# Filter None and False values from the list
letter =['a',3, None, False,'','g','h','i','j']
print(list(filter(None, letter)))

# Use Bool to filter out False values
print(list(filter(bool, letter)))

# use isalpha to filter out non-alphabetic values
# all data must be strings to use isalpha
Letters =['sql','123', 'python', 'java', 'c++', 'ruby', 'javascript']
print(list(filter(str.isalpha, Letters)))
