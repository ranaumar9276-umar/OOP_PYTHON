# Topic : Encapsulation


class BankAccount:
    def __init__(self, name, balance):

        self.name = name

        self.__balance = balance

    def deposit(self, amount):

        self.__balance += amount

    def withdraw(self, amount):

        self.__balance -= amount

    def show_balance(self):

        print("=" * 50)

        print("Customer :", self.name)

        print("Current Balance :", self.__balance)

account = BankAccount(
    "Rana Umar",
    5000000000

)
account.deposit(10000)
account.withdraw(5000)
account.show_balance()