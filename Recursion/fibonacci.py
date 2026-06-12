#Appraoch: We have to consider two base cases we have to call the function twice and we know that the value of 
# 0 and 1 position in fibo are different so they have to handled separately



def solution(num):
    if num==0:
        return 0
    if num==1:
        return 1
    return solution(num-2)+solution(num-1)
    

print(solution(8))