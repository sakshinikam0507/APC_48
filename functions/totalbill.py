def total(prices,qty):
    tot=0
    for price,q in zip(prices,qty):
        tot+=price*q
    if tot>=5000:
        disc=tot*0.20
    elif tot>=2000:
        disc=tot*0.10
    else:
        disc=0
    return tot-disc

prices=list(map(float,input("Enter prices: ").split()))
qty=list(map(int,input("Enter quantities: ").split()))
print("Total bill:",total(prices,qty))
