import pandas as pd
# set the maximum number of rows to display to 60
pd.set_option('display.max_rows', 5000)  

#importing data from a CSV file
data = pd.read_csv(r'E:\Clouds\Microsoft\Younus\OneDrive - MSFT\Portfolio\DataSets\Maven Toys Data\inventory.csv')
print(data.head())  # Display the first few rows of the DataFrame

#import data from an csv file using to_string method
# print(data.to_string())  # Display all rows of the DataFrame as a string

# check system maximum rows display option
print(pd.options.display.max_rows)  # Display the current maximum number of rows to display 