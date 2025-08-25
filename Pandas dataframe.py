import pandas as pd
# Creating a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
print(df)

# Accessing Columns (# select one column)
print(df[['Name']])


# Adding a New Column
df['Salary'] = [70000, 80000, 90000]
print(df)


# Dropping a Column
df = df.drop('City', axis=1)
print(df)


print(df.loc[[0]])

#Return row 0 and 1:
#use a list of indexes:
print(df.loc[[0, 1]])


# Add a list of names to give each row a name:
import pandas as pd
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df)


dat = pd.read_csv("data.csv")
print(dat.info())
# shows first and last five rows
print(dat.head())
print(dat.tail())
print(dat.describe())
