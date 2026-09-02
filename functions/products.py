items=[]
n=int(input("Enter number of products: "))

for i in range(n):
    name=input("Enter product name: ")
    price=float(input("Enter price: "))
    qty=int(input("Enter quantity: "))
    items.append({"name":name,"price":price,"quantity":qty})

items=list(map(lambda x:{**x,"total":x["price"]*x["quantity"]},items))
costly=list(filter(lambda x:x["price"]>1000,items))
items=sorted(items,key=lambda x:x["total"])

print("Product values:",items)
print("Products costing more than 1000:",costly)
print("Sorted products:",items)
