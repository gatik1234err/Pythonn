import random

# Generate a random 3-digit number
secret_number = random.randint(100, 999)
secret_digits = [int(d) for d in str(secret_number)]
secret_sorted = sorted(secret_digits)

tries = 0
max_tries = 10

# Some random print statements
print("Welcome to the 3-Digit Number Guessing Game!")
print("I have selected a random 3-digit number. You have 10 tries to guess it.")
print("If you guess the digits correctly but in the wrong order, I'll tell you!")


# While loop to play the game
while tries < max_tries:
    tries += 1
    try:
        guess = int(
            input(f"Attempt {tries}/{max_tries}: Enter a 3-digit number: "))
        if not (100 <= guess <= 999):
            print("Please enter a valid 3-digit number (100-999).")
            continue
        guess_digits = [int(d) for d in str(guess)]
        if guess_digits == secret_digits:
            print(
                f"Congratulations! You guessed it correctly in {tries} tries.")
            break
        elif sorted(guess_digits) == secret_sorted:
            print("The digits are correct, but not in the same place.")
        else:
            print("Incorrect guess.")
    except ValueError:
        print("Please enter a valid integer.")
        continue

if tries == max_tries:
    print(
        f"Sorry, you've used all {max_tries} tries. The number was {secret_number}.")
