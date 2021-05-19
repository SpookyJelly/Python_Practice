#피보나치수 S4
#첫째 줄에 n이 주어진다. n은 10,000보다 작거나 같은 자연수 또는 0이다.

# 출력
# 첫째 줄에 n번째 피보나치 수를 출력한다.



N = int(input())
memo = [0] + [0]* (N)
if N > 0:
    memo[1] = 1
    for n in range(2,N+1):
        memo[n] = memo[n-1] + memo[n-2]

print(memo[-1])


# n=int(input())
# if n<2:
#     print(n)
# else:
#     x,y=0,1
#     for i in range(2,n+1):
#         x,y=y,x+y
#     print(y)