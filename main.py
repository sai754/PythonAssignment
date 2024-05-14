from Entity import Customer, Inventory, Order, OrderDetails, Product
from DAO import CustomerService, InventoryService, OrderDetailsService, OrderService, ProductService
from Exception.exceptions import IncompleteOrderException


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
    
    











