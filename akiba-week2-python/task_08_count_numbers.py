num= int(input("Enter positive number:"))
countof_even=0
countof_odd=0
sum=0
if num<=0:
    print("The number is not positive!,Try again.")
else:    
    for i in range(1,num+1,1):
        sum+=i
        if i % 2==0:
            countof_even +=1
        else:
            countof_odd +=1
        
    print(f"\n ==================================\n Even numbers:{countof_even} \n Odd numbers:{countof_odd} \n Sum of all numbers:{sum}\n ==================================")