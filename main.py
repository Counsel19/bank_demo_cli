from bank_user import BankUser
from helpers import checkIfUserExists
from utils import users


def main():
    print("=========================================")
    print("Welcome to Ayo's Banking App")
    print("=========================================")

    account_number = int(input("\nEnter your Account Number: "))

    user_result = checkIfUserExists(account_number, users)

    if not (user_result):
        return print("\nInvalid Account Number! \nPlease enter a valid Account Number")

# Create an instance of a Bank User
    current_user = BankUser(account_number=user_result["account_number"],
                            current_balance=user_result['current_balance'],
                            pin=user_result["pin"],
                            username=user_result["username"],)
    print("""
 ============================================
 Plese Select an Operation to be carried out: E.g 1 for Transfer
        
 1. Transfer
 2. Deposit
 3. Withdrawal
 4. Quit
 =============================================
      """)

    user_option = input("Select: ")

    if (user_option == "1"):
        r_account_number = int(input("\nEnter Recepient Account Number: "))
        current_user.transfer(r_account_number)


if __name__ == '__main__':
    main()
