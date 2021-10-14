import datetime as dt
import time


class BankAccountError(Exception):
    pass


def create_bank_account(initial_balance):
    balance = initial_balance

    def deposit(amount):
        nonlocal balance

        balance += amount

        return amount

    def withdraw(amount):
        nonlocal balance

        if amount > balance:
            raise BankAccountError(
                f"You can't withdraw {amount} given a balance of {balance}"
            )

        balance -= amount

        return amount

    def bank_account():
        return balance

    bank_account.deposit = deposit
    bank_account.withdraw = withdraw

    return bank_account


def fetch_special_offers():
    time.sleep(3)

    return [{"description": "Free shipping.", "expires": dt.date(2021, 12, 31)}]
