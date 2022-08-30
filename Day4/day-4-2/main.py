import random 
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
# print(names[0])
#Write your code below this line 👇
num_items= len(names)
random_choice= random.randint(0, num_items-1)
print(random_choice)
person_who_will_pay = names[random_choice]
print(person_who_will_pay + " is going to but the meal.")