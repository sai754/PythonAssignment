from Entity import Customer, Inventory, Order, OrderDetails, Product, PaymentRecord
from DAO import CustomerService, InventoryService, OrderDetailsService, OrderService, ProductService
from Exception.exceptions import IncompleteOrderException
from datetime import datetime

if __name__ == "__main__":
    # Customer class and Customer Service
    customer1 = Customer(1, "Sai", "Subash", "sai@example.com", "1234567890", "Ambattur")

    # Create a CustomerService object
    customer_service = CustomerService(customer1)

    # Get customer details
    print("Customer Details Before Update :")
    customer_service.get_customer_details()

    # Update customer info
    customer_service.update_customer_info(first_name="SAII", phone="9876543210")

    # Get updated customer details
    print("Customer Details After Update:")
    customer_service.get_customer_details()

    order = Order("001", customer1)
    order_service = OrderService(order)

    try:
        order_detail = OrderDetails(1, order,None, 5)  # Attempt to create an order detail with a missing product reference
    except IncompleteOrderException as e:
        print("IncompleteOrderException:", e)

    inventory = Inventory(1, "Laptop", 10, "2024-05-15")
    inventory_service = InventoryService(inventory)

    try:
        inventory_service.remove_from_inventory(15)  # Attempting to remove more stock than available
    except Exception as e:
        print(e)

    # Task 6
    # Products List
    Product.add_product(1, "Laptop", "High-performance laptop", 1000)
    Product.add_product(2, "Headphones", "Wireless headphones", 50)

    # Update product
    Product.update_product(1, new_name="Gaming Laptop")
    Product.view_all_products()
    # Remove product
    try:
        Product.remove_product(2)
    except ValueError as e:
        print(e)

    # Try to remove product with existing orders
    try:
        Product.remove_product(1)
    except ValueError as e:
        print(e)
    
    # Orders List
    order_1 = Order.add_order(1, "Sai")
    order_2 = Order.add_order(2, "John")

    # Update order status
    Order.update_order_status(1, "shipped")

    # Cancel order
    Order.cancel_order(2)

    # Sorted Lists

    Order.add_order(1, "Sai", datetime(2024, 5, 1))
    Order.add_order(2, "John", None)
    Order.add_order(3, "Alice", datetime(2024, 5, 2))

    # Sort orders by date in ascending order
    asc = True
    Order.sort_orders_by_date(asc)
    print("Sorted orders by date:")
    for order in Order.orders:
        print(f"Order ID: {order.order_id}, Date: {order.order_date}")

    
    # Inventory List
    
    Inventory.add_inventory(1, "Product A", 100, "2024-05-01")
    Inventory.add_inventory(3, "Product C", 50, "2024-05-02")
    Inventory.add_inventory(2, "Product B", 75, "2024-05-03")

    # Get inventory information
    Inventory.get_inventory_info()

    # Update stock quantity
    Inventory.update_stock_quantity(1, 120)

    # Remove a product from inventory
    Inventory.remove_inventory(3)

    # Get updated inventory information
    Inventory.get_inventory_info()

    # Product Search and Retrieval

    product1 = Product(1, "Laptop", "Electronics", 1200)
    product2 = Product(2, "Phone", "Electronics", 800)
    product3 = Product(3, "T-shirt", "Apparel", 20)
    product4 = Product(4, "Shoes", "Apparel", 50)

    # Search products by name
    try:
        laptop_products = Product.search_by_name("Laptop")
        print("Products with 'laptop' in the name:")
        for product in laptop_products:
            print(f"Product ID: {product.product_id}, Name: {product.product_name}")
    except ValueError as e:
        print(e)

    # Search Prodcts by price
    try:
        affordable_products = Product.search_by_price_range(0, 100)
        print("\nProducts within the price range 0 - 100:")
        for product in affordable_products:
            print(f"Product ID: {product.product_id}, Name: {product.product_name}, Price: ${product.price}")
    except ValueError as e:
        print(e)

    # Check Duplicate Products
    # Implemented find_by_id and check_duplicates
    product1 = Product.add_product(9, "ABC", "Electronics", 1200)
    product2 = Product.add_product(8, "EFG", "Electronics", 800)

    # Record Payments

    order1 = Order(101, "John Doe", 0)  # Initialize total_amount_paid to 0
    order2 = Order(102, "Jane Smith", 0)

    # Recording payments for orders
    order1.record_payment(1200)
    order2.record_payment(1600)

    # Display payment records
    print("\nPayment Records:")
    for payment in PaymentRecord.payment_records:
        print(f"Order ID: {payment.order_id}, Amount: {payment.amount}, Status: {payment.status}, Payment Date: {payment.payment_date}")












