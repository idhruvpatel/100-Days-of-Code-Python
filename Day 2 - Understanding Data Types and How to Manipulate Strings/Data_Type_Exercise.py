# Data Types
# Instructions
# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

# Warning. Do not change the code on lines 1-3. Your program should work for different inputs. e.g. any two-digit number.

# Example Input
# 39
# Example Output
# 3 + 9 = 12

# 12

two_digit_numbers = input("Type a two digit number: ")

first_digit = two_digit_numbers[0]
last_digit = two_digit_numbers[1]

print(first_digit + " + " + last_digit + " =")
print(int(first_digit) + int(last_digit))
