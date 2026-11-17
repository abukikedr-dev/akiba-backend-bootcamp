# Number Analyzer

# Ask for the first number before the loop to set initial largest and smallest values
first_num = int(input("Enter number 1: "))

largest = first_num
smallest = first_num
total_sum = first_num
even_count = 0
odd_count = 0

# Check if the first number is even or odd
if first_num % 2 == 0:
    even_count = even_count + 1
else:
    odd_count = odd_count + 1

# Loop 9 more times to get the remaining 9 numbers (total 10 numbers)
for i in range(2, 11):
    num = int(input("Enter number " + str(i) + ": "))
    
    # Update sum
    total_sum = total_sum + num
    
    # Check for largest and smallest
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
        
    # Check for even or odd
    if num % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1

# Calculate the average after the loop finishes
average = total_sum / 10

# Display all results
print("\n--- Results ---")
print("Largest number:", largest)
print("Smallest number:", smallest)
print("Total sum:", total_sum)
print("Average:", average)
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)