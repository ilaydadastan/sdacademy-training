"""
Job Applicant System
Problem:
Create a system that manages job applicants. The system should allow adding, removing, and viewing applicants. Each applicant has a name, email, and the position they applied for.

Criteria:
Add Applicant:

Add an applicant by entering their name, email, and the position they applied for.
Ensure that no duplicate applicants are added based on the email address.
Remove Applicant:

Remove an applicant from the system by their email address.
If no applicant is found with that email, notify the user.
View Applicants:

Display a list of all applicants with their name, email, and applied position.
If there are no applicants, notify the user.
Menu:

Provide a menu with the following options:
1: Add applicant
2: Remove applicant
3: View all applicants
4: Exit the system

Steps:
Implement a class JobApplicantSystem with methods to add, remove, and view applicants.
Display the menu for the user to interact with the system.
Based on user input, perform the corresponding action: add, remove, view, or exit.
"""


class JobApplicantSystem:
    def __init__(self):
        self.applicants = []

    def add_applicant(self, name, email, position):
        if any(applicant['email'] == email for applicant in self.applicants):
            print(f"An applicant with email {email} already exists.")
        else:
            self.applicants.append({'name': name, 'email': email, 'position': position})
            print(f"Applicant {name} for {position} added.")

    def remove_applicant(self, email):
        for applicant in self.applicants:
            if applicant['email'] == email:
                self.applicants.remove(applicant)
                print(f"Applicant with email {email} removed.")
                return
        print(f"No applicant found with email {email}.")

    def view_applicants(self):
        if not self.applicants:
            print("No applicants in the system.")
        else:
            print("\nApplicants List:")
            for applicant in self.applicants:
                print(f"Name: {applicant['name']}, Email: {applicant['email']}, Position: {applicant['position']}")

def applicant_system():
    system = JobApplicantSystem()

    while True:
        print("\nMenu:")
        print("1. Add applicant")
        print("2. Remove applicant")
        print("3. View applicants")
        print("4. Exit")

        choice = input("Please choose an option (1-4): ")

        if choice == "1":
            name = input("Enter applicant name: ")
            email = input("Enter applicant email: ")
            position = input("Enter position applied for: ")
            system.add_applicant(name, email, position)
        elif choice == "2":
            email = input("Enter email of applicant to remove: ")
            system.remove_applicant(email)
        elif choice == "3":
            system.view_applicants()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# Start the job applicant system
applicant_system()
