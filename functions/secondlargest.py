def second(nums):
    vals=[]
    for x in nums:
        if x not in vals:
            vals.append(x)
    vals.sort()
    return vals[-2]

nums=list(map(int,input("Enter numbers: ").split()))
print("Second largest:",second(nums))
