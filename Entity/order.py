from Exception.exceptions import IncompleteOrderException
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
        if product is None:  # Check for missing product reference
            raise IncompleteOrderException()

        self.__order_items.append({'product': product, 'quantity': quantity})