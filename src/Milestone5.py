class Customer:
    def __init__(self, customer_id, name):
        self.customer_id=customer_id
        self.name=name
class Product:
    def __init__(self, product_id, product_name, price):
        self.product_id=product_id
        self.product_name=product_name
        self.price=price
class OrderItem:
    def __init__(self, product, quantity):
        self.product=product
        self.quantity=quantity
    def display_item(self):
        print("Product:", self.product.product_name)
        print("Quantity:", self.quantity)
        print("Price:", self.product.price)
class Order:
    def __init__(self, order_id, customer, item):
        self.order_id=order_id
        self.customer=customer
        self.item=item
    def display_order(self):
        print("Order ID:", self.order_id)
        print("Customer:", self.customer.name)
        self.item.display_item()
customer=Customer("C101", "Pavani")
product=Product("P101", "Laptop", 50000)
item=OrderItem(product, 2)
my_order=Order("O101", customer, item)
my_order.display_order()