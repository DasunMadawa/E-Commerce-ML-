from customer import Customer
from product import Product
from order import Order

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

#========================================================================================================================================================================================================================
# print("----------- Customer Details --------------------")
# cus_name = input("Enter Customer Name: ")
# cus_address = input("Enter Customer Address: ")
# cus_contact = input("Enter Customer Contact: ")

# #Customer 2
# ##create
# new_customer = Customer(name=cus_name, address=cus_address, contact=cus_contact)
# print(new_customer.get_details())
# print("----------- Customer Created -----------------------------")
# print("----------------------------------------------------------")

# #Product 3
# print("----------- Product Details -----------------------------")
# prod_name = input("Enter Product Name: ")
# prod_quantity = int(input("Enter Product Quantity: "))
# prod_price = float(input("Enter Product Price: "))

# ## Create
# new_product = Product(name=prod_name, price=prod_price, quantity=prod_quantity)
# print(new_product.get_details())
# print("----------- Product Created -----------------------------")

# ##update product price

# new_product.update_price(new_price=float(input("Enter New Product Price: ")))
# print(new_product.get_details())

# print("----------- Product Updated -----------------------------")

## Create order
order1 = Order(customer=dilshan, order_id='OD001')
order1.add_product(soap)
order1.add_product(biscuit)

total  = order1.calculate_total()
print(f'Order Total is: {total}')

print(order1.generate_summary())