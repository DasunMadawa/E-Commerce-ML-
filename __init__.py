from customer import Customer
from product import Product

dilshan = Customer(name="Dilshan Rangaka" , address="Bandaragama" , contact="0770531515")
print(dilshan.get_details())

dilshan.set_name("Dilshan")
print(dilshan.get_details())

soap = Product(name="Detol", price=150.00 , quantity=10)
print(soap.get_details())

soap.update_price(250)
print(soap.get_details())

biscuit = Product(name="Maari", price=90.00 , quantity=15)
biscuit.update_price(250)
print(biscuit.get_details())
