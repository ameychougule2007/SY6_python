class UPI:
    def pay(self, amount):
        print("Paid", amount, "using UPI")


class Card:
    def pay(self, amount):
        print("Paid", amount, "using Card")


class Cash:
    def pay(self, amount):
        print("Paid", amount, "using Cash")


class Payment:
    def __init__(self, method):
        self.method = method

    def make_payment(self, amount):
        self.method.pay(amount)


choice = input("Enter payment method (upi/card/cash): ")
amount = int(input("Enter amount: "))

if choice == "upi":
    method = UPI()
elif choice == "card":
    method = Card()
else:
    method = Cash()

payment = Payment(method)
payment.make_payment(amount)