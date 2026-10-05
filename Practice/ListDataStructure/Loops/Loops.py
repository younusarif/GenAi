# Loops & Types

# For Loop
items = (1,10) # using tuple in loops
for item in items:
    print(f"Items#: {item}")

items = [1,10] # using list in loops
for item in items:
    print(f"Items#: {item}")

for name in 'family':# using string in loops
    print(f"Letter# {name.capitalize()}")

#  Loop using Range
for name in range(5):# using range instead type number in loops
    print(f"Number# {name}")

for name in range(15,20):# give start and end range instead type number in loops
    print(f"Number# {name}")

for name in range(16,30,2):# give start and end range with step up value instead type number in loops
    print(f"Number# {name}")

# Break Loop using Break 
fname = ['Ali','Fatima','','Hasan','Hussain']
for name in fname: # assign a name to variable  is name
    if name == '':
        print ('Empty Value Detected')
        break
    print(f'Firstname = {name}') # use f{} string to convert data into strings

# Continue Loop using Continue
fname = ['Ali','Fatima','Hasan','Hussain']
for name in fname: # assign a name to variable  is name
    if name == 'Fatima':
        print ('Skip the Value')
        continue
    print(f'Firstname = {name}') # use f{} string to convert data into strings
    
# Skips weekends in Calendar Loop using continue
days =['Mon','Sun','Wed','Thurs']
for day in days:
    if day in ['Sat','Sun']:
        continue
    print(f'Workdays: {day}')

# Skips weekends in Calendar Loop using continue
days =['Mon','Sun','Wed','Thurs']
weekends =['Sat','Sun']
for day in days:
    if day in weekends: # Avoid using hardcding value inside for or if, instead define in var
        continue
    print(f'Workdays: {day}')

# Else with For Loop 
elsenum = [1,2,3]
for num in elsenum:
    print (num)
else:
    print('Loops is completed')

# Else with For Loop 
elsenum = [1,2,3,4]
for num in elsenum:
    if num ==3:
        print(num)
        break
else:
    print('Loops is completed')

# Else with For Loop 
elsenum = [1,2,3]
for num in elsenum:
    print(num)
    if num ==2:
        break
else:
    print('Loops is completed')

# Nested Loop
for x in range(2):
    for y in range(1):
        for z in range (1):
            print (f"({x},{y},{z})")

# Use case of Nested Loop
colors = ['red','blue','green']
sizes =['L','M','S']
for color in colors:
    for size in sizes:
        print(f'{color} - SizeNumber {size}')

