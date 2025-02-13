# Import the pandas library for data manipulation
import pandas as pd  

# Define the file path to the dataset 
file_path = "Pakistan Largest Ecommerce Dataset.csv"

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(file_path)  

# Print the number of rows in the dataset
print(f"Number of rows: {len(df)}")  
