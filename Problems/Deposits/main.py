from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, starting_sum, interest=None):
        self.sum = starting_sum
        self.interest = interest

    @abstractmethod
    def add_money(self, amount):
        ...

    def add_interest(self):
        ...


class SavingsAccount(Account):
    def add_money(self, amount):
        if amount >= 10:
            self.sum += amount
        else:
            print("Cannot add to SavingsAccount: amount too low.")


class Deposit(Account):
    def add_money(self, amount):
        if amount >= 50:
            self.sum += amount
        else:
            print("Cannot add to Deposit: amount too low.")

    def add_interest(self):
        self.sum *= (1 + self.interest)


new_savings = SavingsAccount(50)
new_savings.add_money(5)  # prints the following message:
# Cannot add to SavingsAccount: amount too low.
new_savings.add_money(30)
new_savings.add_interest()
print(new_savings.sum)
# 80




new_deposit = Deposit(60, 0.078)
new_deposit.add_money(70)
new_deposit.add_interest()

print(new_deposit.sum)
# 140.14
