nums = [5, 5, 6, 10]


def sol(nums):
    if not nums:
        return []
    i=0
    j=i+1
    while j<len(nums):
        if nums[j]!=nums[i]:
            nums[i+1] =nums[j]
            i=i+1
            print(i)
        j=j+1
    return nums[:i+1]





print(sol(nums))

