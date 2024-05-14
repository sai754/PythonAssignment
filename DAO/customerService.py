class CustomerService:
    def __init__(self, customer):
        self.customer = customer
        self.__total_orders = 0

    def calculate_total_orders(self, orders):
        self.__total_orders = len(orders)

    def get_customer_details(self):
        print(f"Customer ID: {self.customer.customer_id}")
        print(f"Name: {self.customer.first_name} {self.customer.last_name}")
        print(f"Email: {self.customer.email}")
        print(f"Phone: {self.customer.phone}")
        print(f"Address: {self.customer.address}")

    def update_customer_info(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self.customer, key):
                setattr(self.customer, key, value)
