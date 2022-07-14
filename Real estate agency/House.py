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