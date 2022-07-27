# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = round(weight / (height * height),2)
print (f"your BMI is {bmi}")

if bmi<=18.5:
  print("You are Underweight")
elif bmi>18.5 and bmi <= 25 :
  print("you have a normal weight")
elif bmi > 25 and bmi <= 30:
  print("You are overweight")
elif bmi > 30 and bmi <= 35:
  print("You are obese")
else:
  print("You are clinically obese")


# if bmi<=18.5:
#   print("You are Underweight")
# elif bmi <= 25:
#   print("you have a normal weight")
# elif bmi <= 30:
#   print("You are overweight")
# elif bmi <= 35:
#   print("You are obese")
# else:
#   print("You are clinically obese")


