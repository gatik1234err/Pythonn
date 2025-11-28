import numpy as np

a = np.array([5, 7, 8, 2, 1])
print(a)

mean = 0
for i in a:
    mean = mean + i
mean /= len(a)
print(a.mean())

b = np.std(a)
print(b)

variance = 0
for i in a:
    variance += (i - mean) ** 2
variance /= len(a)
std_dev = variance ** 0.5
print(std_dev)

mean = a.mean()
c = 0
for i in a:
    differ = np.sum((i - mean) ** 2)
    squared_value = differ.mean()
    c = np.sqrt(squared_value)

print(c)
print(np.std(a))
