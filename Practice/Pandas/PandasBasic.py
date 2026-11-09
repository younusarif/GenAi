import pandas as pd

# Create a pandas Series from a list
data = [10, 20, 30, 40, 50] # Create a list of data
series = pd.Series(data) # Create a pandas Series from the list
print("Pandas Series:") # Print a label for the output
print(series) # Print the pandas Series


# custom label the index of the Series
labeled_series = pd.Series(data, index=['a', 'b', 'c', 'd', 'e']) # Create a pandas Series with labeled index
print("\nLabeled Pandas Series:") # Print a label for the output        
print(labeled_series) # Print the labeled pandas Series


# Create a pandas DataFrame from a list
data_list = [
    [1, 'Alice', 25], 
    [2, 'Bob', 30], 
    [3, 'Charlie', 35], 
    [4, 'David', 40]] # Create a list of lists
df_from_list = pd.DataFrame(data_list, columns=['ID', 'Name', 'Age']) # Create a pandas DataFrame from the list of lists
print("\nPandas DataFrame from list:") # Print a label for the output
print(df_from_list) # Print the pandas DataFrame from the list of lists 

# Create a pandas DataFrame from a dictionary
data_dict = {   
    
    'Name': ['Alice', 'Bob', 'Charlie', 'David'], # Create a list of names
    'Age': [25, 30, 35, 40], # Create a list of ages
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston'] # Create a list of cities
}
df = pd.DataFrame(data_dict) # Create a pandas DataFrame from the dictionary
print("\nPandas DataFrame:") # Print a label for the output
print(df) # Print the pandas DataFrame  

#locate a specific row in the DataFrame using the index
row = df.loc[1] # Locate the row with index 1   
print("\nRow with index 1:") # Print a label for the output
print(row) # Print the row with index 1


# locte & convert a specific row in dictionary to dataframe
row_dict = df.loc[0] # Locate the row with index 2
row_df = pd.DataFrame([row_dict]) # Convert the dictionary to a pandas DataFrame
print("\nRow with index 0 as DataFrame:") # Print a label for the output
print(row_df) # Print the row with index 2 as a pandas DataFrame

# locate multiple rows in the DataFrame using a list of indices
rows = df.loc[[0, 2]] # Locate the rows with indices 0 and 2
print("\nRows with indices 0 and 2:") # Print a label for the output
print(rows) # Print the rows with indices 0 and 2
