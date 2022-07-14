# Агентство недвижимости
import random


class House:
    address: str
    area: float
    cost: float

    def __init__(self, address, area, cost):
        self.address = address
        self.area = area
        self.cost = cost

    def info(self):
        message = f'House is situated in {self.address}, area {self.area}, cost {self.cost}'
        return message

    def increase_cost(self, cost):
        self.cost += cost

    def decrease_cost(self, cost):
        self.cost -= cost


class Townhouse(House):
    def __init__(self, address, cost, area=60):
        super().__init__(address, area, cost)


class Person:
    name: str
    age: int
    money: float
    realty: list

    def __init__(self, name, age, realty=None, money=0):
        if realty is None:
            realty = []
        self.name = name
        self.age = age
        self.money = money
        self.realty = realty

    def info(self):
        message = f'{self.name} , возраст {self.age}, недвижимость {self.realty}, денег {self.money}.'
        return message

    def earn_money(self, money):
        self.money += money

    def make_deal(self, house):
        try:
            isinstance(house, House)
            if self.money >= house.cost:
                self.money = self.money - house.cost
                self.realty.append(house.info())
                return True
            else:
                return False
        except BaseException:
            exit('Incorrect House')

if __name__ == '__main__':
    salary = 1500
    house1 = House('Warsaw', 83, 90000)
    house2 = House('Praha', 50, 100000)
    townhouse = Townhouse('Minsk', 70000)
    house3 = 'Test'
    person = Person('Lenya', 32)
    text = ['Нужно больше золота....', 'Нужна другая работа....', 'Буду питаться только ролтоном :(',
            'Не хватает чуть чуть...']
    print(person.info())
    h = [house1, house2, townhouse, house3]
    while len(person.realty) <= 4:
        if person.make_deal(next((elem for elem in h))):
            print('Купил!!!!!')
            continue
        person.earn_money(salary)
        print(random.choice(text), f'У меня уже есть {person.money}')

print(person.info())
