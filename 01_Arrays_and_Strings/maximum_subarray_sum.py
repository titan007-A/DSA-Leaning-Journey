nums=[-2,1,-3,4,-1,2,1,-5]
nums2=[-2,-5,-2,-4.-8]

def sols(nums):

    max=float("-inf")
    total=0
    for i in range(len(nums)):
        total=total+nums[i]
        max = max(max,total)
        if total<0:
            total=0


    return max



print(sols(nums))