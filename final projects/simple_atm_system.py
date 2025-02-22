"""
ATM System
Problem:
Create an ATM System that verifies the user's PIN and provides options to check balance, deposit money, or withdraw money. The system should handle incorrect PIN attempts and balance checks.

Criteria:
PIN Verification:

The user has 3 attempts to enter the correct PIN (1234).
After 3 incorrect attempts, lock the user out.
Menu Options:

After a correct PIN, the user should see the menu with 4 options:
Check balance: Show the current balance.
Deposit money: Allow the user to deposit money into their account.
Withdraw money: Allow the user to withdraw money if they have enough balance.
Exit: Exit the ATM system.
Transaction Validation:

Ensure that the withdrawal amount doesn't exceed the balance.
Deposit and withdrawal amounts should be numeric.
Edge Cases:

Handle invalid choices in the menu and prompt the user again.
Ensure only numeric input is allowed for deposit and withdrawal amounts.

Steps:
Prompt the user to enter their PIN.
Check if the entered PIN is correct, and allow access if it is.
Show the menu with options to check balance, deposit, withdraw, or exit.
Allow the user to deposit or withdraw money, and update the balance accordingly.
Handle invalid inputs and ensure sufficient funds for withdrawals.

"""


def atm_system():
    pin = "1234"  # Hardcoded pin
    balance = 1000  # Starting balance
    attempts = 3

    print("Welcome to the ATM System!")

    while attempts > 0:
        entered_pin = input("Please enter your pin: ")

        if entered_pin == pin:
            print("Pin accepted. Welcome!")
            break
        else:
            attempts -= 1
            print(f"Incorrect pin. You have {attempts} attempts left.")
            if attempts == 0:
                print("You have been locked out of the ATM.")
                return

    while True:
        print("\nMenu:")
        print("1. Check balance")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Exit")

        choice = input("Please choose an option (1-4): ")

        if choice == "1":
            print(f"Your current balance is ${balance}.")
        elif choice == "2":
            deposit_amount = float(input("Enter deposit amount: $"))
            balance += deposit_amount
            print(f"You have successfully deposited ${deposit_amount}. New balance: ${balance}.")
        elif choice == "3":
            withdraw_amount = float(input("Enter withdrawal amount: $"))
            if withdraw_amount > balance:
                print("Insufficient funds.")
            else:
                balance -= withdraw_amount
                print(f"You have successfully withdrawn ${withdraw_amount}. New balance: ${balance}.")
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")


# Start the ATM system
atm_system()
