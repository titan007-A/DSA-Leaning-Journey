# Problem: [A number is palindrome or not]
# Link: [URL to LeetCode/GeeksforGeeks/etc.]
# Approach: [Brief description of the logic, e.g., "Used a hash map to track frequencies"]
# Time Complexity: O
# Space Complexity: O(N)

def solution(nums):
    new_nums=0
    org=nums
    while nums>0:
        extr_digit = nums%10
        new_nums= new_nums*10+extr_digit
        nums=nums//10
    print(new_nums)
    if new_nums==org:
        return True
    else:
        return False

print(solution(1331))
    
