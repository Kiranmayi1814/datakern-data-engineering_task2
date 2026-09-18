class Customer:
    def __init__(self,customer_id,name,customer_type,discount):
        self.customer_id=customer_id
        self.name=name
        self.customer_type=customer_type
        self.discount=discount
class Product:
    def __init__(self,name,price,stock):
        self.name=name
        self.price=price
        self.stock=stock
class Order:
    def __init__(self,customer,product,quantity):
        self.customer=customer
        self.product=product
        self.quantity=quantity
    def total(self):
        return self.product.price*self.quantity*(1-self.customer.discount/100)
def main():
    print("Retail Order Management")
    customer_id=input("Enter Customer ID: ")
    name=input("Enter Customer Name: ")
    print("1.Regular 2.Premium 3.Corporate")
    choice=input("Select Customer Type: ")
    customers={
        "1":Customer(customer_id,name,"Regular",6),
        "2":Customer(customer_id,name,"Premium",7),
        "3":Customer(customer_id,name,"Corporate",5)
    }
    if choice not in customers:
        print("Invalid customer type")
        return
    customer=customers[choice]
    product=Product("Laptop",50000,10)
    try:
        quantity=int(input("Quantity: "))
        if quantity<=0 or quantity>product.stock:
            raise ValueError("Invalid quantity or stock")
        order=Order(customer,product,quantity)
        print("Customer ID:",order.customer.customer_id)
        print("Customer Name:",order.customer.name)
        print("Customer Type:",order.customer.customer_type)
        print("Product:",order.product.name)
        print("Quantity:",order.quantity)
        print("Total:",order.total())
        product.stock-=quantity
        print("Order completed")
        print("Remaining Stock:",product.stock)
    except ValueError as error:
        print("Error:",error)
if __name__=="__main__":
    main()