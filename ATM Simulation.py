transaction_no = 0
newbalance = 0
totaldeposit = 0
deposit = 0
withdraw = 0
totalwithdraw = 0
customerstransactions = 0

customers = int(input("Enter the number of customers to be processed"))
for count in range(1, customers + 1):
    balance = float(input("enter your account balance"))
    customerstransaction = 0
    transaction = 0
    while transaction != 4:
        print("customer number:", count)
        print("1. check Balance")
        print("2. Deposit")
        print("3. withdraw")
        print("4. Exit")
        transaction = int(input("which transaction do you wish to perform?"))
        if transaction == 1:
            print("Your current balance is:", balance)
            customerstransaction = customerstransaction + 1
            customerstransactions = customerstransactions + 1
        elif transaction == 2:
            deposit = float(input("Enter the amount you wish to deposit:"))
            while deposit <= 0:
                print("amount is invalid, re-enter valid amount")
                deposit = float(input("Enter the amount you wish to deposit:"))
            balance = deposit + balance
            totaldeposit = deposit + totaldeposit
            customerstransaction = customerstransaction + 1
            customerstransactions = customerstransactions + 1
            print("your new balance is:", balance)
        elif transaction == 3:
            withdraw = float(input("Enter the amount you wish to withdraw:"))
            while withdraw <= 0 or withdraw > balance:
                print("amount is invalid, re-enter valid amount")
                withdraw = float(input("Enter the amount you wish to withdraw:"))
            totalwithdraw = totalwithdraw + withdraw
            balance = balance - withdraw
            print("new balance is;", balance)
            customerstransaction = customerstransaction + 1
            customerstransactions = customerstransactions + 1
        elif transaction == 4:
            print("session ended")
            print("your final balance is:", balance)
            print("total number of transactions performed is:", customerstransaction)
        else:
            print("invalid")
print("the total number of customers processed is", customers)
print("total amount deposited is:", totaldeposit)
print("the total amount withdrawn is:", totalwithdraw)
print("total transactions performed is:", customerstransactions)
