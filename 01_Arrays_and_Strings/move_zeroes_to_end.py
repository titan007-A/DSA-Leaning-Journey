nums = [0,52,51,16,0,0,61,0,401,15,51,53,363,0]

def sols(nums):
    i=0
    j=len(nums)-1
    while(i<j):
        if nums[i] !=0:
            i=i+1
        elif nums[j]==0:
            j=j-1
        else:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j-=1

    return nums



print(sols(nums))
                

