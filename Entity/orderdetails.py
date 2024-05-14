from decimal import Decimal
from Exception.exceptions import  IncompleteOrderException
class OrderDetails:
    def __init__(self, order_detail_id, order, product, quantity):
        self.__order_detail_id = order_detail_id
        self.__order = order
        if product is None:
            raise IncompleteOrderException()
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
