import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('Patreon.csv')

# Check if 'Launched' column exists
if 'Launched' not in df.columns:
    raise ValueError("The 'Launched' column is missing from the CSV file.")

# Convert 'Launched' to a datetime object
df['Launched'] = pd.to_datetime(df['Launched'], format='%b-%y', errors='coerce')

# Check for conversion errors
if df['Launched'].isnull().any():
    print("Warning: Some 'Launched' dates could not be converted and are set to NaT.")

# Drop rows with NaT in 'Launched' column after conversion
df.dropna(subset=['Launched'], inplace=True)

# Set hierarchical index with 'Rank' and 'Launched'
df.set_index(['Rank', 'Launched'], inplace=True)

# Display the DataFrame with hierarchical indexing
print("DataFrame with Hierarchical Index ('Rank' and 'Launched'):")
print(df.head())  # Display first few rows for inspection

# Perform basic aggregations
total_patrons = df['Patrons'].sum()
average_days_running = df['DaysRunning'].mean()

print("\nTotal Patrons:", total_patrons)
print("Average Days Running:", average_days_running)

# Access data for a specific rank and launch date
# Ensure the date format matches
try:
    specific_data = df.loc[(1, pd.Timestamp('2020-01-01'))]
    print("\nData for Rank 1 in Jan-20:")
    print(specific_data)
except KeyError as e:
    print(f"Error accessing specific data: {e}")

# Access a range of ranks within a specific launch month
try:
    rank_range = df.loc[pd.IndexSlice[10:20, pd.Timestamp('2020-02-01')], :]
    print("\nData for Ranks 10 to 20 in Feb-20:")
    print(rank_range)
except KeyError as e:
    print(f"Error accessing range data: {e}")

# Group by 'Launched' year and aggregate
df['Year'] = df.index.get_level_values('Launched').year
aggregated_by_year = df.groupby('Year').agg(
    total_patrons=('Patrons', 'sum'),
    average_days_running=('DaysRunning', 'mean')
).reset_index()

print("\nAggregated Data by Year:")
print(aggregated_by_year)
