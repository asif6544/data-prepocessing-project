import pandas as pd

# Load dataset
df = pd.read_csv("raw_data.csv")

# Show dataset info
print(df.info())

# Handle missing values
df.fillna(df.mean(numeric_only=True), inplace=True)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Save cleaned data
df.to_csv("cleaned_data.csv", index=False)

print("Data preprocessing completed successfully!")
