
# week 2 mini project bank system

correct_pin = "1234"
attempts = 3
is_authenticated = False

# Challenge Requirement: 3-Attempt PIN System
while attempts > 0:
    print("===== AKIBA BANK =====")
    entered_pin = input("Enter your PIN: ")
    
    if entered_pin == correct_pin:
        print("PIN correct!")
        print("Welcome to Akiba Bank.\n")
        is_authenticated = True
        break
    else:
        attempts = attempts - 1
        if attempts > 0:
            print("Incorrect PIN.")
            print("Attempts remaining:", attempts, "\n")
        else:
            print("Too many incorrect attempts.")
            print("Your account is locked.")

# Main Bank Menu (runs only if PIN is correct)
if is_authenticated:
    balance = 1000
    transactions = 0  # Bonus Challenge: Transaction counter
    running = True

    while running:
        print("\n===== AKIBA BANK =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        # Feature 1: Check Balance
        if choice == "1":
            print("Your current balance is:", balance, "Birr")
            
        # Feature 2: Deposit Money
        elif choice == "2":
            deposit = float(input("Enter deposit amount: "))
            if deposit > 0:
                balance = balance + deposit
                transactions = transactions + 1
                print("Deposit successful!")
                print("Your new balance is:", balance, "Birr")
            else:
                print("Invalid amount! Please enter a positive number.")
                
        # Feature 3: Withdraw Money
        elif choice == "3":
            withdraw = float(input("Enter withdrawal amount: "))
            if withdraw <= 0:
                print("Invalid amount! Please enter a positive number.")
            elif withdraw > balance:
                print("Insufficient balance!")
            else:
                balance = balance - withdraw
                transactions = transactions + 1
                print("Withdrawal successful!")
                print("Your new balance is:", balance, "Birr")
                
        # Feature 4: Exit
        elif choice == "4":
            print("Transactions made:", transactions)
            print("Thank you for using Akiba Bank!")
            print("Goodbye!")
            running = False
            
        # Feature 5: Invalid Option
        else:
            print("Invalid option.")
            print("Please choose a valid option.")