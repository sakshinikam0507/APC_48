def avg(nums):
    return sum(nums)/len(nums)

nums=list(map(int,input("Enter numbers: ").split()))
print("Average:",avg(nums))
