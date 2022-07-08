import time
checking = 0
savings = 0
proceed1 = "Checking" or "checking_balance"
proceed2 = "Savings" or "savings_balance"
deposit = "Deposit" or "deposit"
withdraw = "Withdraw" or "withdraw"

time.sleep(1)
print("Thank you for choosing the Bank of Kegan")
time.sleep(1)
choice = str(input("Type \"Deposit\" or \"Withdraw\" \n "))
if choice == "Deposit":
    print("Deposit Transaction Initiated: Checking ")
    time.sleep(.5)
    print("Please choose an account you would like to Deposit into. ")
    account_choice = str(input("Type \"Checking\" or \"Savings\" \n "))
    if account_choice == proceed1:
        print("Checking Account Loading... \n")
        time.sleep(2)
        print("Checking: $", checking, "\n")
        time.sleep(2)
        amount1 = int(input("Please type how much you'd like to deposit. \n "))
        time.sleep(.5)
        print("$", amount1, "Transaction Pending...")
        time.sleep(2)
        checking = (checking + amount1)
        print("Your new balance is: ")
        print("$", checking)
        exit()

    elif account_choice == proceed2:
        print("Savings Account Loading... ")
        time.sleep(2)
        print("Savings: $", savings)
        time.sleep(2)
        amount2 = int(input("Please type how much you'd like to deposit. \n "))
        time.sleep(.5)
        print("$", amount2, "Transaction Pending... ")
        time.sleep(2)
        savings = (savings + amount2)
        print("Your new balance is: ")
        print("$", savings)
        exit()
    else:
     print("Please choose a valid argument ")
elif choice == "Withdraw":
    print("Withdraw Transaction Initiated: Checking ")
    print("Type what account you would like to withdraw from. ")
    choice2 = str(input("Checking or Savings"))
    if choice2 == proceed1:
        print("Withdraw Transaction Initiated: Checking ")
        print("Checking Account Loading... ")
        time.sleep(2)
        print("Checking \n Balance: ", checking)
        withdraw1 = int(input("Type how much you would like to withdraw. "))
        print("$", withdraw1, "withdraw transaction pending... ")
        time.sleep(2)
        if checking == 0:
            print("You broke broke, make some money and come back later.")
        else:
         checking = withdraw1 - checking
         print("your new balance is: $", checking)
    elif choice2 == proceed2:
        time.sleep(.5)
        print("Savings Account Loading... ")
        time.sleep(2)
        print("Savings \n Balance: ", savings)
        withdraw2 = int(input("Type how much you would like to withdraw. "))
        print("$", withdraw2, "withdraw transaction pending... ")
        time.sleep(2)
        if savings == 0:
            print("You broke broke, make some money and come back later.")
        else:
         savings = withdraw2 - savings
         print("your new balance is: $", savings)
    else:
        print("Please choose a valid argument.")
