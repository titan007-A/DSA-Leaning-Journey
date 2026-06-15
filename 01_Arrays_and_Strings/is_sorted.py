nums=[2, 5, 5, 5, 7, 23, 25, 26, 32, 36, 42, 43, 46, 58, 64, 75]

def sol(nums):
    is_sorted = True
    for i in range(len(nums)-1):
        if (nums[i]>nums[i+1]):
            is_sorted=False
    return is_sorted

print(sol(nums))