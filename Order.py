class Order:
    def __init__(self) -> None:
        self.items = {}

    def add_item(self, order_item):
        if order_item in self.items:
            self.items[order_item] += order_item.quantity
        else:
            self.items[order_item] = order_item.quantity

    def remove(self, remove_one):
        if remove_one in self.items:
            del self.items[remove_one]

    def total_price(self):
        return sum(item_price.price * quantity for item_price, quantity in self.items.items())

    def clear(self):
        self.items = {}
