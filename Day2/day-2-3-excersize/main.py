# 🚨 Don't change the code below 👇
age = input("What is your current age?\n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#ages left till 90 
age_left = (90 - int(age) )
months = age_left * 12
weeks = age_left * 52
days = age_left * 365 

print(f"You have {days} days, {weeks} weeks and {months} months left.")