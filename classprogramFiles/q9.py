class ATM:
    def __init__(self,n,b):
        self.n=n
        self.b=b
    def check(self):
        print("Balance:",self.b)
    def deposit(self,x):
        self.b+=x
    def withdraw(self,x):
        if x<=self.b:
            self.b-=x
        else:
            print("Insufficient balance")
    def details(self):
        print("Account:",self.n)
        print("Balance:",self.b)
a=ATM("12345",5000)
while True:
    print("1.Check 2.Deposit 3.Withdraw 4.Details 5.Exit")
    ch=int(input("Enter choice: "))
    if ch==1:
        a.check()
    elif ch==2:
        a.deposit(float(input("Enter amount: ")))
    elif ch==3:
        a.withdraw(float(input("Enter amount: ")))
    elif ch==4:
        a.details()
    elif ch==5:
        break