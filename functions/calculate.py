def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def calc(fun,a,b):
    return fun(a,b)

a=float(input("Enter first number: "))
b=float(input("Enter second number: "))

print("Addition:",calc(add,a,b))
print("Subtraction:",calc(sub,a,b))
print("Multiplication:",calc(mul,a,b))
print("Division:",calc(div,a,b))
