from abc import ABC
from statistics import quantiles


class User(ABC):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address


class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = Order()

    def view_menu(self, restaurant):
        restaurant.menu.show_menu()

    def add_to_cart(self, restaurant, items_name, quantity):
        cart_items = restaurant.menu.find_item(items_name)
        # print(cart_items.quantity)
        if cart_items:
            if quantity > cart_items.quantity:
                print("Not Enough Item Available")
            else:
                cart_items.quantity = quantity
                self.cart.add_item(cart_items)
                print("Item Added")
        else:
            print("Item Not Found")

    def view_cart(self):
        print("**View Cart**")
        print("Name\tPrice\tQuantity")
        for cart_item, quantity in self.cart.items.items():
            print(f"{cart_item.name}\t{cart_item.price}\t\t{quantity}")
        print(f"Total Price: {self.cart.total_price()}")


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


class Employee(User):
    def __init__(self, name, phone, email, address, age, designation, salary):
        super().__init__(name, phone, email, address)
        self.age = age
        self.designation = designation
        self.salary = salary


class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.employees = []

    def add_employee(self, restaurant, employee):
        restaurant.add_employee(employee)

    def view_employee(self, restaurant):
        restaurant.view_employee()

    def add_new_item(self, restaurant, menu_item):
        restaurant.menu.add_menu_item(menu_item)

    def delete_item(self, restaurant, item_name):
        restaurant.menu.remove_item(item_name)


class Restaurant:
    def __init__(self, name):
        self.name = name
        self.employees = []
        self.menu = Menu()

    def add_employee(self, employee):
        self.employees.append(employee)

    def view_employee(self):
        print("employee list")
        for emp in self.employees:
            print(emp.name, emp.phone, emp.email, emp.address)


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


class FoodItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = int(quantity)


mama_res = Restaurant("Mama Restaurant")

mn = Menu()
item = FoodItem("Pizza", 120, "20")
item2 = FoodItem("Burger", 100, "40")
admin = Admin("Me", "1234567777", "me@gmail.com", "Dhaka")
admin.add_new_item(mama_res, item)
admin.add_new_item(mama_res, item2)

customer1 = Customer("rahim", "123456", "rahim@gmail.com", "Dhaka")
customer1.view_menu(mama_res)
item_name = input("Enter Item Name: ")
item_quantity = int(input("Enter Item Quantity: "))
# customer1.add_to_cart(mama_res, item_name, int(item_quantity))
customer1.add_to_cart(mama_res, item_name, item_quantity)
customer1.view_cart()
