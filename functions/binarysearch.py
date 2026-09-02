def search(nums,x,left,right):
    if left>right:
        return -1
    mid=(left+right)//2
    if nums[mid]==x:
        return mid
    if x<nums[mid]:
        return search(nums,x,left,mid-1)
    return search(nums,x,mid+1,right)

nums=list(map(int,input("Enter sorted numbers: ").split()))
x=int(input("Enter element to search: "))
ans=search(nums,x,0,len(nums)-1)
print("Index:",ans)
