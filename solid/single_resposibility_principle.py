class Computer:

    def __init__(self):
        self._brand = None
        self._model = None

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        self._brand = value

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value


class Inventory:

    def search_inventory(self, computer: Computer):
        pass


computer = Computer()
print(computer.brand)
computer.brand = 'Dell'

inventory = Inventory()
inventory.search_inventory(computer=computer)
