nums=[5,10,-3,-1,-10,6]

def sols(nums):
    result=[0]*(len(nums))
    p=0
    n=1
    for i in range(len(nums)):
        if (nums[i]>=0):
            result[p]=nums[i]
            p=p+2
        if (nums[i]<0):
            result[n]=nums[i]
            n=n+2
    
    return result

print(sols(nums))