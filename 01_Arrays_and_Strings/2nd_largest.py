 #brute force

nums=[23,42,52,63,74,75,85,23]

def sol(nums):
    first_max_index=0
    second_max=float('-inf')
    for i in range(len(nums)):
        if(nums[first_max_index]<nums[i]):
            first_max_index = i
    
    for i in range(len(nums)):
        if (second_max<nums[i] and (i)!=first_max_index):
            second_max=nums[i]

    return second_max

print(sol(nums))
        

