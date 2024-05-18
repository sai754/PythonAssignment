from Util.DBConn import DBConnection
from decimal import Decimal
from datetime import date
class OrderService(DBConnection):
    def create_order(self,customerid):
        order_items = []
        while (True):
            product_id = int(input("Enter Product ID to add to the order (0 to finish): "))
            if product_id == 0:
                break
            quantity = int(input("Enter Quantity: "))
            self.cursor.execute("SELECT ProductID, Price FROM Products WHERE ProductID = ?", (product_id,))
            product = self.cursor.fetchone()
            if product:
                order_items.append({'product_id': product.ProductID, 'quantity': quantity, 'price': product.Price})
            else:
                print("Product not found!")
        total_amount = sum(item['quantity'] * item['price'] for item in order_items)
        orderid = self.cursor.execute("select top 1 OrderID from Orders order by OrderID desc ").fetchone()[0] + 1
        self.cursor.execute("INSERT INTO Orders VALUES (?,?, ?, ?,?)",
                           (orderid,customerid, date.today(), total_amount,"Pending"))
        self.conn.commit()
        for item in order_items:
                orderdetailid = self.cursor.execute("select top 1 OrderDetailID from OrderDetails order by OrderDetailID desc ").fetchone()[0] + 1
                self.cursor.execute("INSERT INTO OrderDetails VALUES (?, ?, ?,?)",
                               (orderdetailid, orderid, item['product_id'], item['quantity']))
        self.conn.commit()
        for item in order_items:
             oldquantity = self.cursor.execute("Select QuantityInStock from Inventory where ProductID = ?",item['product_id']).fetchone()[0]
             if oldquantity < item['quantity']:
                  print(f"This Product with product id {item['product_id']} Order cannot be placed because of insufficient stock!")
                  self.cursor.execute("Delete from OrderDetails where OrderID = ? and ProductID = ?",(orderid, item['product_id']))
                  self.conn.commit()
                  self.cursor.execute("Delete from Orders where OrderID = ?",orderid)
                  continue
             newQuantity = oldquantity - item["quantity"]
             self.cursor.execute("Update Inventory set QuantityInStock = ? where ProductID = ?",(newQuantity,item['product_id']))
             self.conn.commit()
        print("Order placed successfully!")
    
    def get_All_Orders(self):
         self.cursor.execute("Select * from Orders")
         for row in self.cursor:
              print(row)
    
    def calcuclate_total_amount(self,orderid):
         self.cursor.execute("""Select sum(Quantity * Price) as TotalAmount
                               from OrderDetails
                               inner join Products ON OrderDetails.ProductID = Products.ProductID
                               WHERE OrderID = ?""",(orderid))
         return self.cursor.fetchone()
    
    def get_order_by_orderid(self,orderid):
         self.cursor.execute("Select * from Orders where OrderID = ?",(orderid))
         order = self.cursor.fetchone()
         return order
    
    def change_order_status(self,orderid,status):
         self.cursor.execute("Update Orders set StatusOfOrder = ? where OrderID = ?",(status,orderid))
         self.conn.commit()
         print("Order Updated Successfully")

    def cancel_order(self,orderid):
         self.cursor.execute("delete from OrderDetails where OrderID = ?",(orderid))
         self.conn.commit()
         self.cursor.execute("delete from Orders where OrderID = ?",(orderid))
         self.conn.commit()
         print("Deleted Successfully")

