class Customer:
    def __init__(self,customerID,name,customer_type):
        self.customerID=customerID
        self.name=name
        self.customer_type=customer_type
    def display_details(self):
        print("Customer ID:",self.customerID)
        print("Customer Name:",self.name)
        print("Customer Type:",self.customer_type)
class RegularCustomer(Customer):
    pass
class PremiumCustomer(Customer):
    pass
class CorporateCustomer(Customer):
    pass
my_regularCustomer=RegularCustomer("c101","pavani","regular")
my_premiumCustomer=PremiumCustomer("c102","Durga","premium")
my_corporateCustomer=CorporateCustomer("c103","Kiranmayi","corporate")
my_regularCustomer.display_details()
my_premiumCustomer.display_details()
my_corporateCustomer.display_details()

