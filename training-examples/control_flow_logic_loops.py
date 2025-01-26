#loops

for i in range(1, 10, 2): # 1, 3, 5, 7, 9
    print("Hello")

#print all even numbers from 2 to 10
for i in range(2, 10, 2):
    print(i)



# let's print whether numbers from 1 to 100 are even or odd

for i in range(1, 100):
    if i % 2 == 0:
        print(f'{i} is even')
    else:
        print(f"{i} it's odd")


name = "ilayda"
age = 25
print(f"My name is {name} and  I am {age} years old")


for i in range(10, 0, -1):
    print(i)


fruits = ["apple", "banana", "cherry", "strawberry"]

for fruit in fruits:
    print(f"I like {fruit}")


count = 1

while count <= 5:
    print(f"Count is {count}")
    count += 1


#guessing game

secret_number = 7
guess = None

while guess != secret_number:
    guess = int(input("Guess the secret number (1-10): "))

    if guess < secret_number:
        print("too low!")
    elif guess > secret_number:
        print("too high!")
    else:
        print("you guessed it!!!!")
