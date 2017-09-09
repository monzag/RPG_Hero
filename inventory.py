class Inventory:

    def __init__(self, capacity=10, max_weight=15):
        self.capacity = capacity
        self.max_weight = max_weight
        self.list_of_items = []

    def add_item(self, item):
        if self.get_inventory_size() < self.capacity and (self.get_inventory_weight() + item.weight) < self.max_weight:
            self.list_of_items.append(item)
        else:
            print('Too many items or too heavy!')

    def drop_item(self, item):
        if item in self.list_of_items:
            self.list_of_items.remove(item)

    def get_inventory_size(self):
        size = 0
        for item in self.list_of_items:
            size += 1

        return size

    def get_inventory_weight(self):
        weight = 0
        for item in self.list_of_items:
            weight += item.weight

        return weight

    def get_the_heaviest_item(self):
        max_weight = 0
        heaviest_item = ''

        for item in self.list_of_items:
            if item.weight > max_weight:
                max_weight = item.weight
                heaviest_item = item

        return heaviest_item

