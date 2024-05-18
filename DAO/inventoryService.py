from Util.DBConn import DBConnection
from Exception.exceptions import InsufficientStockException
class InventoryService(DBConnection):
    def get_product_by_invId(self,inventoryId):
        self.cursor.execute("Select * from Products join Inventory on Products.ProductID = Inventory.ProductID where InventoryID = ?",inventoryId)
        product = self.cursor.fetchone()
        if product:
            print(product)
        else:
            print(f"No Product with the Inventory ID {inventoryId}")
    def get_quantity(self,inventoryid):
        self.cursor.execute("Select QuantityInStock from Inventory where InventoryID = ?",(inventoryid))
        product = self.cursor.fetchone()
        if product:
            print(product[0])
        else:
            print(f"No Product with the Inventory ID {inventoryid}")
    
    def addTo_inventory(self,invenID,quantity):
        self.cursor.execute("select QuantityInStock from Inventory where InventoryID = ?",(invenID))
        old_quantity = self.cursor.fetchone()[0]
        new_quantity = old_quantity + quantity
        self.cursor.execute("update Inventory set QuantityInStock = ? where InventoryID = ?",(new_quantity,invenID))
        self.conn.commit()
        print("Updated Successfully")

    def removeFrom_inventory(self,invenID,quantity):
        self.cursor.execute("select QuantityInStock from Inventory where InventoryID = ?",(invenID))
        old_quantity = self.cursor.fetchone()[0]
        if old_quantity > quantity:
            new_quantity = old_quantity - quantity
            self.cursor.execute("update Inventory set QuantityInStock = ? where InventoryID = ?",(new_quantity,invenID))
            self.conn.commit()
            print("Updated Successfully")
        else:
            raise InsufficientStockException("Not enough stock available")
    
    def low_stock_items(self,threshold):
        self.cursor.execute("select * from Products join Inventory on Products.ProductID = Inventory.ProductID where Inventory.QuantityInStock < ?",(threshold))
        for row in self.cursor:
            print(row)
    
    def out_of_stock_items(self):
        self.cursor.execute("select * from Products join Inventory on Products.ProductID = Inventory.ProductID where Inventory.QuantityInStock = 0")
        for row in self.cursor:
            print(row)
