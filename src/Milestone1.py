class Customer:
    def __init__(self,customerID,name,customer_type):
        self.customerID=customerID
        self.name=name
        self.customer_type=customer_type
    def display_details(self):
        print("Customer ID:",self.customerID)
        print("Customer Name:",self.name)
        print("Customer Type:",self.customer_type)
my_customer=Customer("c101","pavani","regular")
my_customer.display_details()