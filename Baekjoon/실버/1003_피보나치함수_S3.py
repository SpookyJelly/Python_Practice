# 1003번 피보나치
# 재귀형으로 피보나치 수열을 생성할때, fibonacci (0)과 fibonacci(1)이 몇회 호출되는지 구하시오

def fibo(n):
    # 처음에는 그냥 재귀로 건내줬는데, 시간 초과가 났다.
    # 그래서 메모이제이션 방법을 이용해서 memo라는 리스트에 등판했던 값을 넣어놓고, 다음 값을 구할때는 리스트에 저장되어있는
    # 값을 참조 (call by value)하여 속도를 무진장 높히는 방법이다.
    # global cnt0,cnt1
    if n == 0:
        # cnt0 +=1
        return memo[0]
    if n == 1:
        # cnt1+=1
        return memo[1]
    
    result = [0,0,0]
    for idx in range(3):
        result[idx] = memo[n-2][idx]+memo[n-1][idx]

    return result

TC = int(input())

for tc in range(1,TC+1):
    N = int(input())
    # 순서대로 fibo 값, fibo(0) 등판횟수, fibo(1) 등판 횟수 --> 생각해보니 굳이 fibo 값을 구할 필요는 없는거 였다.
    # 항상 기억해라. 2차원 배열 생성할때는 리스트 내포를 이용해서 만들어야지 복사가 안된다.
    memo = [[0,0,0] for _ in range(N+1)]
    memo[0] = [0,1,0]
    # N이 0이면 memo[1] 세팅하는것도 에러나니까, memo[1] 세팅은 조건을 달아서 진행했다.
    if N >= 1:
        memo[1] = [1,0,1]
        # 이 블럭도 덜 들여써도 되는데, (N == 0 이여도 range(2,1) 이 되어 실행이 안되므로)
        # 직관성을 위해 안으로 넣어줬다.
        for idx in range(2,N+1):
            for i in range(3):
                memo[idx][i] = fibo(idx-1)[i] + fibo(idx-2)[i]

    print(memo[N][1],memo[N][2])
    

# 그냥 재귀하니까 또또또또 시간초과 --> 메모이제이션 이용
