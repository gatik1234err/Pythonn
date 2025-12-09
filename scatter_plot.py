import matplotlib.pyplot as plt
a = [10, 20, 30, 40, 5]
b = [10, 50, 30, 40, 60]
c = [10, 12, 10, 2, 14]

plt.scatter(a, c, cmap="#00FFF", s=100, label="Kyun")
plt.scatter(b, c, cmap="#00FFE", s=100, label="Kyun")

plt.grid(True)
plt.legend()
plt.show()
