import random 
import my_module 

random_integer = random.randint(1,100)
print(random_integer)

print(my_module.pi)


random_float = random.random()
print(random_float)
random_float = random.random()*5
print(random_float)

# Love calculator 
love_score = random.randint(1,100)
print(f"Yout love score is {love_score}")

#list using array
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america[0])
print(states_of_america[5])
print(states_of_america[-1]) # It is the last elements of the array
print(states_of_america[-2]) 
# print(states_of_america)

dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

# changing the element in the array list 
print(dirty_dozen[0])
dirty_dozen[0] = "Blueberry"
print(dirty_dozen[0])
# print(dirty_dozen)

# adding elements in the last 
dirty_dozen.append("Watermelon")
print(dirty_dozen)
print(" ")
dirty_dozen.extend(["Sugercane", "Strawberry"])
print(dirty_dozen)