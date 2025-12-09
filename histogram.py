import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

a = pd.read_csv("./students.csv")
b = a["Student Age"]
plt.hist(b, bins=33)
plt.show()
