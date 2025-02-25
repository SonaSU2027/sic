
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Load the dataset
df = pd.read_csv('IPLData.csv')

# Reading the data
print(df)

# Understanding the data structure
print(df.info())  # Provides data types and non-null values
print(df.isnull().sum())  # Check for missing values
print(df.describe())  # Summary statistics for numerical data

# Handling missing values
# Fill missing numerical values with median
df.fillna(df.median(numeric_only=True), inplace=True)

# Fill missing categorical values with mode
for col in df.select_dtypes(include=['object']).columns:
    df[col].fillna(df[col].mode()[0], inplace=True)

# Verify missing values are handled
print(df.isnull().sum())
