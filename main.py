import time
checking_balance = 0.0
savings_balance = 0.0

time.sleep(1)
print("Thank you for choosing the Bank of Kegan")
time.sleep(1)
transaction_type = input("Type \"Deposit\" or \"Withdraw\" \n ")
if transaction_type == "Deposit":
    # str("Deposit")              # This does nothing, no equal sign.
    account_type = input("Type \"Checking\" or \"Savings\" \n ")
    if account_type == "Checking":
        str("Checking")              # This does nothing, no equal sign.
        print("Checking Account Loading... \n")
        print("Checking: $", checking_balance, "\n")
        time.sleep(2)
        checking_deposit_amount = float(input("Please type how much you'd like to valid_deposit_responses. \n "))
        print("$", checking_deposit_amount, "Transaction Pending...")
        time.sleep(2)
        checking_balance += checking_deposit_amount
        print("Your new balance is: ")
        print("$", checking_balance)
        exit()

    elif account_type == "Savings":
        str("Savings")              # This does nothing, no equal sign.
        print("Savings Account Loading... ")
        print("Savings: $", savings_balance)
        time.sleep(2)
        savings_deposit_amount = float(input("Please type how much you'd like to valid_deposit_responses. \n "))
        print("$", savings_deposit_amount, "valid_deposit_responses transaction pending... ")
        time.sleep(2)
        savings_balance += savings_deposit_amount
        print("Your new balance is: ")
        print("$", savings_balance)
        exit()
    else:
        print("Please choose a valid argument ")
elif transaction_type == "Withdrawal":
    str("Withdraw")              # This does nothing, no equal sign.
    print("Type what account you would like to valid_withdraw_responses from. ")
    account_type_choice = input("Checking or Savings")
    if account_type_choice == "Checking":
        str("Checking")
        print("Checking Account Loading... ")
        time.sleep(2)
        print("Checking \n Balance: ", checking_balance)
        checking_withdrawal_amount = float(input("Type how much you would like to valid_withdraw_responses. "))
        print("$", checking_withdrawal_amount, "valid_withdraw_responses transaction pending... ")
        time.sleep(2)
        checking_balance -= checking_balance
        print("your new balance is: $", checking_balance)
    elif account_type_choice == "Savings":
        str("Savings")              # This does nothing, no equal sign.
        print("Savings Account Loading... ")
        time.sleep(2)
        print("Savings \n Balance: ", savings_balance)
        savings_withdrawal_amount = float(input("Type how much you would like to valid_withdraw_responses. "))
        print("$", savings_withdrawal_amount, "valid_withdraw_responses transaction pending... ")
        time.sleep(2)
        savings_balance -= savings_balance
        print("Your new balance is: $", savings_balance)
