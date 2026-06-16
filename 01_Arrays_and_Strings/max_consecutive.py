nums=[1,1,0,1,1,1,1,0,1,1]

def sol(nums):
    count =1
    count_max = []
    for i in range(1,len(nums)):
        if nums[i]==1 and nums[i-1]==1:
            count= count+1
            count_max.append(count)
        elif (nums[i]==0 and nums[i-1]==1) or (nums[i]==1 and nums[i-1]==0):
            count=1
            count_max.append(count)
    highest=max(count_max)
    return highest if highest>1 else None


print(sol(nums))