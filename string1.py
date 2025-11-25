
def count_characters(input_string):
    vowels = "aeiouAEIOU"
    vowels_count = 0
    consonants_count = 0
    digits_count = 0
    spaces_count = 0

    for char in input_string:
        if char in vowels:
            vowels_count += 1
        elif char.isdigit():
            digits_count += 1
        elif char.isspace():
            spaces_count += 1
        elif char.isalpha():
            consonants_count += 1

    return vowels_count, consonants_count, digits_count, spaces_count


user_input = input("Enter a string: ")
v, c, d, s = count_characters(user_input)
print(f"Vowels: {v}, Consonants: {c}, Digits: {d}, Spaces: {s}")
