from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, age: int, gender: str):
        self.age = age
        self.gender = gender

    @abstractmethod
    def is_mammal(self):
        pass


class Dog(Animal):
    def __init__(self, age: int, gender: str, color: str):
        super().__init__(age, gender)
        self.color = color

    def is_mammal(self):
        return True

    def bark(self):
        pass

    def fetch(self):
        pass


class Zebra(Animal):
    def __init__(self, age: int, gender: str, is_wild: bool):
        super().__init__(age, gender)
        self.is_wild = is_wild

    def is_mammal(self):
        return True

    def run(self):
        pass


class Duck(Animal):
    def __init__(self, age: int, gender: str, beak_color: str = 'yellow'):
        super().__init__(age, gender)
        self._beak_color = beak_color

    def is_mammal(self):
        return False

    def swim(self):
        pass

    def fly(self):
        pass

    def quack(self):
        pass
