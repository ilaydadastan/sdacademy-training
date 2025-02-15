import menu
import order
import payment


def main():
    items = menu.get_menu()
    print("Menu", items)

    order_taken = order.take_order(items[0])
    print(order_taken)

    total_amount = 15
    payment_status = payment.process_payment(total_amount)
    print(payment_status)


if __name__ == "__main__":
    main()

