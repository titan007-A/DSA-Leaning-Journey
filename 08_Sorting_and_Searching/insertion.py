nums=[2, 5, 5, 5, 7, 23, 25, 26, 32, 36, 42, 43, 46, 58, 64, 75]

def sort(nums):
    for i in range(len(nums)):
        key=nums[i]
        j=i-1
        while(j>=0 and nums[j]>key):
            if(nums[key]<nums[j]):
                nums[j+1]=nums[j]
                j-=1
            
        nums[j+1]=key
    return nums



print(sort(nums))