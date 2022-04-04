#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
print(f"Welcome to Tip Calc!")
bill = float(input("What's the total bill in $s? : "))

tip = float(input("How much tip would you like to give? 10, 12, 15? :"))
people = int(input("How many people to split the bill? : "))

tip_as_percentages = tip / 100
bill_including_tip = tip_as_percentages * bill
total_bill = bill + bill_including_tip
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

print(f"\n Each person should pay: ${final_amount}")
