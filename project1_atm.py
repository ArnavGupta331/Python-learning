balance=200000
pin=2006
print("Welcome to the ATM")
checkpoint1=int(input("enter ATM pin: "))
if checkpoint1 != pin:
    print("Invalid pin")
else:
    if True:
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
checkpoint2=int(input("Enter the choice"))
if checkpoint2 == 1:
            print("Your Balance:", balance)
elif checkpoint2 == 2:
            amount = int(input("Enter amount to deposit: "))
            balance += amount
            print(" Money Deposited")
            print("New Balance:", balance)

elif checkpoint2 == 3:
            amount = int(input("Enter amount to withdraw: "))
            if amount > balance:
                print("Insufficient Balance!")
            else:
                balance -= amount
                print("Withdrawal Successful")
                print("Remaining Balance:", balance)

elif checkpoint2 == 4:
    print("Thank you for using the ATM!")
else:
            print("Invalid choice! Please select again.")