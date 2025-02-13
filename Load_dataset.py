# Import necessary libraries
import pandas as pd
from sqlalchemy import create_engine

# Database connection details
DB_NAME = "mandefro"  # Name of the PostgreSQL database
DB_USER = "postgres"  # Database username
DB_PASSWORD = "mande123"  # Database password
DB_HOST = "localhost"  # Host where the database is running 
DB_PORT = "5432"  # Default PostgreSQL port

# Load cleaned dataset from a CSV file
file_path = "Cleaned_Ecommerce_Dataset.csv"  # Path to the cleaned dataset
df = pd.read_csv(file_path)  # Read the CSV file into a pandas DataFrame

# Define the table name in PostgreSQL
table_name = "ecommerce_data"

# Create a PostgreSQL connection using SQLAlchemy
engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

# Define the expected columns to ensure they match before loading into the database
expected_columns = [
    "item_id", "status", "created_at", "sku", "price", "qty_ordered", "grand_total", 
    "category_name_1", "sales_commission_code", "discount_amount", 
    "payment_method", "Working Date", "BI Status", "MV", "Year", "Month", 
    "Customer Since", "M-Y", "FY", "Customer ID"
]

# Check if any expected columns are missing from the DataFrame
missing_columns = [col for col in expected_columns if col not in df.columns]

# Attempt to load the DataFrame into the PostgreSQL table
try:
    df.to_sql(table_name, engine, if_exists="replace", index=False)  # Load data into the database, replacing existing table if needed
    print(f"Cleaned data successfully loaded into PostgreSQL table '{table_name}'.")  # Success message
except Exception as e:
    print(f"❌ Error loading data: {e}")  # Print error message if loading fails
