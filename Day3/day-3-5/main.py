# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# name1 = input("Give one name")
# name2 = input("Give another name")

def same_letters(a,b):
    # return sum ( a[i] == b[i] for i in range(len(b)) 
  m=0
  n=0
  for i in range (len(a)):
   if a[i] in b:
     m += 1;
   n += 1
  return m
  
ch = "true love"
total1 = same_letters(ch,name1)
print(f"letter matched {total1}")
total2 = same_letters(ch,name2)
print(f"letter matched {total2}")
total = str(total1) + str(total2)
if total > "90" or total < "10":
  print(f"Your score is {total}, You go together like coke and mentos.")
elif total > "40"  or total < "50":
  print(f"Your score is {total}, You are alright together.")
else:
  print(f"Your score is {total}.")
