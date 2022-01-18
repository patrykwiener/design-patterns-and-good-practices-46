class Employee:
    pass


class Company:
    def __init__(self, employee):
        self.employee = employee


if __name__ == '__main__':
    employee = Employee()
    company = Company(employee=employee)
    t=0

