from customer import Customer
from product import Product

#Customer 1
## Create
dilshan = Customer(name="Dilshan Rangaka" , address="Bandaragama" , contact="0770531515")
print(dilshan.get_details())

## Update
dilshan.set_name("Dilshan")
print(dilshan.get_details())

#product 1
## Create
soap = Product(name="Detol", price=150.00 , quantity=10)
print(soap.get_details())

## update
soap.update_price(250)
print(soap.get_details())


#product 2
## Create
biscuit = Product(name="Maari", price=90.00 , quantity=15)
print(biscuit.get_details())

## Update
biscuit.update_price(200)
print(biscuit.get_details())