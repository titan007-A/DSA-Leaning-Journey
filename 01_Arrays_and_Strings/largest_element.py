nums=[55,32,-97,99,3,67]

def sol(nums):
    max = nums[0]
    for i in range(nums):
      largest = max(largest,nums[i])
    return largest

