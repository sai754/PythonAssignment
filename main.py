from Entity import Customer, Inventory, Order, OrderDetails, Product, PaymentRecord
from DAO import CustomerService, InventoryService, OrderDetailsService, OrderService, ProductService
from Exception.exceptions import IncompleteOrderException
from datetime import datetime



def CustomerMenu():
    customer_service = CustomerService()
    while(True):
        print("""
Do you want to
1. Create Customer
2. View Customers
3. Update Customers
4. Go Back
              """)
        choice = int(input("Enter your choice: "))
        if choice == 1 :
             customer_service.get_all_customer()
             print("Create Customer next customer")
             customer_id = int(input("Enter Customer ID: "))
             first_name = input("Enter first name: ")
             last_name = input("Enter last name: ")
             email = input("Enter your email address ")
             allemails = customer_service.get_all_email()
             if email in allemails:
                 print("Email already exists")
             else:
                 phone = int(input("Enter Phone number: "))
                 address = input("Enter Address: ")
                 newCustomer = Customer(customer_id,first_name,last_name,email,phone,address)
                 customer_service.create_customer(newCustomer,customer_id)
        elif choice == 2:
            customer_service.get_all_customer()
        elif choice == 3:
            customer_service.get_all_customer()
            customer_id = int(input("Enter the customer id you want to update : "))
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            email = input("Enter your email address ")
            allemails = customer_service.get_all_email()
            if email in allemails:
                 print("Email already exists")
            else:
                 phone = int(input("Enter Phone number: "))
                 address = input("Enter Address: ")
                 newCustomer = Customer(customer_id,first_name,last_name,email,phone,address)
                 customer_service.update_customerDB(newCustomer,customer_id)
        else:
            break

def ProductsMenu():
    product_service = ProductService()
    while(True):
        print("""
Do you want to
1. Create Product
2. Update Product Info
3. Get Products Info
4. Check If the Product is in Stock
5. Go Back""")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            product_service.get_all_products()
            print("Enter Product Details")
            product_id = int(input("Enter the Product ID: "))
            product_name = input("Enter the Name of the Product: ")
            dedscription = input("Enter the Description: ")
            pricef = float(input("Enter the Price (with 2 decimal values): "))
            price = format(pricef,".2f")
            newProduct = Product(product_id,product_name,dedscription,price)
            product_service.create_product(newProduct)
        if choice == 2:
            product_service.get_all_products()
            product_id = int(input("Enter the Product ID you want to Update :"))
            product_name = input("Enter the Name of the Product: ")
            description = input("Enter the Description: ")
            pricef = float(input("Enter the Price (with 2 decimal values): "))
            price = format(pricef,".2f")
            newProduct = Product(product_id,product_name,description,price)
            product_service.update_product(newProduct,product_id)
        if choice == 3:
            product_service.get_all_products()
            product_id = int(input("Enter the Product ID: "))
            product = product_service.get_productById(product_id)
            if product:
                print(product)
            else:
                print(f"Product with this product id {product_id} not found")
        if choice == 4:
            product_service.get_all_products()
            product_id = int(input("Enter the Product ID: "))
            quantity = product_service.is_product_instock(product_id)
            if quantity:
                if quantity[0] > 0:
                    print(f"Product is Available in Stock , Available = {quantity[0]}")
                else:
                    print("It is out of stock")
            else:
                print("It is not available in inventory")
        else: 
            break
def OrdersMenu():
    order_service = OrderService()
    product_service = ProductService()
    customer_service = CustomerService()
    orderdetail_service = OrderDetailsService()
    while(True):
        print("""
Do you want to 
1. Create an Order
2. Calculate Total Amount of Order:
3. Get Order Details
4. Change the status of the order
5. Cancel Order
6. Change Quantity
7. Add Discount
8. Exit""" )
        choice = int(input("Enter the choice: "))
        if choice == 1:
            customer_id = int(input("Enter the Customer ID: "))
            customer = customer_service.get_customer_detailsDB(customer_id)
            print(customer)
            print("Available Products are: ")
            product_service.available_products()
            order_service.create_order(customer_id)
        elif choice == 2:
            order_service.get_All_Orders()
            orderid = int(input("Enter the Order ID to verify total amount: "))
            total_amount = order_service.calcuclate_total_amount(orderid)
            print(f"The total amount of the order : {total_amount[0]}")
        elif choice == 3:
            orderid = int(input("Enter the order id: "))
            order = order_service.get_order_by_orderid(orderid)
            if order:
                print(order)
            else:
                print(f"No Order found for the order id {orderid}")
        elif choice == 4:
            order_service.get_All_Orders()
            orderid = int(input("Enter the Order Id: "))
            status = input("Enter the New status of the Order: ")
            order_service.change_order_status(orderid,status)
        elif choice == 5:
            order_service.get_All_Orders()
            orderid = int(input("Enter the OrderID of Order you want to delete: "))
            order_service.cancel_order(orderid)
        elif choice == 6:
            order_service.get_All_Orders()
            orderid = int(input("Enter the Order ID: "))
            quantity = int(input("Enter the Updated Quantity: "))
            orderdetail_service.Update_quantity(orderid,quantity)
        elif choice == 7:
            order_service.get_All_Orders()
            orderid = int(input("Enter the OrderID: "))
            discount = int(input("Enter the discount percentage: "))
            newAmount = orderdetail_service.add_discount(orderid,discount)
            print(f"The new Total Amount is : {newAmount}")
        else:
            break

def InventoryMenu():
    inventory_service = InventoryService()
    while(True):
        print("""
Do you want to
1. Get Product with Inventory Id
2. Get the Quantity In Stock
3. Add Quantity to Inventory
4. Remove Quantity from Inventory
5. List Low Stock Products
6. List Out Of Stock Products
7. Go Back""")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            inventory_id = int(input("Enter the inventory id: "))
            inventory_service.get_product_by_invId(inventory_id)
        if choice == 2:
            inventory_id = int(input("Enter inventory id: "))
            inventory_service.get_quantity(inventory_id)
        if choice == 3:
            inventory_id = int(input("Enter inventory id: "))
            quantity = int(input("Enter the quantity you want to add: "))
            inventory_service.addTo_inventory(inventory_id,quantity)
        if choice == 4:
            inventory_id = int(input("Enter inventory id: "))
            quantity = int(input("Enter the quantity you want to remove: "))
            inventory_service.removeFrom_inventory(inventory_id,quantity)
        if choice == 5:
            threshold = int(input("Enter the threshold value: "))
            inventory_service.low_stock_items(threshold)
        if choice == 6:
            inventory_service.out_of_stock_items()
        else:
            break
def MainMenu():
    while(True):
        print("""
    1. Customer Menu
    2. Product Menu
    3. Orders Menu
    4. Inventory Menu
    5. Exit""")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            CustomerMenu()
        elif choice == 2:
            ProductsMenu()
        elif choice == 3:
            OrdersMenu()
        elif choice == 4:
            InventoryMenu()
        else:
            break


if __name__ == "__main__":
    MainMenu()










