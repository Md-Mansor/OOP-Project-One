from Food_Item import FoodItem
from Menu import Menu
from Users import Customer, Admin, Employee
from Restaurant import Restaurant
from Order import Order

mama_restaurant = Restaurant("mama ar  restaurant")


def customer_menu():
    name = input("Enter Your Name: ")
    phone = input("Enter Your Phone Number: ")
    email = input("Enter Your Email Address: ")
    address = input("Enter Your Address Number: ")
    customer = Customer(name=name, phone=phone, email=email, address=address)

    while True:
        print(f"Welcome {customer.name}")
        print("1 View Menu")
        print("2 Add Item To Cart")
        print("3 View Cart")
        print("4 Pay Bill")
        print("5 Exit")

        choice = int(input("Enter Your Choice: "))
        if choice == 1:
            customer.view_menu(mama_restaurant)
        elif choice == 2:
            item_name = input("Enter Item Name: ")
            item_quantity = int(input("Enter Item Quantity: "))
            customer.add_to_cart(mama_restaurant, item_name, item_quantity)
        elif choice == 3:
            customer.view_cart()
        elif choice == 4:
            customer.pay_bill()
        elif choice == 5:
            break
        else:
            print("Invalid Input")


def admin_menu():
    name = input("Enter Your Name: ")
    phone = input("Enter Your Phone Number: ")
    email = input("Enter Your Email Address: ")
    address = input("Enter Your Address: ")
    admin = Admin(name=name, phone=phone, email=email, address=address)

    while True:
        print(f"Welcome {admin.name}")
        print("1 Add New Item")
        print("2 Add New Employee")
        print("3 View Employee")
        print("4 View Items")
        print("5 Delete Item")
        print("6 Exit")

        admin_choice = int(input("Enter Your Choice: "))
        if admin_choice == 1:
            item_name = input("Enter Item Name: ")
            item_price = int(input("Enter Item Price: "))
            item_quantity = int(input("Enter Item Quantity: "))
            item = FoodItem(item_name, item_price, item_quantity)
            admin.add_new_item(mama_restaurant, item)
        elif admin_choice == 2:
            name = input("Enter Employee Name: ")
            phone = input("Enter Employee Phone Number: ")
            email = input("Enter Employee Email: ")
            address = input("Enter Employee Address: ")
            age = input("Enter Employee Age: ")
            designation = input("Enter Employee Designation: ")
            salary = input("Enter Employee Salary: ")
            employee = Employee(name, phone, email, address, age, designation, salary)
            admin.add_employee(mama_restaurant, employee)
        elif admin_choice == 3:
            admin.view_employee(mama_restaurant)
        elif admin_choice == 4:
            admin.view_menu(mama_restaurant)
        elif admin_choice == 5:
            item_name = input("Enter Item Name for Delete")
            admin.delete_item(mama_restaurant, item_name)
        elif admin_choice == 6:
            break
        else:
            print("Invalid Input")


while True:
    print("Welcome")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")
    operation = int(input("Enter Your Choice: "))
    if operation == 1:
        customer_menu()
    elif operation == 2:
        admin_menu()
    elif operation == 3:
        break
    else:
        print("Invalid Input")
