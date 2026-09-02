items={}

def add(name,price,qty):
    items[name]=[price,qty]

def remove(name):
    if name in items:
        del items[name]

def sub():
    return sum(price*qty for price,qty in items.values())

def disc(amt,coupon):
    if coupon=="SAVE10":
        return amt*0.10
    return 0

def tax(amt):
    return amt*0.18

def makebill(coupon):
    s=sub()
    d=disc(s,coupon)
    t=tax(s-d)
    return s,d,t,s-d+t

n=int(input("Enter number of products: "))
for i in range(n):
    name=input("Enter product name: ")
    price=float(input("Enter price: "))
    qty=int(input("Enter quantity: "))
    add(name,price,qty)

coupon=input("Enter coupon: ")
s,d,t,tot=makebill(coupon)
print("Subtotal:",s)
print("Discount:",d)
print("GST:",t)
print("Final invoice:",tot)
