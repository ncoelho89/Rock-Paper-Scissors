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


possibilites = [rock, paper, scissors]
user_choice = input("What do you choose? Type 0 for rock, 1 for Paper, or 2 for scissors\n")
if user_choice == "0":
  print(possibilites[0])
elif user_choice == "1":
  print(possibilites[1])
elif user_choice == "2":
  print(possibilites[2])

import random
print("Computer chooses:")
computer_choice = random.choice(possibilites)
print(computer_choice)

if user_choice == "0" and computer_choice == scissors:
  print("You win")
elif user_choice == "0" and computer_choice == rock:
  print("You tie")
elif user_choice == "0" and computer_choice == paper:
  print("You lose")
elif user_choice == "1" and computer_choice == scissors:
  print("You lose")
elif user_choice == "1" and computer_choice == rock:
  print("You win")
elif user_choice == "1" and computer_choice == paper:
  print("You tie")
elif user_choice == "2" and computer_choice == scissors:
  print("You tie")
elif user_choice == "2" and computer_choice == rock:
  print("You lose")
elif user_choice == "2" and computer_choice == paper:
  print("You win")
else: 
  print("You typed an invalid number, you lose")