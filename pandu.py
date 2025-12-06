import pandas as pd

data = {'Product': ['Shoes', 'Watch'], 'Price (INR)': [1500, 2500]}
a = pd.DataFrame(data)
print(a)
print("\nPrice column:", a["Price (INR)"])
print("\nRow 0:", a.loc[0])
