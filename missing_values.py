import numpy as np
a = np.array([1, 2, np.nan, 4, np.nan])
print(np.isnan(a).sum())
np.where(np.isnan(a), np.nanmean(a), a)

print(a)
