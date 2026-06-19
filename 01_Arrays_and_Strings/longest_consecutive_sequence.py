nums=[1,2,90,98,3,27,91,93,92,95]

def sols(nums):
    max_lseq=1
    lseq=1
    
    for i in range(len(nums)):
        if nums[i]==nums[i-1]:
            continue
        
        if (st+1) in nums:
            lseq=lseq+1
            st=st+1
        elif(max_lseq<lseq):
            max_lseq=lseq
        else:
            st=nums[i]
            lseq=1
            
    print(lseq)
sols(nums)
