#If the bill was $150.00, split between 5 people, with 12% tip. 
print("Welcome to the tip calculator ")
bill = float(input("what was the total bill? $ "))
tip = int(input("How much percentage of tip would you like to give ? "))
people = int(input("How many people to split the bill ? "))
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
tip_percentage = tip / 100
tip_amount = bill * tip_percentage 
total_bill = bill + tip_amount 
bill_per_person = total_bill / people 
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
final_amount = round(bill_per_person,2)  # this will print till both 1 decunak abd 2 decimal point 
print(f"Each person should pay : ${final_amount}\n")
# Expected final amount needs to be printed like below (till 2 decimal point)
print("Expected output must have 2 decimal point values like below \n")
expected_final_amount = print("Each person should pay : %.2f" % bill_per_person )
expected_final_amount = print("Each person should pay : %.2f" % round (bill_per_person, 2))
expected_final_amount = print("Each person should pay : {:.2f}".format(bill_per_person))
expected_final_amount = print("Each person should pay : {:.2f}".format(round (bill_per_person, 2)))