import pandas as pd
# set the maximum number of rows to display to 60
pd.set_option('display.max_rows', 5000)  

#importing data from a CSV file
data = pd.read_csv(r'E:\Clouds\Microsoft\Younus\OneDrive - MSFT\Portfolio\DataSets\Maven Toys Data\inventory.csv')
print(data.head())  # Display the first few rows of the DataFrame

#import data from an csv file using to_string method
print(data.to_string())  # Display all rows of the DataFrame as a string

# check system maximum rows display option
print(pd.options.display.max_rows)  # Display the current maximum number of rows to display 

#print information about the DataFrame
print(data.info())  # Display information about the DataFrame

# read particular rows using indexing
print(data.iloc[5])  # Display the  5 rows of the DataFrame

#loc vs iloc
#loc is label based indexing, iloc is integer based indexing
# read using loc and iloc
print(data.head(5))  # Display the first 5 rows of the DataFrame
print(data.loc[5])  # Display the row with index label 5 using loc
print(data.iloc[5])  # Display the row at integer index 5 using iloc

# 