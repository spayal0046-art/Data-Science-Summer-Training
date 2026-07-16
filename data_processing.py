# Project 2: Python-Based Data Processing

import pandas as pd

# Sample Student Data
data = {
    "Name": ["Aman", "Payal", "Riya", "Rahul", "Sneha"],
    "Age": [20, 21, 20, 22, 21],
    "Marks": [85, 92, 78, 88, 95]
}

# Create DataFrame
df = pd.DataFrame(data)

print("Student Data")
print(df)

print("\nAverage Marks:", df["Marks"].mean())

print("Highest Marks:", df["Marks"].max())

print("Lowest Marks:", df["Marks"].min())