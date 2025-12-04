import numpy as np
import random
a = np.random.randint(10, 20, (10, 5))
print(a)
b = a.mean(axis=1)
print("b:", b)
