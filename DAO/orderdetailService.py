from decimal import Decimal
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
