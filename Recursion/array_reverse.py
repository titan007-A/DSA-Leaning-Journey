arr=[20,23,42,53,14,42,15]


def solution(arr,left,right):
    if (left>=right):
        return
    arr[left],arr[right]=arr[right],arr[left]
    solution(arr,left+1,right-1)
solution(arr,1,3)
print(arr)    