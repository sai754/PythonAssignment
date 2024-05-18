from Util.DBConn import DBConnection
from datetime import date
class ProductService(DBConnection):
    def create_product(self,product):
        category = int(input("Enter the Category (1-5): "))
        self.cursor.execute("Insert into Products values (?,?,?,?,?)",
                            (product.product_id,product.product_name,product.description,product.price,
                             category))
        self.cursor.commit()
        quantity = int(input("Enter the Quantity: "))
        last_date_stock = date.today()
        inven_id = self.cursor.execute("Select top 1 InventoryID from Inventory Order by InventoryID desc").fetchone()[0] + 1
        self.cursor.execute("Insert into Inventory values (?,?,?,?)",
                            (inven_id, product.product_id,quantity,last_date_stock))
        self.conn.commit()
        print("Product Created Successfully")
    
    def get_all_products(self):
        self.cursor.execute("Select * from Products")
        for row in self.cursor:
            print(row)
    
    def update_product(self,product,productid):
        category = int(input("Enter the Category (1-5): "))
        self.cursor.execute("""
                            Update Products 
                            set ProductName = ?, Description = ?, Price = ?, Category = ?
                            where ProductID = ?""",
                            (product.product_name,product.description,product.price,
                             category,productid))
        self.cursor.commit()
        print("Updated Successfully")
    
    def get_productById(self,productid):
        self.cursor.execute("Select * from Products where ProductID = ?",productid)

        return self.cursor.fetchone()
    
    def is_product_instock(self,productid):
        self.cursor.execute("Select QuantityInStock from Inventory where ProductID = ?",(productid))
        product = self.cursor.fetchone()
        return product
    
    def available_products(self):
        self.cursor.execute("select * from Products join Inventory on Products.ProductID = Inventory.ProductID where QuantityInStock > 0")
        for row in self.cursor:
            print(row)
    

    
        
    