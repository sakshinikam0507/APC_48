cart = []
cart.append("Milk")
cart.append("Bread")
cart.append("Apples")
cart.remove("Bread")
item = input("Enter item to search: ")
if item in cart:
    print("Item is in the cart")
else:
    print("Item is not in the cart")
print("Cart:", cart)
print("Total items:", len(cart))
