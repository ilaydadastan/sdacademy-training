# Defining a simple function
def welcome_message():
    print("Welcome to Python programming!")


welcome_message()


def multiply_by_two(num):
    return num * 2


double = multiply_by_two  # Assigning function to a variable
print(double(10))  # Output: 20


# Defining a lambda function
multiply = lambda a, b: a * b
print(multiply(4, 7))  # Output: 28


global_value = "Global Scope"

def check_scope():
    local_value = "Local Scope"
    print(global_value)  # Accessible inside function
    print(local_value)  # Accessible only inside function

check_scope()
# print(local_value)  # This would cause an error as local_value is not defined globally.


def display_age(age):
    print(f"Your age is {age} years.")

display_age(25)  # Output: Your age is 25 years.


count = 0

def increase():
    global count
    count += 2
    print(count)

increase()  # Output: 2
increase()  # Output: 4


def introduce(name="User"):
    print(f"Hello, {name}!")

introduce()  # Output: Hello, User!
introduce("John")  # Output: Hello, John!

def function_scope():
    text = "Inside the function"
    print(text)

function_scope()
# print(text)  # Would cause an error since 'text' is local to the function.


def calculate_area(length, width):
    area = length * width
    return area

# Call the function with arguments
length = 5
width = 10
result = calculate_area(length, width)

print(f"The area of the rectangle is: {result}")


def is_valid_email(email):
    if "@" not in email or "." not in email:
        return False
    return True

email = "test@example.com"
if is_valid_email(email):
    print(f"{email} is valid.")
else:
    print(f"{email} is not valid.")


