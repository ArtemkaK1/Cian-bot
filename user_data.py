from dataclasses import dataclass


@dataclass
class UserData:
    rooms: int = 0
    max_price: int = 0

    def set_rooms(self, num):
        self.rooms = num

    def set_max_price(self, price):
        self.max_price = price
