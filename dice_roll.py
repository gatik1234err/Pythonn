import numpy as np
rolls = np.random.randint(1, 7, 1000)
counts = np.bincount(rolls)
print(rolls)
for i in range(1, 7):
    print(f"{i}: {(counts[i]/1000)*100}")
