
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    if num1 == num2 and num1 == num3:
        print("All three numbers are equal.")
    elif num1 == num2 or num1 == num3:
        print("The largest number is", num1, "and there are equal numbers.")
    else:
        print("The largest number is:", num1)

elif num2 >= num1 and num2 >= num3:
    if num2 == num3:
        print("The largest number is", num2, "and there are equal numbers.")
    else:
        print("The largest number is:", num2)

else:
    print("The largest number is:", num3)