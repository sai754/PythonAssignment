from decimal import Decimal
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
