class FoodOrder:
    def __init__(self,i,n,f,q,p):
        self.i=i
        self.n=n
        self.f=f
        self.q=q
        self.p=p
    def bill(self):
        total=self.q*self.p
        return total+total*0.05
    def __del__(self):
        print("Order completed")
o=FoodOrder(1,"Amit","Pizza",2,200)
print("Total bill:",o.bill())
del o