from Exception.exceptions import InsufficientStockException
class InventoryService:
    def __init__(self, inventory):
        self.inventory = inventory

    def get_product(self):
        return self.inventory.product

    def get_quantity_in_stock(self):
        return self.inventory.quantity_in_stock

    def add_to_inventory(self, quantity):
        self.inventory.quantity_in_stock += quantity

    def remove_from_inventory(self, quantity):
        if quantity > self.inventory.quantity_in_stock:
            raise InsufficientStockException("Insufficient Stock Available")
        self.inventory.quantity_in_stock -= quantity

    def update_stock_quantity(self, new_quantity):
        self.inventory.quantity_in_stock = new_quantity

    def is_product_available(self, quantity_to_check):
        return self.inventory.quantity_in_stock >= quantity_to_check

    def get_inventory_value(self):
        return self.inventory.quantity_in_stock * self.inventory.product.price

    def list_low_stock_products(self, threshold):
        if self.inventory.quantity_in_stock < threshold:
            print(f"Product: {self.inventory.product.name}, Quantity: {self.inventory.quantity_in_stock}")

    def list_out_of_stock_products(self):
        if self.inventory.quantity_in_stock == 0:
            print(f"Product: {self.inventory.product.name}, Quantity: {self.inventory.quantity_in_stock}")

    def list_all_products(self):
        print(f"Product: {self.inventory.product.name}, Quantity: {self.inventory.quantity_in_stock}")
