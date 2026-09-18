class Customer:
    def __init__(self,customer_id,name):
        self.customer_id=customer_id
        self.name=name
class Product:
    def __init__(self,product_id,product_name,price,stock):
        if price<0:
            raise ValueError("Price cannot be negative")
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
        self.stock-=quantity
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
    def __init__(self,order_id,item):
        self.order_id=order_id
        self.item=item
    def calculate_total(self):
        return self.item.calculate_amount()
    def complete_order(self):
        self.item.product.reduce_stock(self.item.quantity)
        print("Order completed")
        print("Total Amount:",self.calculate_total())
        print("Remaining Stock:",self.item.product.stock)
try:
    product=Product("P101","Laptop",50000,10)
    item=OrderItem(product,2)
    my_order=Order("O101",item)
    my_order.complete_order()
except ValueError as error:
    print("Error:",error)
