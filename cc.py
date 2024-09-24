import pandas as pd

# Define the path to the zip file and the output CSV file
zip_path = 'data/winemag-data-130k-v2.csv.zip'
output_csv_path = 'data/reviews-per-country.csv'

# Read the CSV file directly from the zip archive
reviews = pd.read_csv(zip_path, compression='zip')

# Create a summary of the data by country
data = reviews.groupby('country').agg(
    count=('points', 'size'),
    average_points=('points', 'mean')  # Rename to 'average_points'
).reset_index()

# Round the average points to one decimal place
data['average_points'] = data['average_points'].round(1)

# Rename columns to match the expected output
data.rename(columns={'average_points': 'points'}, inplace=True)

# Write the summary data to a new CSV file
data.to_csv(output_csv_path, index=False)

print(f"Summary file has been created: {output_csv_path}")

# Testing if the output CSV file contains the expected columns
def test_columns_exist():
    expected_columns = ['country', 'count', 'points']
    try:
        df = pd.read_csv(output_csv_path)
        for col in expected_columns:
            assert col in df.columns
        print("All expected columns are present.")
    except AssertionError as e:
        print(f"Column check failed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the test function
test_columns_exist()

