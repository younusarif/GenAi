import numpy as np
import pandas as pd

# set the maximum number of rows to display to 60
pd.set_option('display.max_rows', None)

loan_data = pd.read_csv(r'E:\Clouds\Microsoft\Younus\OneDrive - MSFT\Portfolio\Financial Modelling\CreditRiskModeling\Data\loan_data.csv')

#information about the DataFrame, including data types and non-null counts
# loan_data.info()

# Display particular columns from the DataFrame using indexing
# Credit_line= loan_data['earliest_cr_line']
# print(Credit_line)

# using iloc to select the 'earliest_cr_line' column by its index position
earliest_credit_line = loan_data.iloc[:, 26]  # Assuming 'earliest_cr   line' is the 26th column (index 26)       
print(earliest_credit_line)
