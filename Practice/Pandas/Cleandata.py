import pandas as pd
# set the maximum number of rows to display to 60
pd.set_option('display.max_rows', None)

#importing data from a CSV file
originaldata = pd.read_csv(r'E:\Clouds\Microsoft\Younus\OneDrive - MSFT\Portfolio\DataSets\Maven Toys Data\inventory.csv')
# print(originaldata)  # Display the first few rows of the DataFrame

dirtydata = originaldata.copy()  # Create a copy of the original DataFrame to work with
# print(dirtydata)  # Display the dirty data

#isnull() method is used to detect missing values in a DataFrame. It returns a DataFrame of the same shape as the original, with True for entries that are NaN (missing) and False for entries that are not NaN.
# print(dirtydata.isnull())  # Display a DataFrame indicating missing values  
print(dirtydata.isnull().sum())  # Display the count of missing values for each column  

df = dirtydata.dropna()  # Drop rows with missing values
# print(df)  # Display the cleaned DataFrame after dropping rows with missing values
print(df.isnull().sum())  # Display the count of missing values for each column after dropping rows with missing values 
