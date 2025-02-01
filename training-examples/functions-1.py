
print("Hello AI")


def greet1(name):
    print("Hello, " + name)


greet1("Ilayda")


def add_numbers(a, b):
    print(a+b)


add_numbers(3, 8)


def multiply(x, y):
    return x * y


operation = multiply
print(operation(4, 5))


def greet(name: str, surname: str):
    print("Hello " + name + surname)


#changing a global variable inside a function

count = 0


def increase_count():
    global count
    count += 1
    print(count)


increase_count()
increase_count()



# bank account simulation

def deposit(balance, amount):
    balance += amount
    print("new balance:", balance)


balance = 100
deposit(balance, 50)
print("My latest balance:", balance)



#defining lambda functions

square = lambda x: x**2
print(square(5))


# multiple arguments in lambda functions
add = lambda x, y: x + y
print(add(7, 9))



# validating an email address
#ilaydastan2@gmail.com
def is_valid_email(email):
    if "@" not in email or "." not in email:
        return False
    return True

email = "ilaydastan2@gmail.com"

if is_valid_email(email):
    print("email is valid")
else:
    print(f"{email} is not valid")


#validating phone number
phone_number = "37255552222"

def is_valid_phone_number(phone_number):
    if len(phone_number) == 11 and phone_number.startswith("372") and phone_number.isdigit():
        return True
    return False


if is_valid_phone_number(phone_number):
    print("phone number is valid")
else:
    print("phone number is not valid")



# modify shopping list

shopping_list = ["bread", "milk", "eggs"]


def add_item_to_list(shopping_list, item):
    shopping_list.append(item)
    return shopping_list


def remove_item_from_list(shopping_list, item):
    if item in shopping_list:
        shopping_list.remove(item)
    return shopping_list

shopping_list = add_item_to_list(shopping_list, "apple")
shopping_list = remove_item_from_list(shopping_list, "lemon")
print(shopping_list)









