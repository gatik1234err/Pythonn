import matplotlib.pyplot as plt
import numpy as np
a = np.arange(1, 8)
b = [1, 7, 8, 6, 10, 3, 11]
aa = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
plt.stem(a, b)
plt.xticks(a, aa)
plt.show()
