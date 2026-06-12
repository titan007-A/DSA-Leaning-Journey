# Problem: [A number is palindrome or not]
# Link: [URL to LeetCode/GeeksforGeeks/etc.]
# Approach: [Brief description of the logic, e.g., "Used a hash map to track frequencies"]
# Time Complexity: O
# Space Complexity: O(N)

def solution(num):
    arm_num=0
    while num>0:
        extr = num%10
        arm_num= arm_num + (extr*extr*extr)
        num= num//10
        print(arm_num)
    return arm_num

print(solution(153))
