def string_repeat(number, string):
    return string * number

# Example usage:
print(string_repeat(2, "HawaiiPizza"))  # "HawaiiPizzaHawaiiPizza"


def no_space(string):
    return string.replace(" ", "")

# Example usage:
print(no_space("Hawaii Pizza"))  # "HawaiiPizza"


def number_to_string(number):
    return str(number)

# Example usage:
print(number_to_string(123))  # "123"


def boolean_to_string(boolean):
    return str(boolean)

# Example usage:
print(boolean_to_string(True))  # "True"


def abbrev_name(string):
    words = string.split()
    return f"{words[0][0]}.{words[1][0]}"

# Example usage:
print(abbrev_name("Hawaii Pizza"))  # "H.P"

def name_length(string):
    words = string.split()
    return [f"{word} {len(word)}" for word in words]

# Example usage:
print(name_length("hawaii pizza"))  # ["hawaii 6", "pizza 5"]


def remove_orders(string):
    orders = string.split(',')
    orders = orders[1:-1]  # Remove first and last elements
    return ",".join(orders)

# Example usage:
print(remove_orders("1,2,3,4"))  # "2,3"


def food_menu(food_list):
    return [f"{index + 1}. {item}" for index, item in enumerate(food_list)]

# Example usage:
print(food_menu(["Hawaii Pizza", "Diablo Pizza"]))  # ["1. Hawaii Pizza", "2. Diablo Pizza"]


