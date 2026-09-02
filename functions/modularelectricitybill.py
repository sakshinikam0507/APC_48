def slab(units):
    if units<=100:
        return units*5
    elif units<=200:
        return 100*5+(units-100)*7
    elif units<=300:
        return 100*5+100*7+(units-200)*10
    else:
        return 100*5+100*7+100*10+(units-300)*12

def bill(units):
    fixed=100
    charge=slab(units)
    tax=(charge+fixed)*0.05
    disc=(charge+fixed)*0.10 if units<100 else 0
    return charge+fixed+tax-disc

units=float(input("Enter units consumed: "))
print("Final bill:",bill(units))
