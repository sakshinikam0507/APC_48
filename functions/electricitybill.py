def bill(units):
    if units<=100:
        ans=units*5
    elif units<=200:
        ans=100*5+(units-100)*7
    elif units<=300:
        ans=100*5+100*7+(units-200)*10
    else:
        ans=100*5+100*7+100*10+(units-300)*12
    return ans

units=float(input("Enter units consumed: "))
print("Electricity bill:",bill(units))
