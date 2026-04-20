#  Write a Pandas program to find and replace the missing values in a given DataFrame 
# which do not have any valuable information. 

import pandas as pd
import numpy as np

df_missing = pd.DataFrame({
    'ID': [101, 102, np.nan, 104],
    'Score': [85, np.nan, 90, 78],
    'Remarks': ['Good', 'Average', np.nan, 'Excellent']
})

print("Original DataFrame:\n", df_missing)

df_cleaned = df_missing.copy()

df_cleaned['ID'] = df_cleaned['ID'].fillna(0).astype(int) 
df_cleaned['Score'] = df_cleaned['Score'].fillna(df_cleaned['Score'].mean())
df_cleaned['Remarks'] = df_cleaned['Remarks'].fillna('Unknown')

print("\nDataFrame after replacing missing values:\n", df_cleaned)