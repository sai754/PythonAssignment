from Exception.exceptions import IncompleteOrderException
from datetime import datetime
class Order:
    orders = [] # Order List
    def __init__(self, order_id, customer,total_amount=0 ,order_date=None):
        self.__order_id = order_id
        self.__customer = customer
        self.__order_date = order_date
        self.__order_items = []
        self.__status = 'pending'
        self.__total_amount = total_amount
        Order.orders.append(self)

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
        if product is None:  # Check for missing product reference
            raise IncompleteOrderException()

        self.__order_items.append({'product': product, 'quantity': quantity})

    @classmethod
    def add_order(cls, order_id, customer, total_amount=0,order_date=None):
        order = cls(order_id, customer, total_amount,order_date)
        cls.orders.append(order)
        print("Order added successfully.")

    @classmethod
    def update_order_status(cls, order_id, new_status):
        order = cls._find_order_by_id(order_id)
        if order:
            order.status = new_status
            print("Order status updated successfully.")
        else:
            raise ValueError("Order not found.")

    @classmethod
    def cancel_order(cls, order_id):
        order = cls._find_order_by_id(order_id)
        if order:
            cls.orders.remove(order)
            print("Order canceled successfully.")
        else:
            raise ValueError("Order not found.")

    @staticmethod
    def _find_order_by_id(order_id):
        for order in Order.orders:
            if order.order_id == order_id:
                return order
        return None
    
    @classmethod
    def sort_orders_by_date(cls, ascending=True):
        orders_with_dates = [order for order in cls.orders if order.order_date is not None]
        sorted_orders = sorted(orders_with_dates, key=lambda x: x.order_date, reverse=not ascending)
        cls.orders.clear()
        cls.orders.extend(sorted_orders)

    def record_payment(self, amount):
        self.__total_amount += amount  # Update total amount paid
        payment_record = PaymentRecord(self.order_id, amount)
        print(f"Payment recorded for order {self.order_id} successfully.")
        return payment_record
    
class PaymentRecord:
    payment_records = []

    def __init__(self, order_id, amount, payment_date=None, status="Pending"):
        self.order_id = order_id
        self.amount = amount
        self.status = status
        self.payment_date = payment_date if payment_date else datetime.now()
        PaymentRecord.payment_records.append(self)