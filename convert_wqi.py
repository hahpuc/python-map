import pandas as pd

# Load the CSV file into a DataFrame
csv_file_path = 'test-wqi.csv'  # Replace with the actual path to your CSV file
df = pd.read_csv(csv_file_path)

# Convert the "Date" column to datetime format for easy filtering
df['Date'] = pd.to_datetime(df['Date'])

# Filter data based on a specific date or date range
start_date = '2020-11-01'
end_date = '2020-11-01'

filtered_data = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

filtered_data.to_csv('filtered_data.csv', index=False)

# Display the filtered data
print(filtered_data)
