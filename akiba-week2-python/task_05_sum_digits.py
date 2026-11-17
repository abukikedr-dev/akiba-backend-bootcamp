number = int(input("Enter a number: "))
total_sum = 0
while number > 0:
    total_sum += number % 10  # this gets the last number because any number divided by 10 gives the reminder the last digit
    number = number // 10     # this removes the last digit from the number because anuy number divided by 10 gives the quotient without the lastdigit

print("Sum of digits:", total_sum)