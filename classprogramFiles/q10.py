class Vehicle:
    def __init__(self,no,model,rate):
        self.no=no
        self.model=model
        self.rate=rate
        self.avail=True
    def rent(self):
        if self.avail:
            self.avail=False
            print("Vehicle rented")
        else:
            print("Not available")
    def ret(self):
        self.avail=True
        print("Vehicle returned")
    def charge(self,days):
        return self.rate*days
v=Vehicle("MH09AB1234","Honda",1000)
v.rent()
print("Charge:",v.charge(3))
v.ret()