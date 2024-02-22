def calculate_square_and_cube(number):
    square = number ** 2
    cube = number ** 3
    return square, cube

# Input number
input_number = 2

# Calculate square and cube
square_result, cube_result = calculate_square_and_cube(input_number)

# Print the results
print("Input:", input_number)
print("Square:", square_result)
print("Cube:", cube_result)
