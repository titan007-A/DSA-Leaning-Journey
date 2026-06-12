# Problem: [Print factors of a number]
# Link: [URL to LeetCode/GeeksforGeeks/etc.]
# Approach: [Brief description of the logic, e.g., "Used a hash map to track frequencies"]
# Time Complexity: O
# Space Complexity: O(N)
import math
def solution(num):
    factors=[]
    for i in range(1,int(math.sqrt(num))+1):
        if num%i==0:
            factors.append(i)

    factors.append(num)
    return factors


print(solution(60245353543))