prices=[10,9,7,1,1,4,5]

def sol(nums):
    buy_index=0
    for i in range(len(prices)):
        if (nums[buy_index]>nums[i]):
            buy_index=i
    if buy_index==len(nums)-1:
        return -1
    sell_index=buy_index
    for i in range(buy_index+1,len(prices)):
        if (nums[sell_index]<nums[i]):
            sell_index=i
            if(i==len(nums)-1 and sell_index==buy_index):
                sell_index=-1
    
    if sell_index==-1:
        return -1
    
    return f"the max profit is {-nums[buy_index]+nums[sell_index]}"




print(sol(prices))