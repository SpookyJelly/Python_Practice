def solution(A):
    # write your code in Python 3.6
    A = list(set(A))
    A.sort

    for idx in range(len(A)):
        if idx+1 != A[idx]:
            return idx+1
        if idx == len(A)-1:
            if A[idx] > 0 :
                return A[idx]+1


print(solution([-1,-3]))