import numpy as np
import matplotlib.pyplot as plt

a = np.random.uniform(55, 25, 100)
sales = np.random.normal(55, 25, 100)
plt.boxplot([a, sales])
plt.show()
