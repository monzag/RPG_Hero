from character import Character
from inventory import Inventory


class Hero:

    def __init__(self, first_name, last_name, race):
        self.character = Character(first_name, last_name, race)
        self.inventory = Inventory()
        self.experience = 0
        self.level = 1

    def get_items(self):
        return self.inventory.list_of_items

    def pick_an_item(self, item):
        self.inventory.add_item(item)

    def drop_item(self, item):
        self.inventory.drop_item(item)
