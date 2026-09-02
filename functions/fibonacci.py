def fib(n):
    ans=[]
    a=0
    b=1
    for i in range(n):
        ans.append(a)
        a,b=b,a+b
    return ans

n=int(input("Enter n: "))
print(fib(n))
