from abc import ABC
from typing import List


class Account:
    def __init__(self, balance: float = 0):
        self._balance = balance

    def deposit(self, amount: float):
        pass

    def withdraw(self, amount: float):
        pass

    def get_balance(self) -> float:
        pass


class AccountHolder(ABC):

    def __init__(self, id: int, email: str, accounts: List[Account]):
        self._id = id
        self._email = email
        self._accounts = accounts


class IndividualHolder(AccountHolder):

    def __init__(self, id: int, email: str, accounts: List[Account], name: str, pesel: str):
        super().__init__(id, email, accounts)
        self._name = name
        self._pesel = pesel


class CorporateHolder(AccountHolder):

    def __init__(self, id: int, email: str, accounts: List[Account], contact: str):
        super().__init__(id, email, accounts)
        self._contact = contact
