print("Welcome To The Rock Paper & Scissor Game")

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

a = int(input("Your Choice ! 0 for Rock , 1 for Paper, 2 for Scissors!  "))
import random

b = random.randint(0,2)
print(f"Computer chosed {b}")
if a >= 3 or a < 0:
  print("You Lose")
elif a ==0 and b == 2:
  print("You Win")
  
elif b > a:
  print("You Lose")
elif a == b:
  print("It's a Draw")
elif b == 0 and a == 2:
  print("You Lose")
elif a > b:
  print("You Won")




