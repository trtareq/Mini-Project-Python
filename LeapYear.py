print("Welcome To The Ultimate Leap Year Calculator")

a = int(input("Enter a Year: "))

if a % 4 == 0:
 if a % 100 == 0:
   if a % 400 == 0:
     print(str(a) + " " + "Is a Leap  Year")
     
   else:
     print(str(a) + " " + " Is Not a Leap  Year")
 else:
   print(str(a) + " " + " Is a Leap  Year")
else:
  print(str(a) + " " + " Is Not a Leap  Year")



    







  



