#CONDITIONAL STATEMENT

is_raining = False

if is_raining:
    print("take an umbrella")
else:
    print("enjoy the sunshine")


number = 7
if number > 5:
    print("the number is greater than 5")
else:
    print("the number is not greater than 5")


if number % 2 == 0:
    print("the number is even")
else:
    print("the number is odd")


person = {"name": "Ilayda", "age": 15}
if person["age"] > 18:
    print(person["name"] + " is an adult")
else:
    print(person["name"] + " is not and adult")


fruits = ["apple", "banana", "cherry"]
if "apple" in fruits:
    print("apple is in the list")
else:
    print("apple is not in the list")


#logical operators in conditional statements

age = 25
has_ticket = False

if age >= 18 and has_ticket:
    print("you can enter the concert")
else:
    print("you cannot enter the concert")



#multiple conditions with elif


temperature = 2
if temperature > 25:
    print("it's hot outside!")
elif temperature >= 10:
    print("it's warm outside")
else:
    print("it's cold outside")


score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")















