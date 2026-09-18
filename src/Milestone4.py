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
    def get_discount(self):
        return 6
class PremiumCustomer(Customer):
    def get_discount(self):
        return 7
class CorporateCustomer(Customer):
    def get_discount(self):
        return 5
my_regularCustomer=RegularCustomer("c101","pavani","regular")
my_premiumCustomer=PremiumCustomer("c102","Durga","premium")
my_corporateCustomer=CorporateCustomer("c103","Kiranmayi","corporate")
my_regularCustomer.display_details()
print("Regular Discount:", my_regularCustomer.get_discount(), "%")
print()
my_premiumCustomer.display_details()
print("Premium Discount:", my_premiumCustomer.get_discount(), "%")
print()
my_corporateCustomer.display_details()
print("Corporate Discount:", my_corporateCustomer.get_discount(), "%")