import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '*', '+']

a = int(input("How Many letters do you want?\n "))

b = int(input(f"How Many numbers do you want?\n "))

c = int(input(f"How Many symbols do you want?\n "))

password_list = []
for char in range(1, a + 1):
  random_char = random.choice(letters)
  password_list.append(random_char) 

for num in range(1, b + 1):
  random_num = random.choice(numbers)
  password_list.append(random_num)

for sym in range(1, c + 1):
  random_sym = random.choice(symbols)
  password_list.append(random_sym)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""

for char in password_list:
  password += char
print(f"Your Password is {password}")



  






  
  
