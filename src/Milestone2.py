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
my_product=Product("P101","Laptop",60000,10)
print(my_product.product_id)
print(my_product.product_name)
print(my_product.price)
print(my_product.stock)