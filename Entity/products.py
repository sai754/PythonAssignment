class Product:
    products = [] # Task 6 Managing Product list
    def __init__(self, product_id, product_name, description, price):
        self.__product_id = product_id
        self.__product_name = product_name
        self.__description = description
        self.__price = price
        Product.products.append(self)

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
    
    @classmethod
    def add_product(cls, product_id, product_name, description, price):
        if cls._find_product_by_id(product_id):
            raise ValueError("Product with the same ID already exists.")
        cls._check_duplicate(product_name)
        product = cls(product_id, product_name, description, price)
        cls.products.append(product)
        print("Product added successfully.")

    @classmethod
    def update_product(cls, product_id, new_name=None, new_description=None, new_price=None):
        product = cls._find_product_by_id(product_id)
        if product:
            if new_name is not None:
                product.product_name = new_name
            if new_description is not None:
                product.description = new_description
            if new_price is not None:
                product.price = new_price
            print("Product updated successfully.")
        else:
            raise ValueError("Product not found.")

    @classmethod
    def remove_product(cls, product_id):
        product = cls._find_product_by_id(product_id)
        if product:
            cls.products.remove(product)
            print("Product removed successfully.")
        else:
            raise ValueError("Product not found.")

    @staticmethod
    def _find_product_by_id(product_id):
        for product in Product.products:
            if product.product_id == product_id:
                return product
        return None
    
    @classmethod
    def view_all_products(cls):
        for product in cls.products:
            print(product.product_id, product.product_name,product.description)

    @classmethod
    def search_by_name(cls, name):
        results = [product for product in cls.products if name.lower() in product.product_name.lower()]
        return results

    @classmethod
    def search_by_price_range(cls, min_price, max_price):
        results = [product for product in cls.products if min_price <= product.price <= max_price]
        return results

    @classmethod
    def _check_duplicate(cls, product_name):
        for product in cls.products:
            if product.product_name == product_name:
                raise ValueError(f"Product with name '{product_name}' already exists.")
