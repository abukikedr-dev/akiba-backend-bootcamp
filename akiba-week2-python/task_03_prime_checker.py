# Ask the user to enter a number
num = int(input("Enter a whole number: "))

# Numbers less than or equal to 1 are not prime
if num <= 1:
    print(num, "is NOT a prime number.")
elif num == 2:
    print(num, "is a prime number.")
else:
    # Assume the number is prime until proven otherwise
    is_prime = True
    
    # Loop to check for divisors from 2 up to the square root of the number.
    # CHALLENGE EXPLANATION: 
    # We don't need to check every number because if a number 
    # has a factor larger than its square root, it must also have a matching 
    # paired factor smaller than its square root. Therefore, if no divisors 
    # are found up to the square root, the number is prime.
    limit = int(num ** 0.5) + 1
    
    for i in range(2, limit):
        if num % i == 0:
            is_prime = False
            break # Exit loop once a factor is found
            
    if is_prime:
        print(num, "is a prime number.")
    else:
        print(num, "is NOT a prime number.")