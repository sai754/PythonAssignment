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
    