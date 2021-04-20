# 2003번 수들의 합

# N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다.
# 이 수열의 i번째 수부터 j번째 수까지의 합 A[i] + A[i+1] + … + A[j-1] + A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 N(1 ≤ N ≤ 10,000), M(1 ≤ M ≤ 300,000,000)이 주어진다. 
# 다음 줄에는 A[1], A[2], …, A[N]이 공백으로 분리되어 주어진다. 각각의 A[x]는 30,000을 넘지 않는 자연수이다.

# 즉, 연속된 요소의 합이 M 인 경우를 count 해서 출력하라는 것

def sol1():
    global cnt,start,end
    while start <=end and end<=N:
        summ = sum(lst[start:end])
        if summ==M:
            cnt+=1
        if summ<=M:
            end+=1
            continue
        elif summ>M and start<end:
            start+=1
            continue
        else:
            start+=1
            end+=1

def sol2():
    global cnt,start,end,total
    while 0 <= start < N and 0 <= end < N:
        if total == M:
            cnt += 1
        if total <= M:
            total += lst[end]
            end += 1
        else:
            total -= lst[start]
            start += 1

    while 0 <= start < N:
        if total == M:
            cnt += 1
        total -= lst[start]
        start += 1

def sol3():
    global cnt,start,end,total
    while 0 <=start<N:
        # 예외 조건.end가 끝까지 다 갔는데도 M 보다 작음
        if end >= N and total < M:
            break
        # M 보다 작으면 플러스
        if total <M:
            total += lst[end]
            end += 1
        else: # total >=M
            if total == M:
                cnt += 1
            start += 1
            end = start
            total = 0
# N,M = map(int,input().split()) # M: 목표값, N:리스트의 길이
N,M = 10,5

# lst = list(map(int,input().split()))

lst = [1,2,3,4,2,5,3,1,1,2]
start = 0
end = 0
cnt = 0
total = 0

sol3()
print(cnt)




# while True:
#     if start == N-1 and total < M:
#         break
#     if total < M:
#         end += 1
#         total += lst[end]
#     elif total == M:
#         cnt += 1
#         total -= lst[start]
#         start += 1
#     elif total > M:
#         total -= lst[start]
#         start += 1


