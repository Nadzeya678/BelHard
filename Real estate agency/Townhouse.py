import House


class Townhouse(House):
    def __init__(self, address, cost, area=60):
        super(House).__init__(address, cost, area)
