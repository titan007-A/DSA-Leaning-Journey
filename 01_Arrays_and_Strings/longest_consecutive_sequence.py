nums=[1,2,90,98,3,27,91,93,92,95,94]

def sols(nums):
    lseq=1
    
    for i in range(len(nums)):
        st=nums[i]
        count=1
        while (st+1 in nums):
            count=count+1
            st=st+1
        lseq = max(lseq,count)
            
    print(lseq)
sols(nums)
