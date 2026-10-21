# This is a simple example of using a lambda function in Python to multiply a number by 2.
# Assign the lambda function to a variable called 'multiple'.   
multiple = lambda x: x * 2 # This is a lambda function that multiplies the input 'x' by 2.
print(multiple(5))  # Output: 10


add = lambda x, y: x + y  # This is a lambda function that takes two arguments and returns their sum. 
print(add(3, 4))  # Output: 7


check = lambda i: i in "hello"  # This is a lambda function that checks if the input 'i' is in the string "hello".  
print(check("h"))  # Output: True
print(check("x"))  # Output: False


prices = [100, 200, 300, 400, 500]  # This is a list of prices.
# Use the map function with a lambda to apply a 10% discount to each price in the list.
discounted_prices = list(map(lambda price: price * 0.9, prices))  # This applies a 10% discount to each price.
print(discounted_prices)  # Output: [90.0, 180.0, 270.0, 360.0, 450.0]  

students = [['John', 85], ['Jane', 92], ['Dave', 78], ['Sara', 95]]  # This is a list of students with their scores.
# Use the filter function with a lambda to get students who scored above 90.
high_scorers = list(filter(lambda student: student[1] > 90, students))
print(high_scorers)  # Output: [['Jane', 92], ['Sara', 95]]   
