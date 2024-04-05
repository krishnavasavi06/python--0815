def is_anagram_number(n1,n2):
    str1=str(n1)
    str2=str(n2)
    return sorted(str1)==sorted(str2)
number1=int(input("Enter the first number:"))
number2=int(input("Enter the second number."))
if is_anagram_number(number1,number2):
    print("The numbers are anagram numbers.")
else:
    print("The numbers are not anagram numbers.")