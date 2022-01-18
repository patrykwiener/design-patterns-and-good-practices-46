# pylint: disable=missing-module-docstring missing-class-docstring missing-function-docstring


class SamplePylint:  # pylint: disable=too-few-public-methods
    def __init__(self, number):
        self._number = number

    @classmethod
    def divide(cls, number):
        if number == 0:
            raise ZeroDivisionError()


class Children(SamplePylint):

    def __init__(self, name, number):
        super().__init__(number)
        self._name = name

    @classmethod
    def some_method(cls, param):
        return param in (1, 2, 3)

    @classmethod
    def some_method2(cls):
        print('bad implementation')


if __name__ == '__main__':
    sample = SamplePylint(10)
    try:
        sample.divide(0)
    except ZeroDivisionError:
        pass
    sample.divide(number=10)

    Children.some_method(4)
