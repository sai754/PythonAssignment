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