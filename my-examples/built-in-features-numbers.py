import math
import random

print(abs(-5))  # Output: 5
print(abs(3))

print(round(3.14159, 2))  # Output: 3.14
print(round(4.5))

print(min(3, 7, 1, 9))

print(max(3, 7, 1, 9))  # Output: 9


print(pow(2, 3))  # Output: 8

print(sum([1, 2, 3, 4]))  # Output: 10


print(int(3.7))      # Output: 3
print(int('10'))

print(float(3))      # Output: 3.0
print(float('3.14'))

print(complex(1, 2))    # Output: (1+2j)

print(math.floor(3.7))  # Output: 3

print(math.ceil(3.1))

print(math.sqrt(16))

print(math.log(100, 10))  # Output: 2.0
print(math.log(2.718))

print(math.exp(2))

print(math.sin(math.pi / 2))  # Output: 1.0
print(math.cos(math.pi))      # Output: -1.0
print(math.tan(math.pi / 4))   # Output: 1.0

print(random.random())  # Output: A random number between 0 and 1 (e.g., 0.3745401188473625)
print(random.randint(1, 10))  # Output: A random integer between 1 and 10 (e.g., 7)

print(random.choice([1, 2, 3, 4, 5]))  # Output: A random choice (e.g., 3)

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)  # Output: A shuffled list, e.g., [4, 2, 1, 3, 5]

temperature = -5
print(abs(temperature))  # Output: 5


price = 19.995
print(round(price, 2))  # Output: 20.0


prices = [12, 20, 15, 30]
print(min(prices))  # Output: 12 (cheapest)
print(max(prices))  # Output: 30 (most expensive)


investment = 100
interest_rate = 0.02
years = 3
final_amount = investment * pow(1 + interest_rate, years)
print(final_amount)  # Output: 106.1208


shopping_list = [10, 20, 30, 40]
print(sum(shopping_list))  # Output: 100

total = "15"
discount = 5
print(int(total) + discount)  # Output: 20


quantity = "2"
price = 3.5
print(float(quantity) / price)  # Output: 0.5714


real_part = 2
imaginary_part = 3
number = complex(real_part, imaginary_part)
print(number)  # Output: (2+3j)


price = 25.99
print(math.floor(price))  # Output: 25

people = 7
pizzas_needed = math.ceil(people / 3)
print(pizzas_needed)  # Output: 3

area = 16
side_length = math.sqrt(area)
print(side_length)  # Output: 4


flip = random.random()
if flip > 0.5:
    print("Heads")
else:
    print("Tails")

dice_roll = random.randint(1, 6)
print(dice_roll)  # Output: A random number between 1 and 6


deck = [1, 2, 3, 4, 5]
random.shuffle(deck)
print(deck)  # Output: A shuffled deck of cards










