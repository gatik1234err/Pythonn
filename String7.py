def longest_word(sentence):
    words = sentence.split()
    longest = max(words, key=len)
    return longest


sentence = input("Enter your dsring")
print(longest_word(sentence))
