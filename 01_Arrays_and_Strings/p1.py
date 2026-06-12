# Problem: [Extratioon of digits]
# Link: [URL to LeetCode/GeeksforGeeks/etc.]
# Approach: [simply used loops"]
# Time Complexity: O(N)
# Space Complexity: O(N)


num=5873
def my_solution(num):
    while num>0:
        digit = num % 10
        print(digit)
        num = num // 10
        print(num)
my_solution(num)