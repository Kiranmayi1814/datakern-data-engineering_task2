class Customer:
    def __init__(self,customer_id,name):
        self.customer_id=customer_id
        self.name=name
class Product:
    def __init__(self,product_id,product_name,price,stock):
        if price<=0:
            raise ValueError("Price must be greater than zero")
        if stock<0:
            raise ValueError("Stock cannot be negative")
        self.product_id=product_id
        self.product_name=product_name
        self.price=price
        self.stock=stock
    def reduce_stock(self,quantity):
        if quantity<=0:
            raise ValueError("Quantity must be greater than zero")
        if quantity>self.stock:
            raise ValueError("Not enough stock")
        self.stock=self.stock-quantity
class OrderItem:
    def __init__(self,product,quantity):
        if quantity<=0:
            raise ValueError("Quantity must be greater than zero")
        if quantity>product.stock:
            raise ValueError("Not enough stock")
        self.product=product
        self.quantity=quantity
    def calculate_amount(self):
        return self.product.price*self.quantity
class Order:
    def __init__(self,order_id,customer,item):
        self.order_id=order_id
        self.customer=customer
        self.item=item
    def place_order(self):
        self.item.product.reduce_stock(self.item.quantity)
        print("Order placed successfully")
    def calculate_total(self):
        return self.item.calculate_amount()
    def display_order(self):
        print("Order ID:",self.order_id)
        print("Customer:",self.customer.name)
        print("Product:",self.item.product.product_name)
        print("Quantity:",self.item.quantity)
        print("Total Amount:",self.calculate_total())
        print("Remaining Stock:",self.item.product.stock)
try:
    customer=Customer("C101","Pavani")
    product=Product("P101","Laptop",50000,10)
    item=OrderItem(product,2)
    my_order=Order("O101",customer,item)
    my_order.place_order()
    my_order.display_order()
except ValueError as error:
    print("Error:",error)
