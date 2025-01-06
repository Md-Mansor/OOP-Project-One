from abc import ABC
from statistics import quantiles
from Order import Order


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
        print(f"Total Price: {self.cart.total_price}")

    # def pay_bill(self):
    #     print(f"Total {self.cart.total_price()} Paid Successfully ")
    #     self.cart.clear()

    def pay_bill(self):
        print(f"Total {self.cart.total_price} Paid Successfully")
        self.cart.clear()


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

    def view_menu(self, restaurant):
        restaurant.menu.show_menu()
