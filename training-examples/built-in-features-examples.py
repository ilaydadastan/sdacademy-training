# abs value
import math
import random
from random import randint
from random import *


temperature = -5
print(abs(temperature))


# calculate how much money you will have after 3 year, 100 euros, interest rate 2%,
# we will find final amount

investment = 100
interest_rate = 0.02
years = 3
final_amount = investment * pow(1 + interest_rate, years)
print(final_amount)

# math ceil

people = 7
pizzas_needed = math.ceil(people / 3)
print(pizzas_needed)


# math sqrt
area = 16
side_length = math.sqrt(area)
print(side_length)

#random module functions

# you are flipping a coin, simulate this and please check if it is above or below 0.5

flip = random.random()
print(flip)
if flip > 0.5:
    print("heads")
else:
    print("tails")


# when you play a board game, you roll a dice to get a random number between 1 and 6

dice_roll = random.randint(1, 6)
print(dice_roll)


url = "https://www.example.com"
domain = url.find(".com")
print(domain)

error_message = "404 not found"
fixed_message = error_message.replace("404", "500")
print(fixed_message)


email = "contact@company.com "
print(email.strip())


addresses = "Baker Street, Talinn; 742 city center"
addresses_list = addresses.split(";")
print(addresses_list)
