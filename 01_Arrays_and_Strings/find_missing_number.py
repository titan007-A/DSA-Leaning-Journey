nums =[1,0,3,4]

def sols(nums):
    for i in range(1,len(nums)+1):
        if i not in nums:
            return i
        
print(sols(nums))

