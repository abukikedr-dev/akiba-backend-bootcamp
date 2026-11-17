correctpin=1234
count=0
for i in range(1,4,1):
    pin=int(input("Enter Your PIN Number:"))
    count+=1
    if pin == correctpin:
        print("Access Granted!")
        break
    else:
        print("Incorrect PIN.")
        print(f"Attempts remaining {3-i}")

    