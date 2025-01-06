class Menu:
    def __init__(self):
        self.items = []

    def add_menu_item(self, menu_item):
        self.items.append(menu_item)

    def find_item(self, items_name):
        for menu_item in self.items:
            if menu_item.name.lower() == items_name.lower():
                return menu_item
        return None

    def remove_item(self, items_name):
        found_item = self.find_item(items_name)
        if found_item:
            self.items.remove(found_item)
            print("Item Deleted")
        else:
            print("Item not found")

    def show_menu(self):
        print("(*****Menu*****")
        print("Name\tPrice\tQuantity")
        for menu_item in self.items:
            print(f"{menu_item.name}\t{menu_item.price}\t{menu_item.quantity}")
