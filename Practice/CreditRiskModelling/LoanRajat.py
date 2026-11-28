import numpy as np
import pandas as pd

# set the maximum number of rows to display to 60
pd.set_option('display.max_rows', None)

loan_data = pd.read_csv(r'E:\Clouds\Microsoft\Younus\OneDrive - MSFT\Portfolio\Financial Modelling\CreditRiskModeling\Data\loan_data.csv')
# print(loan_data.head(5))  # Display the first few rows of the DataFrame

# create a deep copy of the DataFrame
loan_data_copy = loan_data.copy(deep=True)
#print(loan_data_copy.head(5))  # Display the first few rows of the copied DataFrame

# using the display() function to show the entire DataFrame
# display(loan_data)

# checking data types of each column in the DataFrame
# print(loan_data.dtypes)  # Display the data types of each column in the Data

# Display information about the DataFrame, including data types and non-null counts   
loan_data.info()  

# unique() method is used to find the unique values in a column of a DataFrame.
print(loan_data['emp_length'].unique())  # Replace 'column_name' with the actual column name

#str.replace() method is used to replace a specified substring with another substring in a string column of a DataFrame.
loan_data['emp_length_cleared'] = loan_data['emp_length'].str.replace('years', '')
loan_data['emp_length_cleared'] = loan_data['emp_length_cleared'].str.replace('year', '') 
loan_data['emp_length_cleared'] = loan_data['emp_length_cleared'].str.replace('+', '')
loan_data['emp_length_cleared'] = loan_data['emp_length_cleared'].str.replace('< 1', '0')
display(loan_data[['emp_length', 'emp_length_cleared']])  # Display the original and modified columns  

# Get particlar columns from the DataFrame using indexing
loan_data[['emp_length']]
