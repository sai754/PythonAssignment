from decimal import Decimal


class CustomerService:
    def __init__(self, customer):
        self.customer = customer
        self.__total_orders = 0

    def calculate_total_orders(self, orders):
        self.__total_orders = len(orders)

    def get_customer_details(self):
        print(f"Customer ID: {self.customer.customer_id}")
        print(f"Name: {self.customer.first_name} {self.customer.last_name}")
        print(f"Email: {self.customer.email}")
        print(f"Phone: {self.customer.phone}")
        print(f"Address: {self.customer.address}")
        print(f"Total Orders: {self.__total_orders}")

    def update_customer_info(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self.customer, key):
                setattr(self.customer, key, value)

class Product:
    def __init__(self, product_id, product_name, description, price):
        self.__product_id = product_id
        self.__product_name = product_name
        self.__description = description
        self.__price = price

    @property
    def product_id(self):
        return self.__product_id

    @property
    def product_name(self):
        return self.__product_name

    @product_name.setter
    def product_name(self, value):
        self.__product_name = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    def in_stock(self):
        return True 

class ProductService:
    def __init__(self, product):
        self.product = product

    def get_product_details(self):
        print(f"Product ID: {self.product.product_id}")
        print(f"Name: {self.product.product_name}")
        print(f"Description: {self.product.description}")
        print(f"Price: {self.product.price}")
        print(f"In Stock: {self.product.in_stock()}")

    def update_product_info(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self.product, key):
                setattr(self.product, key, value)

    def is_product_in_stock(self):
        return self.product.in_stock()
    
class Order:
    def __init__(self, order_id, customer, order_date=None):
        self.__order_id = order_id
        self.__customer = customer
        self.__order_date = order_date
        self.__order_items = []
        self.__status = 'pending'

    @property
    def order_id(self):
        return self.__order_id

    @order_id.setter
    def order_id(self, value):
        self.__order_id = value

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, value):
        self.__customer = value

    @property
    def order_date(self):
        return self.__order_date

    @order_date.setter
    def order_date(self, value):
        self.__order_date = value

    @property
    def order_items(self):
        return self.__order_items

    @order_items.setter
    def order_items(self, value):
        self.__order_items = value

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value

    def add_order_item(self, product, quantity):
        self.__order_items.append({'product': product, 'quantity': quantity})

class OrderService:
    def __init__(self,order):
        self.order = order
    def calculate_total_amount(self):
        total_amount = Decimal('0.00')
        for item in self.__order_items:
            product = item['product']
            quantity = item['quantity']
            price = product.price
            total_amount += price * quantity
        self.__total_amount = total_amount

    def get_order_details(self):
        print(f"Order ID: {self.order_id}")
        print(f"Customer: {self.customer.name}")
        print(f"Order Date: {self.order_date}")
        print(f"Status: {self.status}")
        print(f"Order Items:")
        for item in self.__order_items:
            product = item['product']
            quantity = item['quantity']
            print(f"{product.name} ({quantity} x {product.price}): {quantity * product.price}")

    def update_order_status(self, new_status):
        self.__status = new_status

    def cancel_order(self):
        for item in self.__order_items:
            product = item['product']
            quantity = item['quantity']
            product.in_stock -= quantity

class OrderDetails:
    def __init__(self, order_detail_id, order, product, quantity):
        self.__order_detail_id = order_detail_id
        self.__order = order
        self.__product = product
        self.__quantity = quantity
        self.__discount = Decimal('0.00')

    @property
    def order_detail_id(self):
        return self.__order_detail_id

    @order_detail_id.setter
    def order_detail_id(self, value):
        self.__order_detail_id = value

    @property
    def order(self):
        return self.__order

    @order.setter
    def order(self, value):
        self.__order = value

    @property
    def product(self):
        return self.__product

    @product.setter
    def product(self, value):
        self.__product = value

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        self.__quantity = value

    @property
    def discount(self):
        return self.__discount

    @discount.setter
    def discount(self, value):
        self.__discount = value

class OrderDetailsService:
    def __init__(self, order_detail):
        self.order_detail = order_detail
    def calculate_subtotal(self):
        subtotal = self.__product.price * self.__quantity
        return subtotal - (subtotal * (self.__discount / Decimal('100.00')))

    def get_order_detail_info(self):
        print(f"Order Detail ID: {self.order_detail_id}")
        print(f"Order ID: {self.order.order_id}")
        print(f"Product Name: {self.product.name}")
        print(f"Quantity: {self.quantity}")
        print(f"Price: {self.product.price}")
        print(f"Discount: {self.discount}%")
        print(f"Subtotal: {self.calculate_subtotal()}")

    def update_quantity(self, new_quantity):
        self.__quantity = new_quantity

    def add_discount(self, discount):
        self.__discount = discount

class Inventory:
    def __init__(self, inventory_id, product, quantity_in_stock, last_stock_update):
        self.__inventory_id = inventory_id
        self.__product = product
        self.__quantity_in_stock = quantity_in_stock
        self.__last_stock_update = last_stock_update

    @property
    def inventory_id(self):
        return self.__inventory_id

    @inventory_id.setter
    def inventory_id(self, value):
        self.__inventory_id = value

    @property
    def product(self):
        return self.__product

    @product.setter
    def product(self, value):
        self.__product = value

    @property
    def quantity_in_stock(self):
        return self.__quantity_in_stock

    @quantity_in_stock.setter
    def quantity_in_stock(self, value):
        self.__quantity_in_stock = value

    @property
    def last_stock_update(self):
        return self.__last_stock_update

    @last_stock_update.setter
    def last_stock_update(self, value):
        self.__last_stock_update = value
class InventoryService:
    def __init__(self, inventory):
        self.inventory = inventory

    def get_product(self):
        return self.product

    def get_quantity_in_stock(self):
        return self.quantity_in_stock

    def add_to_inventory(self, quantity):
        self.quantity_in_stock += quantity

    def remove_from_inventory(self, quantity):
        self.quantity_in_stock -= quantity

    def update_stock_quantity(self, new_quantity):
        self.quantity_in_stock = new_quantity

    def is_product_available(self, quantity_to_check):
        return self.quantity_in_stock >= quantity_to_check

    def get_inventory_value(self):
        return self.quantity_in_stock * self.product.price

    def list_low_stock_products(self, threshold):
        if self.quantity_in_stock < threshold:
            print(f"Product: {self.product.name}, Quantity: {self.quantity_in_stock}")

    def list_out_of_stock_products(self):
        if self.quantity_in_stock == 0:
            print(f"Product: {self.product.name}, Quantity: {self.quantity_in_stock}")

    def list_all_products(self):
        print(f"Product: {self.product.name}, Quantity: {self.quantity_in_stock}")

