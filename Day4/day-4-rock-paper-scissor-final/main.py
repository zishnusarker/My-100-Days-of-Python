rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

game_images = [rock, paper, scissors]

print("what do you choose ?")
user_choice = int(input("Type 0 for Rock \nType 1 for Paper \nType 2 for Scissors .\n"))
if user_choice > 2 or user_choice < 0 :
  print("You give an invalid number")
else :
  print(game_images[user_choice])
  computer_choice = random.randint(0, 2)
  print(f"Computer chose {computer_choice}")
  print(game_images[computer_choice])
  
  if user_choice == computer_choice :
    print("It is a draw")
  elif user_choice == 0 and computer_choice == 2 :
    print("You win")
  elif computer_choice == 0 and user_choice == 1 :
    print("You lose")
  elif computer_choice > user_choice :
    print("You lose")
  elif user_choice > computer_choice :
    print("You win")
