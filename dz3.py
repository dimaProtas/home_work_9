class Worker:
    name = ''
    surname = ''
    position = 0
    _income = {"wage": 0, "bonus": 0}

class Position:
    def __init__(self, name, surname, position, _income):
        # super().__init__(name, surname, position, _income)
        self.name = name
        self.surname = surname
        self.position = position
        self._income = _income

    def get_full_name(self):
        name = self.name
        surname = self.surname
        return print(f'{name}, {surname}.')

    def get_total_income(self):
        _income = self._income
        sum_bonus = _income['wage'] + _income['bonus']
        return print(sum_bonus)


r = Position('Dima', 'Protas', 'programist', {'wage': 100,'bonus': 15})
b = Position('Irina', 'Cheri', 'finansist', {'wage': 140,'bonus': 36})
r.get_full_name()
r.get_total_income()
b.get_full_name()
b.get_total_income()

