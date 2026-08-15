from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class UPI(PaymentStrategy):
    def pay(self, amount):
        print("Payment of", amount, "made using UPI")


class CreditCard(PaymentStrategy):
    def pay(self, amount):
        print("Payment of", amount, "made using Credit Card")


class DebitCard(PaymentStrategy):
    def pay(self, amount):
        print("Payment of", amount, "made using Debit Card")


class PaymentProcessor:
    def __init__(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount):
        self.strategy.pay(amount)


print("Payment Methods")
print("1. UPI")
print("2. Credit Card")
print("3. Debit Card")

choice = input("Enter your choice: ")
amount = float(input("Enter amount: "))

if choice == "1":
    strategy = UPI()
elif choice == "2":
    strategy = CreditCard()
elif choice == "3":
    strategy = DebitCard()
else:
    print("Invalid choice")
    exit()

processor = PaymentProcessor(strategy)
processor.process_payment(amount)
