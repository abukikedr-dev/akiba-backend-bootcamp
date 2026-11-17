#number guessing game 
print("==============guessing the number=============")
nums = [7]
attempts = 0

while True:
    user_guess = int(input("Enter your guess: "))
    attempts += 1

    if user_guess in nums:
        print("You guessed correctly!")
        print("Number of attempts:", attempts)
        break
    else:
        print("Wrong guess. Try again.")
        
#challenge giving the player only 5 attempts

nums = [7]
attempts = 0
print("===============you have 5 attempts!================")
for i in range(6):
    user_guess = int(input("Enter your guess: "))
    attempts += 1
    if user_guess in nums:
        print("You guessed correctly!")
        print("Number of attempts:", attempts)
        break
    else:
        print("Wrong guess. Try again.")
        if attempts <= 5: #we used this to prevent from saying "you have -1 attempts left" athe end
            print(f"you have {5-attempts} attempts left!")
if user_guess not in nums:
    print ("game over!")      