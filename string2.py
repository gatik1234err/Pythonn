def is_palindrome(s: str) -> bool:
    s = s.replace(' ', '').lower()
    return s == s[::-1]


a = input("Enter String")
print(is_palindrome(a))
