class Customer:
    def __init__(self , name, address, contact):
        self.name = name
        self.address = address
        self.contact = contact
    
    def set_name(self, name, address, contact):
        self.name = name
        
    def set_address(self, address):
        self.address = address
        
    def set_contact(self, contact):
        self.contact = contact
    
    def get_details(self):
        return f"Name: {self.name}\nAddress: {self.address}\nContact: {self.contact}"
    
    
# customer1 = Customer(name="Customer", address="Horana", contact="00000000000000")
# print(customer1.get_details())

