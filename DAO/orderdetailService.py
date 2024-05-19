from Util.DBConn import DBConnection
from Exception.exceptions import IOException
from decimal import Decimal
import csv
class OrderDetailsService(DBConnection):
    def Update_quantity(self,orderid,quantity):
        self.cursor.execute("update OrderDetails set Quantity = ? where OrderID = ?",(quantity,orderid))
        self.conn.commit()
        # self.cursor.execute("""Update Orders
        #                        set TotalAmount = 
        self.cursor.execute("Select sum(Quantity * Price) as TotalAmount from OrderDetails inner join Products ON OrderDetails.ProductID = Products.ProductID WHERE OrderID = ?",
                            (orderid))
        totalamount = self.cursor.fetchone()[0]
        print(f"New Total Amount : {totalamount}")
        self.cursor.execute("update Orders set TotalAmount = ? where OrderID = ?",(totalamount,orderid))
        self.conn.commit()
        print("Updated Successfully")
    
    def add_discount(self,orderid,discount):
        self.cursor.execute("select TotalAmount from Orders where OrderID = ?", (orderid))
        current_total = self.cursor.fetchone()[0]
        current_total = float(current_total)
        discounted_total = current_total * (1 - discount / 100)
        discounted_total = Decimal(discounted_total)
        self.cursor.execute("update Orders set TotalAmount = ? where OrderID = ?", (discounted_total, orderid))
        self.cursor.commit()

        return discounted_total
    
    def generate_report(self):
        self.cursor.execute("""
                            Select c.CustomerID, c.FirstName, c.Email,p.ProductName, o.OrderID, o.OrderDate, o.TotalAmount, od.Quantity from Customers c join Orders o on c.CustomerID = o.CustomerID join 
                            OrderDetails od on o.OrderID = od.OrderID join Products 
                            p on od.ProductID = p.ProductID""")
        report = self.cursor.fetchall()
        headers = [column[0] for column in self.cursor.description]
        try: 
            with open("report.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(headers)
                writer.writerows(report)
            print("Report Generated as CSV file")
        except IOException as e:
            print(e)