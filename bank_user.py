from helpers import checkIfUserExists, checkIfAmtIsAvailable
from utils import users


class BankUser:
    def __init__(self, username, account_number, pin, current_balance):
        self.username = username
        self.account_number = account_number
        self.pin = pin
        self.current_balance = current_balance

    # transfer
    def transfer(self, recipientAccountNumber):
        # Check if the account number in valid
        user_result = checkIfUserExists(recipientAccountNumber, users)
        if user_result:
            transfer_amount = int(input("\nEnter Amount to Be Transfer: "))
            pin = int(input("Enter PIN: "))
            if (pin == user_result["pin"]):
                if (checkIfAmtIsAvailable(user_result, transfer_amount)):
                    # Subtract the amount from the current user balance
                    self.current_balance -= transfer_amount
                    # Add amount to the reciepient account
                    user_result["current_balance"] += transfer_amount
                
                    print("\n=========================================")
                    print("😊😊😊 Transfar Successfull😊😊😊 \n User has Been Credited")
                    print("=========================================")
                else:
                    print("Insufficient funds")

            else:
                print("You Pin is Incorrect")

    # withdrawal

    # Deposit
