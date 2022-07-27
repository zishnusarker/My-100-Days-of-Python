# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

check_number = number % 2

if check_number == 0:
  print(f"{number} is an even number")
else:
  print(f"{number} is a odd number")