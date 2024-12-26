print("Welcome to the Rollercoaster")

a = int(input("Uour height? "))
bill = 0

if a >= 180:
  print("You can Ride, Welcome!")
  b = int(input("Age: "))
  if b < 12:
    bill = 5
    print("Price 5$")
  elif b <= 18 :
    bill = 7
    print("Price 7$")
  else:
    bill = 12
    print("Price 12$")

  photo = input("Do you want Photo? y or n: ")
  if photo == "y":
    bill += 3
  print(f"Your Bill is {bill} ")
  
    
else:
  print("Better Luck Next Time")


    







  



