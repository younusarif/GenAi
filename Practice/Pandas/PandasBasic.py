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


# Create a pandas DataFrame from a dictionary
data_dict = {   
    
    'Name': ['Alice', 'Bob', 'Charlie', 'David'], # Create a list of names
    'Age': [25, 30, 35, 40], # Create a list of ages
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston'] # Create a list of cities
}
df = pd.DataFrame(data_dict) # Create a pandas DataFrame from the dictionary
print("\nPandas DataFrame:") # Print a label for the output
print(df) # Print the pandas DataFrame  