import pandas as pd

# Sample raw data
data = {
    "Name": ["Payal", "Aman", "Riya", "Payal", None],
    "Age": [20, 21, None, 20, 22],
    "Marks": [85, 90, 78, 85, None]
}

# Create DataFrame
df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing Age with average age
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Fill missing Marks with average marks
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

# Fill missing Name with 'Unknown'
df["Name"] = df["Name"].fillna("Unknown")

print("\nCleaned Data:")
print(df)

print("\nDataset Information:")
print(df.info())