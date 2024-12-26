print("Welcome TO Love Calculator")
a = input("What's your Name? ")
b = input("What's is your loveones Name? ")

combine = a + b
lower = combine.lower()

t = lower.count("t")
r = lower.count("r")
u = lower.count("u")
e = lower.count("e")

true = t + r + u + e

l = lower.count("l")
o = lower.count("o")
v = lower.count("v")
e = lower.count("e")

love = l + o + v + e
score = int(str(true) + str(love))

if (score <10) or (score > 90):
  print(f"Your Love Score is {score}, you guys are not alike " )
elif (score >= 40) and (score <= 50):
   print(f"Your Love Score is {score} , You guys are Okay Together " )
else:
   
  print(f"Your Love Score is {score}")




    







  



