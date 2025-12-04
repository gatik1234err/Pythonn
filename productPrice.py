import numpy as np


prices = np.random.randint(100, 2000, (10, 1))
print("Original prices:\n", prices.flatten())


discounts = np.where(prices >= 1500, 0.20,
                     np.where(prices >= 1000, 0.10,

                              np.where(prices >= 500, 0.05, 0)))

updated_prices = prices * (1 - discounts)
discount_percent = discounts * 100


for i in range(len(prices)):
    orig = prices[i][0]
    disc = discount_percent[i][0]
    new = updated_prices[i][0]
    if disc > 0:
        print(f"₹{orig}  {disc}% off  ₹{new:.2f}")
    else:
        print(
            f"₹{orig} (sir itna discount aapko milega agar aapne break nhi diya toh)")
