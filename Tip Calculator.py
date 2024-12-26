print("Welcome to the Tip Calculator")

a = input("Insert  total Bill : ")
b = input("How many person will split the bill: ")
c = input("What percentage tip would you like to give? 10,12 or 15? ")

total = float(a) * float(c) / 100
result = (float(a) + float(total)) / float(b)
print("Every person should pay " + str(round(result,2)))


