import pandas as pd
import os 

# Create a simple DataFrame with column names
data = {
    "name": ['Alice', 'Bob', 'Charlie'],
    "Age": [25, 30, 35],
    "city": ['new york', 'london', 'babilona']
}
df = pd.DataFrame(data)

# Add a new row (make sure column names match exactly)
df.loc[len(df)] = ['girl1', 40, 'newyork']

# Create directory if not exists
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

# File path
file_path = os.path.join(data_dir, 'sample_data.csv')

# Save the DataFrame to a csv file, including column names
df.to_csv(file_path, index=False)

print(f"CSV file saved to {file_path}")
