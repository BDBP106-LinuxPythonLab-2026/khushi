import pandas as pd

# Read CSV file
df = pd.read_csv("diabetes.csv")

# (i) Print column names
print("Column names:")
print(df.columns)

# (ii) Print first 10 rows
print("\nFirst 10 rows:")
print(df.head(10))

# (iii) Mean of BloodPressure
print("\nMean Blood Pressure:")
print(df["BloodPressure"].mean())

# (iv) First 4 rows of columns 3, 4 and 5
print("\nFirst 4 rows of columns 3, 4 and 5:")
print(df.iloc[:4, 2:5])

# (v) Min-max normalization
BP = df["BloodPressure"]

df["NormalizedBP"] = (
    BP - BP.min()
) / (
    BP.max() - BP.min()
)

print("\nNormalized Blood Pressure:")
print(df[["BloodPressure", "NormalizedBP"]].head())

# (vi) Categorize age

def categorize_age(age):

    if age <= 18:
        return "Youth"

    elif age <= 50:
        return "Adult"

    else:
        return "Senior"


# Apply function
df["age category"] = df["Age"].apply(categorize_age)

print("\nAge categories:")
print(df[["Age", "age category"]].head())

# Display final dataframe
print("\nUpdated DataFrame:")
print(df.head())