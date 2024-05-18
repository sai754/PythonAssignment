from Util.DBConn import DBConnection
class CustomerService(DBConnection):
    # def __init__(self, customer):
    #     super().__init__()
    #     self.customer = customer
    #     self.__total_orders = 0

    # def calculate_total_orders(self, orders):
    #     self.__total_orders = len(orders)

    # def get_customer_details(self):
    #     print(f"Customer ID: {self.customer.customer_id}")
    #     print(f"Name: {self.customer.first_name} {self.customer.last_name}")
    #     print(f"Email: {self.customer.email}")
    #     print(f"Phone: {self.customer.phone}")
    #     print(f"Address: {self.customer.address}")

    # def update_customer_info(self, **kwargs):
    #     for key, value in kwargs.items():
    #         if hasattr(self.customer, key):
    #             setattr(self.customer, key, value)
    
    def calculate_total_ordersDB(self, customer):
        result = self.cursor.execute("Select count(*) from Orders where CustomerID = ?",(customer.customer_id()))
        total_orders = result[0][0] if result else 0
        return total_orders
    
    def get_customer_detailsDB(self,customer_id):
        self.cursor.execute("Select * from Customers where CustomerID = ?",(customer_id))
        result = self.cursor.fetchone()
        return result
    
    def update_customerDB(self,customer, customer_id):
        self.cursor.execute("""Update Customers
                            set FirstName = ?, LastName = ?, Email = ?, Phone = ?, Address = ?
                            where CustomerID = ?""",
                            (customer.first_name, customer.last_name,customer.email,customer.phone,customer.address,customer_id))
        self.conn.commit()
        print("Updated Successfully")
    
    def create_customer(self,customer,customerid):
        self.cursor.execute("Insert into Customers values (?,?,?,?,?,?)",
                            (customerid,customer.first_name,
                            customer.last_name,customer.email, customer.phone,customer.address))
        self.conn.commit()
        print("Customer Created Successfully")
    
    def get_all_customer(self):
        self.cursor.execute("Select * from Customers")
        for row in self.cursor:
            print(row)
    
    def get_all_email(self):
        self.cursor.execute("Select Email from Customers")
        return self.cursor.fetchall()
                            

