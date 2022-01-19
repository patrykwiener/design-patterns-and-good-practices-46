from abc import ABC, abstractmethod


class Discount(ABC):

    @abstractmethod
    @property
    def discount(self):
        pass


class EasterDiscount(Discount):
    _EASTER_DISCOUNT = '30%'

    @property
    def discount(self):
        return f'{self._EASTER_DISCOUNT} on Easter'


class BlackFridayDiscount(Discount):
    _BLACK_FRIDAY_DISCOUNT = '50%'

    @property
    def discount(self):
        return f'{self._BLACK_FRIDAY_DISCOUNT} on Black Friday'


class MothersDayDiscount(Discount):
    _MOTHERS_DAY_DISCOUNT = '15%'

    @property
    def discount(self):
        return f'{self._MOTHERS_DAY_DISCOUNT} on Mother\'s day'


class DiscountManager:

    def process_discount(self, discount: Discount):
        pass


mothers_discount = MothersDayDiscount()
black_discount = BlackFridayDiscount()
discount_manager = DiscountManager()
discount_manager.process_discount(discount=mothers_discount)
discount_manager.process_discount(discount=black_discount)
