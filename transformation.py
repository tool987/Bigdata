import pandas as pd  # Import the pandas library for data manipulation

# Load dataset
file_path = "Pakistan Largest Ecommerce Dataset.csv"  # Define the file path of the dataset
df = pd.read_csv(file_path)  # Read the CSV file into a pandas DataFrame

def clean_data(df):
    """Cleans the dataset by handling missing values, duplicates, formatting, and inconsistencies."""
    
    # Drop Fully Null Columns
    df.dropna(axis=1, how="all", inplace=True)  # Remove columns that have all values as NaN (empty columns)

    # Drop a specific column "increment_id" as it is unnecessary
    df = df.drop(columns=["increment_id"])

    # Handle Missing Values
    df.replace("", pd.NA, inplace=True)  # Convert empty string values to NaN for consistency
    df.fillna(method='ffill', inplace=True)  # Forward-fill missing values based on the previous row

    # Remove Duplicates
    df.drop_duplicates(inplace=True)  # Drop duplicate rows to avoid redundant data

    # Standardize Text Columns
    for col in df.select_dtypes(include=['object']).columns:  # Loop through all text columns
        df[col] = df[col].str.strip().str.lower()  # Remove leading/trailing spaces & convert text to lowercase

    # Fix Common Typos & Inconsistencies
    df.replace({"pakistan ": "pakistan"}, inplace=True)  # Correct typo where "pakistan " has an extra space

    # Convert Data Types
    for col in df.select_dtypes(include=['object']).columns:  # Loop through object-type columns
        try:
            df[col] = pd.to_datetime(df[col], errors='ignore')  # Convert date-like columns if applicable
        except Exception:
            pass  # Ignore errors if conversion is not possible

    for col in df.select_dtypes(include=['number']).columns:  # Loop through numeric-type columns
        df[col] = pd.to_numeric(df[col], errors='coerce')  # Convert to numeric, replacing errors with NaN

    print("\n Cleaning completed!")  # Print a message indicating successful data cleaning
    return df  # Return the cleaned DataFrame

# Apply the cleaning function
df_cleaned = clean_data(df)  # Call the function to clean the dataset

# Save cleaned dataset
df_cleaned.to_csv("Cleaned_Ecommerce_Dataset.csv", index=False)  # Save the cleaned dataset as a new CSV file

print("\n Final dataset saved as 'Cleaned_Ecommerce_Dataset.csv'.")  # Print confirmation message
print("\n🔍 Final dataset info:")  # Print a separator message before showing dataset info
print(df_cleaned.info())  # Display summary information about the cleaned dataset
