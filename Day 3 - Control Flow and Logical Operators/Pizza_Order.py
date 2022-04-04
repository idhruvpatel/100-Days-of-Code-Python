# Pizza Order
# Instructions
# Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.

# Based on a user's order, work out their final bill.

# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1
# Example Input
# size = "L"
# add_pepperoni = "Y"
# extra_cheese = "N"
# Example Output
# Your final bill is: $28.

########################################################################################################################
#                                                       SOLUTION.                                                      #
########################################################################################################################

print(f"Welcome to our Pizzeria! \n")

size = input(f"What size of pizza will you like to have? (S / M / L) : ")
extra_pepperoni = input("Do you want to add extra Pepperoni? (Y/N): ")
extra_cheese = input("Do you want to add extra cheese? (Y/N): ")
bill = 0

if (size == 'S'):
    bill += 15
elif (size == 'M'):
    bill += 20
else:
    bill += 25


if (extra_pepperoni == "Y"):
    if (size == 'S'):
        bill += 2

    else:
        bill += 3

if (extra_cheese == "Y"):
    bill += 1

print(f"Your final bill is ${bill}.")
