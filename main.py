import random

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

user_choice = int(input('What do you choose? Type "0" for rock, "1" for paper and "2" for scissors. '))

if user_choice == 0:
  print(rock)
elif user_choice == 1:
  print(paper)
elif user_choice == 2:
  print(scissors)

print('computer chose: ')

computer_choice = random.randint(0,2)


if computer_choice == 0:
  print(rock)
elif computer_choice == 1:
  print(paper)
elif computer_choice == 2:
  print(scissors)

if user_choice >= 3 or user_choice <= -3:
  print('You lose. You chose an invalid number.')
elif user_choice == computer_choice:
  print('It\'s a draw.')

elif (user_choice == 0 and computer_choice == 2) \
| (user_choice == 1 and computer_choice == 0) \
| (user_choice == 2 and computer_choice == 1):
  print('You won.')

elif (computer_choice == 0 and user_choice == 2) \
|(computer_choice == 1 and user_choice == 0) \
|(computer_choice == 2 and user_choice == 1):
  print('The computer won.')