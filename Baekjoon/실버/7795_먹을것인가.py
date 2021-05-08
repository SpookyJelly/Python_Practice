#7795
# A는 자기 보다 크기가 작은 먹이만 먹을 수 있다.
# 두 생명체 A와 B의 크기가 주어졌을때,  A의 크기가 B보다 큰 쌍이 몇개나 있는지 구하시오


T = int(input())
for tc in range(T):
    n,m = map(int,input().split())
    N = list(map(int,input().split()))
    M = list(map(int,input().split()))

    N.sort()
    M.sort()
    # N.sort(reverse=True)
    # M.sort(reverse=True)

    cnt = 0

    # for i in range(n):
    #     for j in range(m):
    #         if N[i] > M[j]:
    #             cnt += m-j
    #             break
    
    # print(cnt)

    # 요점은 조건을 만족하는 최대 인덱스를 찾는것
    for fish in N:
        left = 0 
        right = m-1
        res = -1 # 리스트 크기가 1개인 경우를 대비
        while left <= right:
            mid = (left+right)//2
            if M[mid] >= fish: # M[mid]보다 내 물고기가 작다 --> 전체 사이즈 줄인다 (같아도 매한가지)
                right = mid -1

            else:# M[mid]보다 내 물고기가 크다 --> 전체 사이즈 키운다
                # res = mid
                cnt += (mid-left)+1
                left = mid + 1
                # cnt = (right-mid) + 1이 안되는 경우
                #  fish = 7인데, [1,3,6,100,150,200]에서 mid는 6이다
                # 근데 실제로 7이 조건을 만족하는 경우는 6 하나인데,
                # 위 계산식은 싹 더해버린다.
                # 차라리 (mid-left)+1 이게 맞을듯 < -- 맞다
        # cnt += res+1 # 탐색이 다 끝난 뒤에 연산을 해라 안그럼 값이 꼬일수도 있다
    print(cnt)
            