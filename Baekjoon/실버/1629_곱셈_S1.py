def pow(a,b,c):
    if b == 1:
        return a % c
    
    n = pow(a,b//2,c)
    temp = n * n # n을 재귀형으로 구하기 때문에, temp은 n이 구해진 뒤 나온다.
    if b%2 == 0:
        return temp % c
    else:
        return a * temp % c


a,b,c = map(int,input().split())

ans = pow(a,b,c)
print(ans)