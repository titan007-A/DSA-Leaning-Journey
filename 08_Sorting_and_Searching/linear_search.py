nums=[2, 5, 5, 5, 7, 23, 25, 26, 32, 36, 42, 43, 46, 58, 64, 75]

def sol(nums,target,l,r):
    mid = (l+r)//2
    if nums[mid]==target:
        return nums[mid]
    elif target<nums[mid]:
        return sol(nums,target,l,mid-1)
        
    else:
        return sol(nums,target,mid+1,r)
    


print(sol(nums,23,0,len(nums)-1))


