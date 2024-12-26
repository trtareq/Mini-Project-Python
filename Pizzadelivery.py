 print("Welcome To Shif Pizza Deliveries")
size = input("Which Size Pizza do you want? S, M or L : ")
add = input("Do you want pepperoni? y or n : ")
xtra = input("Do you want extra cheese?  y or n : ")

bill = 0


if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25 



if add == "y":
  if size == "S":
   bill += 2
  
  else:
   bill += 3




if xtra == "y":
 
   bill += 1
  

print(f"Your Total bill is ${bill}")




    







  



