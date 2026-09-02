def unique(lst):
    ans=[]
    for x in lst:
        if x not in ans:
            ans.append(x)
    return ans

lst=list(map(int,input("Enter numbers: ").split()))
print(unique(lst))
