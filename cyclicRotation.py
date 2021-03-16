def solution(A, K):
    # write your code in Python 3.6
    c = len(A)
    b = A.copy()                                 #created another copy of list iterate
    if K == len(A):
        return A
    else:
        while (K > 0):
            K = K-1
            i = 0
            for i in range(0,c):
                if(i < c-1):                     #swapping variable using both lists or you can say as array
                    b[i+1] = A[i]
                else:
                    b[0] = A[i]
            A = b.copy()
        return A
      
 
# added driver code below to check your own values
num = [3,8,9,7,6]
i = 3
print(solution(num,i))
