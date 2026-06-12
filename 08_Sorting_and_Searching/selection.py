nums = [3,45,32,5,52,55,6,4,47,342,2,23,35]

#core philosophy is to find the min index and replace the i pointer with minimum index
#j will always start after which is i+1


def sort(nums):
    for i in range(len(nums)):
        min_index=i
        for j in range(i+1,len(nums)):
            if (nums[min_index]>nums[j]):
              min_index=j  
        nums[i],nums[min_index]=nums[min_index],nums[i]

    return nums


print(sort(nums))


