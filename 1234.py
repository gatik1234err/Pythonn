# Takes input for name
a = input("Enter your name")
# Takes input for age
b = input("Enter your age")

# Converts string into int
c = int(b)

# Prints the name
print(f"Your name is {a}")

if c < 18:
    # Prints the age
    print("Welcome to the Diddy Party ")
else:
    print("You are not allowed")
