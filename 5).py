def reverse_word(word):
    reversed_word = ''
    # Iterate through the word in reverse order
    for i in range(len(word) - 1, -1, -1):
        # Append each character to the reversed_word string
        reversed_word += word[i]
    return reversed_word

# Sample Input strings
test_cases = [
    "TEMPLE",
    "SIGN UP",
    "AT-LEAST",
    "1245",
    "!@#$%"
]

# Test the program for each input string
for idx, string in enumerate(test_cases):
    reversed_string = reverse_word(string)
    print(f"Test case {idx + 1}:")
    print(f"String: {string}")
    print(f"Reverse String: {reversed_string}")
