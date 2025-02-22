"""
ATM Pin Verification
Problem:
Create an ATM Pin Verification System where the user must enter the correct PIN to access their account. The correct PIN is 1234.

Criteria:
The user has up to 3 attempts to enter the correct PIN.
If the PIN is correct, print "PIN verified successfully! Access granted."
If the PIN is incorrect, print how many attempts are left.
After 3 incorrect attempts, lock the user out and print "Incorrect PIN. You have been locked out."
Ensure the program only accepts numeric input for the PIN.

Steps:
Prompt the user to enter their PIN.
Check if the entered PIN matches 1234.
Provide feedback on the remaining attempts.
Lock the user out after 3 failed attempts.
"""


def atm_pin_verification():
    correct_pin = "1234"  # Predefined correct PIN
    attempts = 0
    max_attempts = 3

    print("Welcome to the ATM!")

    while attempts < max_attempts:
        entered_pin = input("Enter your PIN: ")
        attempts += 1

        if entered_pin == correct_pin:
            print("PIN verified successfully! Access granted.")
            break
        else:
            if attempts < max_attempts:
                print(f"Incorrect PIN. You have {max_attempts - attempts} attempt(s) left.")
            else:
                print("Incorrect PIN. You have been locked out.")
                break


atm_pin_verification()


def atm_pin_verification():
    correct_pin = "1234"
    max_attempts = 3

    print("Welcome to the ATM!")

    for attempt in range(1, max_attempts + 1):
        entered_pin = input("Enter your PIN: ")

        if entered_pin == correct_pin:
            print("PIN verified successfully! Access granted.")
            return
        else:
            remaining_attempts = max_attempts - attempt
            if remaining_attempts > 0:
                print(f"Incorrect PIN. You have {remaining_attempts} attempt(s) left.")
            else:
                print("Incorrect PIN. You have been locked out.")


atm_pin_verification()
