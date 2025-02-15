def calculate_total_price(book_price, book_quantity, tax_rate):
    """
    This function calculates the total price of books,
    including tax. It multiplies the book price by the
    quantity and adds the tax.
    """
    total_price = book_price * book_quantity
    total_price_with_tax = total_price + (total_price * tax_rate)
    return total_price_with_tax


try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")
