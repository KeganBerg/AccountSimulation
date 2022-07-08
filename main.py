import time
checking = 0
savings = 0

time.sleep(1)
print("Thank you for choosing the Bank of Kegan")
time.sleep(1)
choice = input("Type \"Deposit\" or \"Withdraw\" \n ")
if choice:
    str("Deposit")
    account_choice = input("Type \"Checking\" or \"Savings\" \n ")
    if account_choice:
        str("Checking")
        print("Checking Account Loading... \n")
        print("Checking: $", checking, "\n")
        time.sleep(2)
        amount1 = int(input("Please type how much you'd like to deposit. \n "))
        print("$", amount1, "Transaction Pending...")
        time.sleep(2)
        checking = (checking + amount1)
        print("Your new balance is: ")
        print("$", checking)
        exit()

    if account_choice:
        str("Savings")
        print("Savings Account Loading... ")
        print("Savings: $", savings)
        time.sleep(2)
        amount2 = int(input("Please type how much you'd like to deposit. \n "))
        print("$", amount2, "deposit transaction pending... ")
        time.sleep(2)
        savings = (savings + amount2)
        print("Your new balance is: ")
        print("$", savings)
        exit()
    else:
        print("Please choose a valid argument ")
if choice:
    str("Withdraw")
    print("Type what account you would like to withdraw from. ")
    choice2 = input("Checking or Savings")
    if choice2:
        str("Checking")
        print("Checking Account Loading... ")
        time.sleep(2)
        print("Checking \n Balance: ", checking)
        withdraw1 = int(input("Type how much you would like to withdraw. "))
        print("$", withdraw1, "withdraw transaction pending... ")
        time.sleep(2)
        checking = withdraw1 - checking
        print("your new balance is: $", checking)
    if choice2:
        str("Savings")
        print("Savings Account Loading... ")
        time.sleep(2)
        print("Savings \n Balance: ", savings)
        withdraw2 = int(input("Type how much you would like to withdraw. "))
        print("$", withdraw2, "withdraw transaction pending... ")
        time.sleep(2)
        savings = withdraw2 - savings
        print("your new balance is: $", savings)





