def is_palindrome(num):
    num_str=str(num)
    return num_str==num_str[::-1]
num=int(input("Enter the number:"))
if is_palindrome(num):
    print(num,"is a palindrome.")
else:
    print(num,"is not a palindrome.")