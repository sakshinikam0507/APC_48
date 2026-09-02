def stats(nums):
    small=min(nums)
    large=max(nums)
    tot=sum(nums)
    avg=tot/len(nums)
    return small,large,tot,avg

nums=list(map(int,input("Enter numbers: ").split()))
small,large,tot,avg=stats(nums)
print("Minimum:",small)
print("Maximum:",large)
print("Sum:",tot)
print("Average:",avg)
