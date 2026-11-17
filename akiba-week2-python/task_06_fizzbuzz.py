# FizzBuzz (1 to 100) 
print("--- Standard FizzBuzz (1 to 100) ---")

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)


# Challenge custom range
print("\n--- Challenge FizzBuzz (Custom Range) ---")

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

for num in range(start, end, 1):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)