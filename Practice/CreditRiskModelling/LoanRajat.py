import numpy as np
import pandas as pd

loan_data = pd.read_csv(r'E:\Clouds\Microsoft\Younus\OneDrive - MSFT\Portfolio\Financial Modelling\CreditRiskModeling\Data\loan_data.csv')
# print(loan_data.head(5))  # Display the first few rows of the DataFrame

# create a deep copy of the DataFrame
loan_data_copy = loan_data.copy(deep=True)
#print(loan_data_copy.head(5))  # Display the first few rows of the copied DataFrame

# using the display() function to show the entire DataFrame
display(loan_data)

# checking data types of each column in the DataFrame
print(loan_data.dtypes)  # Display the data types of each column in the Data

#
loan_data.info()  # Display information about the DataFrame, including data types and non-null counts   
