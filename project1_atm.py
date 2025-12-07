balance = 200000
pin = 2006
print("Welcome to the ATM")
while True:
    checkpoint1 = int(input("Enter PIN: "))
    if checkpoint1 != pin:
        print("Invalid PIN")
        break
    else:
        print("Login Successful")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        checkpoint2 = int(input("Enter the choice: "))
        if checkpoint2 == 1:
            print("Your Balance:", balance)
        elif checkpoint2 == 2:
            amount = int(input("Enter amount to deposit: "))
            balance += amount
            print("Deposit Successful! New Balance:", balance)
        elif checkpoint2 == 3:
            amount = int(input("Enter amount to withdraw: "))
            if amount > balance:
                print("Insufficient Balance!")
            else:
                balance -= amount
                print("Withdraw Successful! Remaining:", balance)
        elif checkpoint2 == 4:
            print("Thank you for using the ATM!")
            break
        else:
            print("Invalid choice!")
