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

