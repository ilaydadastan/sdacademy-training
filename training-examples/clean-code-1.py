"""
this module contains clean code examples
....
"""



book_title = "Book title"
book_price = 20
# this is for calculate total price with tax
book_quantity = 5

TAX_RATE = 0.08


def calculate_total_price_with_tax(book_price, book_quantity, tax_rate):
    """
    This function calculates the total price of books, including tax.
    It multiplies the book price by the quantity and adds the tax.
    """
    total_price = book_price * book_quantity
    total_price_with_tax = total_price + (total_price * tax_rate)
    return total_price_with_tax


def greet_customer():
    print("Welcome to the bookstore!")


purchase_amount = 100

if purchase_amount >= 50:
    print("you qualify for a 10% discount!")
else:
    print("no discount available")


books = ["Book 1", "Book 2", "Book 3"]

for book in books:
    print(book)


discounted_prices = []
for price in [100, 150, 200]:
    discounted_prices.append((price, price * 0.9))
print(discounted_prices)

# discounted_prices = [(price, price * 0.9) for price in [100, 150, 200]]
# print(discounted_prices)


try:
    result = 10 / 0
except ZeroDivisionError:
    print("you can not divide by zero!")



# bad example
def process_order(order):
    total = 0
    for item in order:
        price = item["price"]
        discount = item["discount"]
        discounted_prices = price - (price * discount / 100)
        total += discounted_prices
    print(f"Total price: {total}")


# good example
def calculate_discounted_price(price, discount):
    return price - (price * discount / 100)


def get_order_total(order):
    total = sum(calculate_discounted_price(item["price"], item["discount"]) for item in order)
    return total


def print_order_total(order):
    total = get_order_total(order)
    print(total)


# bad example (too many nested levels)

def process_scores(scores):
    for score in scores:
        if score >= 50:
            if score >= 70:
                if score >= 90:
                    print("Excellent score")
                else:
                    print("Good score")
            else:
                print("Passed")
        else:
            print("Failed")

# good example
def process_scores(scores):
    for score in scores:
        if score < 50:
            print("Fail")
            continue
        if score < 70:
            print("Pass")
            continue
        if score < 90:
            print("Good")
            continue
        print("Excellent")






















