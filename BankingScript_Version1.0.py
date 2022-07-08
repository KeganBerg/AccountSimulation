import time
checking = 20000.00
savings = 50000.00
valid_checking_responses = ["Checking", "checking_balance"]
valid_savings_responses = ["Savings", "savings_balance"]
valid_deposit_responses = ["Deposit", "valid_deposit_responses"]
valid_withdraw_responses = ["Withdraw", "valid_withdraw_responses"]

time.sleep(1)
print("Thank you for choosing the Bank of Kegan")
time.sleep(1)
choice = str(input("Type \"Deposit\" or \"Withdraw\" \n "))
if choice == "Deposit":
    print("Deposit Transaction Initiated: Checking ")
    time.sleep(.5)
    print("Please choose an account you would like to Deposit into. ")
    account_choice = str(input("Type \"Checking\" or \"Savings\" \n "))
    if account_choice in valid_checking_responses:
        print("Checking Account Loading... \n")
        time.sleep(2)
        print("Checking: $", checking, "\n")
        time.sleep(2)
        amount1 = float(input("Please type how much you'd like to valid_deposit_responses. \n "))
        time.sleep(.5)
        print("$", amount1, "Transaction Pending...")
        time.sleep(2)
        checking = (checking + amount1)
        print("Your new balance is: ")
        print("$", checking)
        exit()

    elif account_choice in valid_savings_responses:
        print("Savings Account Loading... ")
        time.sleep(2)
        print("Savings: $", savings)
        time.sleep(2)
        amount2 = float(input("Please type how much you'd like to valid_deposit_responses. \n "))
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
    print("Type what account you would like to valid_withdraw_responses from. ")
    account_choice = str(input("Checking or Savings"))
    if account_choice in valid_checking_responses:
        print("Withdraw Transaction Initiated: Checking ")
        print("Checking Account Loading... ")
        time.sleep(2)
        print("Checking \n Balance: ", checking)
        withdraw1 = float(input("Type how much you would like to valid_withdraw_responses. "))
        print("$", withdraw1, "valid_withdraw_responses transaction pending... ")
        time.sleep(2)
        if checking == 0:
            print("You broke broke, make some money and come back later.")
        else:
         checking -= withdraw1
         print("your new balance is: $", checking)
    elif account_choice in valid_savings_responses:
        time.sleep(.5)
        print("Savings Account Loading... ")
        time.sleep(2)
        print("Savings \n Balance: ", savings)
        withdraw2 = float(input("Type how much you would like to valid_withdraw_responses. "))
        print("$", withdraw2, "valid_withdraw_responses transaction pending... ")
        time.sleep(2)
        if savings == 0:
            print("You broke broke, make some money and come back later.")
        else:
         savings -= withdraw2
         print("your new balance is: $", savings)
    else:
        print("Please choose a valid argument.")
