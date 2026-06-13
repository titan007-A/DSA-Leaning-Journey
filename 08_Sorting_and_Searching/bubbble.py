#core philosophy is adjacent sorts

nums=[2, 5, 5, 5, 7, 23, 25, 26, 32, 36, 42, 43, 46, 58, 64, 75]

def sort(nums):
    for i in range(len(nums)):
        is_swapped = False
        for j in range(len(nums)-1):
            if(nums[j]>nums[j+1]):
                nums[j],nums[j+1]=nums[j+1],nums[j]
                is_swapped=True
        if (is_swapped)==False:
            break        
    print(nums)


sort(nums)