import pandas as pd
import numpy as np

# Sample dataset creation
data = {
    'Creator ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Name': ['Alice Smith', 'Bob Johnson', 'Carlos Ruiz', 'Daniella Lee', 'Emily Zhang', 
             'Fran Miller', 'George Tan', 'Hanna White', 'Ian Gomez', 'Julia Brown'],
    'Category': ['Art', 'Music', 'Podcasts', 'Writing', 'Videos', 'Art', 'Music', 'Writing', 'Videos', 'Art'],
    'Patrons': [1200, 800, 500, np.nan, 900, np.nan, 300, 250, 450, 1000],
    'Monthly Earnings': [3500.50, 2400.00, 1500.00, np.nan, 3000.75, 0, 900.00, 800.00, 1400.25, 3100.00],
    'Country': ['USA', 'Canada', 'Mexico', 'South Korea', 'China', 'USA', 'Singapore', 'Australia', 'Argentina', 'USA']
}

df = pd.DataFrame(data)

# 1. Handling Missing Data
# Fill missing 'Patrons' with median value and 'Monthly Earnings' with 0
df['Patrons'].fillna(df['Patrons'].median(), inplace=True)
df['Monthly Earnings'].fillna(0, inplace=True)

#Hierarchical Indexing
df.set_index(['Country', 'Category'], inplace=True)


# Aggregate by Category and compute total and average earnings
category_aggregation = df.groupby('Category')['Monthly Earnings'].agg(['sum', 'mean'])

# Display
print("Updated DataFrame with Hierarchical Indexing:")
print(df)
print("\nAggregation Results (Total and Average Earnings by Category):")
print(category_aggregation)
