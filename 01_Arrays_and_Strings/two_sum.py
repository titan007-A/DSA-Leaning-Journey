nums=[5,9,1,2,4,15,6,3]

target=13


def two_sums(nums,target):
    d1={}
    for i in range(len(nums)):
        d1[nums[i]] =i
    for i in range(len(d1)):
        remaining = target-nums[i]
        if remaining in d1:
            return[i,d1[remaining]]
        
        pass
print(two_sums(nums,13))
