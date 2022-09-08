#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""
for char in range(0, nr_letters):
  # password += random.choice(letters)
  p = random.choice(letters)
  password = password + p
  
for char in range (0, nr_symbols):
  # password += random.choice(symbols)
  q = random.choice(symbols)
  password = password + q
  
for char in range(0,nr_numbers):
  #password += random.choice(numbers)
  r = random.choice(numbers)
  password = password + r
  
print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_list = []
for char in range(0, nr_letters):
   password_list += random.choice(letters)
  # password_list.appened(random.choice(letters))
  
for char in range (0, nr_symbols):
  password_list += random.choice(symbols)
  # password_list.appened(random.choice(letters))
  
for char in range(0,nr_numbers):
  password_list += random.choice(numbers)
  #password_list.appened(random.choice(numbers))
  
print(password_list)


random.shuffle(password_list)
print (password_list)

password1 = ""
for char in password_list:
  password1 += char 

print(f"your final password is :{password1}")