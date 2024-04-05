def vowel(char):
    vowels = 'aeiouAEIOU'
    return char in vowels

# Input a character from the user
character = input("Enter a character: ")

# Check if the character is a vowel
if vowel(character):
    print(character, "is a vowel.")
else:
    print(character, "is not a vowel.")
