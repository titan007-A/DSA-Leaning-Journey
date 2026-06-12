# Problem: [Name of the Problem]
# Link: [URL to LeetCode/GeeksforGeeks/etc.]
# Approach: [Brief description of the logic, e.g., "Used a hash map to track frequencies"]
# Time Complexity: O
# Space Complexity: O(N)

def my_solution(nums):
    count =0
    while nums>0:
        count=count+1
        nums=nums//10
    return count