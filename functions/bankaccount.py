bal=0
history=[]

def add(amt):
    global bal
    bal+=amt
    history.append("Deposited "+str(amt))

def withdraw(amt):
    global bal
    if amt<=bal:
        bal-=amt
        history.append("Withdrawn "+str(amt))
        print("Withdrawal successful")
    else:
        print("Insufficient balance")

def checkbal():
    print("Balance:",bal)

def showhistory():
    for x in history:
        print(x)

while True:
    print("1.Deposit")
    print("2.Withdrawal")
    print("3.Balance enquiry")
    print("4.Transaction history")
    print("5.Exit")
    ch=int(input("Enter choice: "))

    if ch==1:
        add(float(input("Enter amount: ")))
    elif ch==2:
        withdraw(float(input("Enter amount: ")))
    elif ch==3:
        checkbal()
    elif ch==4:
        showhistory()
    elif ch==5:
        break
