#if condition:
    # code to run if the condition is true


is_raining = True  # This is a variable
if is_raining:
    print("Take an umbrella!")


#if condition:
    # code to run if the condition is true
#else:
    # code to run if the condition is false


is_raining = False
if is_raining:
    print("Take an umbrella!")
else:
    print("Enjoy the sunshine!")


number = 10
if number > 5:
    print("The number is greater than 5.")
else:
    print("The number is not greater than 5.")


number = 7
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

#dictionary sample
person = {"name": "John", "age": 25}
if person["age"] >= 18:
    print(person["name"] + " is an adult.")
else:
    print(person["name"] + " is a minor.")

#comparing list items
fruits = ["apple", "banana", "cherry"]
if "apple" in fruits:
    print("Apple is in the list.")
else:
    print("Apple is not in the list.")

#logical

age = 25
has_ticket = True
if age >= 18 and has_ticket:
    print("You can enter the concert.")
else:
    print("You cannot enter the concert.")

#multiple conditions with elif
temperature = 30
if temperature > 30:
    print("It’s hot outside!")
elif temperature >= 20:
    print("It’s warm outside.")
else:
    print("It’s cold outside.")


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