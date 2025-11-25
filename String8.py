sen = input("Enter a String: ")

result = ""

for char in sen:
    if char not in result:
        result += char
print(result)
