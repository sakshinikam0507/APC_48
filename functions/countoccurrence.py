def count(lst,x):
    c=0
    for item in lst:
        if item==x:
            c+=1
    return c

lst=list(map(int,input("Enter numbers: ").split()))
x=int(input("Enter element: "))
print("Occurrences:",count(lst,x))
