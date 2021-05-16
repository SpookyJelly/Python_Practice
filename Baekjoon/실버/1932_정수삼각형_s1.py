#맨 위층 7부터 시작해서 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때, 
# 이제까지 선택된 수의 합이 최대가 되는 경로를 구하는 프로그램을 작성하라. 아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택할 수 있다.

# 삼각형의 크기는 1 이상 500 이하이다. 삼각형을 이루고 있는 각 수는 모두 정수이며, 범위는 0 이상 9999 이하이다.

# 입력
# 첫째 줄에 삼각형의 크기 n(1 ≤ n ≤ 500)이 주어지고, 둘째 줄부터 n+1번째 줄까지 정수 삼각형이 주어진다.

# 출력
# 첫째 줄에 합이 최대가 되는 경로에 있는 수의 합을 출력한다

# 개선 방안 : 다른 사람들 풀이 보면 tree 배열 그 자체를 DP화 시켜서 풀었다. -> DP 배열을 따로 만든 내 경우보다 효율이 더 좋음
# 핵심 아이디어 -> DP를 통해 이전 단계에서 계산되었던 값들을 저장 후 이번 계산때 가져와서 사용한다.

import sys
sys.stdin = open('1932_input.txt','r')


N = int(input()) 


tree = [ [] for _ in range(N)]
memo = [ {} for _ in range(N)] # 삼각형의 경로값을 저장할 배열


for i in range(N):
    tem = list(map(int,(input().split())))
    tree[i] = tem

memo[0][0] = tree[0][0] # 초기값 설정 , memo의 0번 요소에 key == 0으로 tree[0][0]을 넣었다


# oidx : outer index / iidex: inner index
# oidx는 리스트의 각 요소에 접근할 때 사용
# iidx는 요소(dict)의 키 값으로 사용됨 

for oidx in range(1,len(tree)):
    for iidx in range(len(memo[oidx-1])):

        # 현재 경로의 최대값 memo[oidx][iidx] / memo[oidx][iidx+1] 은
        # 직전 까지의 경로 최대 합 memo[oidx-1][iidx] 에서 현재 순회중인 값 tree[oidx][iidx]와 tree[oidx][iidx+1]
        # 을 더한 값으로 결정된다.

        # num1과 num2이라는 변수를 선언하여  직전까지 경로 최대합 + 현재 순회중인 값 을 저장해놓는다
        num1 = memo[oidx-1][iidx]+ tree[oidx][iidx]
        num2 = memo[oidx-1][iidx]+ tree[oidx][iidx+1]

        # 근데 만약에 이미 memo[oidx][iidx] / memo[oidx][iidx+1]의 value가 존재한다면
        # max()를 이용해서 최대 값이 그 자리를 차지 할 수 있도록 한다.
        if memo[oidx].get(iidx):
            memo[oidx][iidx] = max(num1, memo[oidx][iidx])

        else:
            memo[oidx][iidx] = num1

        if memo[oidx].get(iidx+1):
            memo[oidx][iidx+1] = max(num2,memo[oidx][iidx+1])
        else:
            memo[oidx][iidx+1] = num2

# 위 과정을 반복하면, memo는 경로 최대값들의 집합이 되어있다.
# 가장 마지막 레벨의 values만 추출하여 최대값을 출력하자.
print(max(memo[-1].values()))

"""

따로 마음에 들었던 풀이

import sys

n = int(sys.stdin.readline())
tri = [[int(sys.stdin.readline())]]
for i in range(n-1):
    tri.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            tri[i][0] += tri[i-1][0]
        elif j == i:
            tri[i][j] += tri[i-1][j-1]
        else:
            tri[i][j] += max(tri[i-1][j-1], tri[i-1][j])

print(max(tri[n-1]))


"""