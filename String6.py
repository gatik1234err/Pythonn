char = "a"

sen = input("Enter a String: ")

count = 0

for i in sen:
    if i == char:
        count += 1
print(f"Number of time a occur is {count}")
