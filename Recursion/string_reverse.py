str1="gagan"


def solution(str1,left,right):
   if left>right:
    return True
   
   if str1[left]==str1[right]:
    return solution(str1,left+1,right-1)
   else:
     return False


print(solution(str1,0,len(str1)-1))

