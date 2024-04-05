def sum_of_digits(number):
    sum_digits = 0
    while number > 0:
        digit = number % 10  # Extract the last digit
        sum_digits += digit  # Add the digit to the sum
        number //= 10        # Remove the last digit from the number
    return sum_digits

# Input the number from the user
number = int(input("Enter an N-digit number: "))

# Calculate the sum of digits
sum_of_digits_result = sum_of_digits(number)

# Print the sum of digits
print("Sum of digits of", number, "is:", sum_of_digits_result)
