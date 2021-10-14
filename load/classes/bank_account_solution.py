class BankAccountError(Exception):
    pass


class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

        return self.balance

    def withdraw(self, amount):
        self.__balance -= amount

        return self.balance


class SavingsAccount(BankAccount):
    interest_rate = 0.02

    def withdraw(self, amount):
        if amount > self.balance:
            raise BankAccountError("your balance is too low")

        return super().withdraw(amount)

    def credit_interest(self):
        self.deposit(self.balance * SavingsAccount.interest_rate)

        return self.balance


class CurrentAccount(BankAccount):
    def __init__(self, balance=0, overdraft=0):
        super().__init__(balance=balance)

        self.__overdraft = overdraft

    def withdraw(self, amount):
        if amount > self.balance + self.__overdraft:
            raise BankAccountError("your balance (inc. overdraft) is too low")

        return super().withdraw(amount)


class Mortgage:
    pass


class CurrentAccountMortgage(CurrentAccount, Mortgage):
    pass


class StarterAccount(SavingsAccount):
    def __init__(self):
        super().__init__(balance=100)


def main():
    savings_account = SavingsAccount()
    print(savings_account.deposit(100))
    print(savings_account.credit_interest())
    print(savings_account.withdraw(50))

    try:
        print(savings_account.withdraw(100))
    except BankAccountError as exc_info:
        print(exc_info)

    current_account = CurrentAccount(overdraft=100)
    print(current_account.deposit(100))
    print(current_account.withdraw(50))
    print(current_account.withdraw(100))

    starter_account = StarterAccount()
    print(starter_account.balance)


if __name__ == "__main__":
    main()
