nums1=[1,1,1,2,4,6,7]
nums2=[1,2,3,6,7,8,9]

def sols(num1,num2):
    i=0
    j=0
    nums3=[]
    if len(num1)>len(num2):
        smaller= len(num2)
    else:
        smaller=len(num1)

    for i in range(smaller):
        if nums1[i]<nums2[i]:
            nums3.append(nums1[i])
        else:
            if nums2[i] not in nums3:
                nums3.append(nums2[i])
    return nums3

print(sols(nums1,nums2))