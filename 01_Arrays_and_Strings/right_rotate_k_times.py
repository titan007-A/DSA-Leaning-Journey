nums =[5,-2,5,3,1,0,6,10,7]


# def sols(nums,k):
#     for i in range(k):
#         nums[:]=[nums[-1]]+nums[0:(len(nums)-1)]

#     return nums

# print(sols(nums,1))

#better solution


def sol2(nums,k):
    nums[:]= [nums[len(nums)-k]] + nums[0:len(nums)-1] 
    return nums
print(sol2(nums,10))