import pandas as pd
df = pd.DataFrame({
    "date": ["5/12/2025", "6/12/2025"],
    "amount": [500, 600],
    "category": ["vadapav", "taxi"]
})
# print(df)

a = pd.DataFrame({
    "date": ["7/12/2025"],
    "amount": [10000],
    "category": ["G lab"]
})

c = pd.concat([df, a], ignore_index=True)

# print(c["amount"].sum())

# print(c.iloc[2, 0:1])


b = pd.read_csv('./students.csv')
print(b.sort_values("Student Age"))
