class Inventory:
    inventories = []
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
    
    @classmethod
    def add_inventory(cls, inventory_id, product, quantity_in_stock, last_stock_update):
        inventory = cls(inventory_id, product, quantity_in_stock, last_stock_update)
        cls.inventories.append(inventory)
        print(f"Product with ID {inventory_id} added to inventory.")

    @classmethod
    def remove_inventory(cls, inventory_id):
        for i, inv in enumerate(cls.inventories):
            if inv.inventory_id == inventory_id:
                cls.inventories.remove(inv)
                print(f"Product with ID {inventory_id} removed from inventory.")
                return
        print(f"Product with ID {inventory_id} not found in inventory.")

    @classmethod
    def update_stock_quantity(cls, inventory_id, new_quantity):
        for inv in cls.inventories:
            if inv.inventory_id == inventory_id:
                inv.quantity_in_stock = new_quantity
                print(f"Stock quantity for product with ID {inventory_id} updated to {new_quantity}.")
                return
        print(f"Product with ID {inventory_id} not found in inventory.")

    @classmethod
    def get_inventory_info(cls):
        print("Inventory Information:")
        for inv in cls.inventories:
            print(f"Product ID: {inv.inventory_id}, Quantity in Stock: {inv.quantity_in_stock}, Last Stock Update: {inv.last_stock_update}")
