a = int(input("Enter marks for sub 1"))
b = int(input("Enter marks for sub 2"))
c = int(input("Enter marks for sub 3"))
d = int(input("Enter marks for sub 4"))
e = int(input("Enter marks for sub 5"))

total = a + b + c + d + e
f = (total / 500) * 100
print(f"Total ={total}")
print("Average = ", total/5)
print(f"Percentage = {f}")
