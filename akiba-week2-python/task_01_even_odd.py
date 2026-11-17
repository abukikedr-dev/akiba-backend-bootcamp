#even or odd checker
number = int(input("Enter a number: "))

if number == 0:
    print("The number is Zero (which is even).")
elif number % 2 == 0:
    print("The number is Even.")
else:
    print("The number is Odd.")