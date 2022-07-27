# Nested if and Elif 

print ("Welcome to the Adventure Park")
height= int (input("What is your height in cm ?"))

if height >= 120:
  print ("You can enjoy the rides!")
  age = int(input("What is your age ?"))
  if age < 12 :
    print ("Pay 5$")
  elif age >= 12 and age <= 18 :
    print("Pay 7$")
  else:
    print("Pay 12$")
else:
 print ("Sorry, height requires >= 150 cm ")

# 
  