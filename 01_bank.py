# bank.py

from module_account import Account

def main():
    accounts = {}  # Dictionary to store accounts by account number

    while True:
        print("\n--- Bank Account Management System ---")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Display Account Info")
        print("6. Exit")
        choice = input("Select an option (1-6): ")

        match choice:
            case '1':
                account_holder = input("Enter account holder's name: ")
                account_number = input("Enter account number: ")
                if account_number in accounts:
                    print("Account already exists.")
                else:
                    accounts[account_number] = Account(account_holder, account_number)
                    print("Account created successfully!")

            case '2':
                account_number = input("Enter account number: ")
                if account_number in accounts:
                    amount = float(input("Enter amount to deposit: "))
                    accounts[account_number].deposit(amount)
                else:
                    print("Account not found.")

            case '3':
                account_number = input("Enter account number: ")
                if account_number in accounts:
                    amount = float(input("Enter amount to withdraw: "))
                    accounts[account_number].withdraw(amount)
                else:
                    print("Account not found.")

            case '4':
                account_number = input("Enter account number: ")
                if account_number in accounts:
                    balance = accounts[account_number].check_balance()
                    print(f"Current balance: ${balance:.2f}")
                else:
                    print("Account not found.")

            case '5':
                account_number = input("Enter account number: ")
                if account_number in accounts:
                    accounts[account_number].display_account_info()
                else:
                    print("Account not found.")

            case '6':
                print("Exiting the system. Goodbye!")
                break

            case _:
                print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
