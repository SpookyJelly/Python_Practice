# RGB거리에는 집이 N개 있다. 거리는 선분으로 나타낼 수 있고, 1번 집부터 N번 집이 순서대로 있다.

# 집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다. 
# 각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때, 아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.

# 1번 집의 색은 2번 집의 색과 같지 않아야 한다.
# N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
# i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.

# 첫째 줄에 집의 수 N(2 ≤ N ≤ 1,000)이 주어진다. 
# 둘째 줄부터 N개의 줄에는 각 집을 빨강, 초록, 파랑으로 칠하는 비용이 1번 집부터 한 줄에 하나씩 주어진다.
# 집을 칠하는 비용은 1,000보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄에 모든 집을 칠하는 비용의 최솟값을 출력한다.

#  필요 없음
# visited = [False]*3
# result = []

# def combi(sample,depth):
#     mini = 9999

#     if depth == 3:
#         # 결과값 반환
#         print(result)
#         result.append(sample[:])
#         return 


#     for i in range(3):
#         if not visited[i]:
#             visited[i] = True
#             sample[depth] = i
#             combi(sample,depth+1)
#             visited[i] = False


import sys
sys.stdin = open('1149_input.txt','r')

# RGB 케이스, 문제의 조건에 맞는 경우만 나열했다. 경우의 수가 적기에 따로 combi 구하지 않고, 직접 하드코딩하여 속도와 생산성을 높임
case = [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0],[0,1,0],[0,2,0],[1,0,1],[1,2,1],[2,0,2],[2,1,2]]
N = int(input())
test = []
result = 0
memo = 999
for _ in range(N):
    house = list(map(int,input().split()))
    test.append(house)
    mini = 99999999
    if len(test) == 3:
        for elem in case:
            cost = 0
            for idx in range(len(elem)):
                cost += test[idx][elem[idx]]
                if cost > mini:
                    break

            if cost < mini:
                mini = cost
                memo = elem[2]

        result += mini
        test = []

# 앗 씨발....전체 입력이 3으로 나누어 떨어지지 않을수도 있잖아??

# 출력전, 입력이 1,2 인 경우일때를 대비하여 한 번 더 최솟값 출력 과정을

# 입력이 1개인 경우
print(memo)
if len(test) == 1:
    tem_lst = []
    for idx,value in enumerate(test[0]):
        if idx == memo:
            continue
        else:
            tem_lst.append(value)
    print(tem_lst)
    result += min(tem_lst)

# 입력이 남아 있는 경우 --> 1개 2개 통합 --> 다시 나눠야하나??
if len(test)==2:
    tem_lst = []

    for idx,value in enumerate(test[0]):
        if idx == memo:
            continue
        else:
            for idx2,value2 in enumerate(test[1]):
                if idx2 == idx:
                    continue
                else:
                    tem_lst.append(value+value2)

    result += min(tem_lst)
                    


print(result)

