# Your Life in Weeks
# Instructions
# I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.

# https: // waitbutwhy.com/2014/05/life-weeks.html

# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

# It will take your current age as the input and output a message with our time left in this format:

# You have x days, y weeks, and z months left.

# Where x, y and z are replaced with the actual calculated numbers.

# Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.

# Example Input
# 56
# Example Output
# You have 12410 days, 1768 weeks, and 408 months left.

print(f"Your Life in Weeks board! \n")

current_age = input(f"enter your current age: ")

time_left = 90 - int(current_age)

time_left_in_days = time_left * 365

time_left_in_weeks = time_left * 52

time_left_in_months = time_left * 12

print("\n")

print(
    f"You have {time_left_in_days} days, {time_left_in_weeks} weeks, and {time_left_in_months} months left.\n")

print(f"Don't Worry, it's just calculation!")
