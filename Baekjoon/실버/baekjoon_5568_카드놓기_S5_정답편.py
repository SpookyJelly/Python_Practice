# 5568번 카드 놓기

"""
상근이는 카드 n(4 ≤ n ≤ 10)장을 바닥에 나란히 놓고 놀고있다.
각 카드에는 1이상 99이하의 정수가 적혀져 있다.
상근이는 이 카드 중에서 k(2 ≤ k ≤ 4)장을 선택하고, 가로로 나란히 정수를 만들기로 했다.
상근이가 만들 수 있는 정수는 모두 몇 가지일까?

예를 들어, 카드가 5장 있고, 카드에 쓰여 있는 수가 1, 2, 3, 13, 21라고 하자.
여기서 3장을 선택해서 정수를 만들려고 한다.
2, 1, 13을 순서대로 나열하면 정수 2113을 만들 수 있다.
또, 21, 1, 3을 순서대로 나열하면 2113을 만들 수 있다.
이렇게 한 정수를 만드는 조합이 여러 가지 일 수 있다.

n장의 카드에 적힌 숫자가 주어졌을 때,
그 중에서 k개를 선택해서 만들 수 있는 정수의 개수를 구하는 프로그램을 작성하시오.


"""
def DFS(L):

    # 종료조건은, 뽑아야하는 갯수 == DFS의 level이다.
    # level은 각 재귀마다 하나씩 커진다.
    if L == k:
        all.append(result[:])
        return
    else:
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                # result,그러니까 출력될 친구의 level번째 요소를 lst[i]에 있는것으로 바꾼다.
                # 근데, i는 일단 무조건, 0~n-1까지는 변경된다는것을 생각하면,
                # 당연히, 다양한 조합을 맛봐야하는 result[L]이 lst[i]를 할당받아야한다.
                result[L] = lst[i]
                DFS(L+1)
                visited[i] = False
                # result[L] = 0 이건 굳이 필요없다. 왜냐? 어짜피 for 문마다 다시 할당되기에


# n = int(input())
# k = int(input())
# lst = [int(input()) for _ in range(n)]

n = 4
k = 2
lst = [1, 2, 12,1]

# 자, DFS 활용한 순열재귀 구할때 필요한것은 다음과 같다.
# 1. 방문 체크해줄 lst와 동일한 크기의 False 리스트 --> visited
# 2. 실제 요소들로 채워질 (순열이 될) 공백 리스트 --> result
# 다행이도, 이건 그냥 순열의 갯수만 구하면 되기에, cnt만 잘 이용해보자.

visited = [False] * n
result = [0] * k
all = [] # 전체 순열을 받아줄 빈 임시 리스트


DFS(0) # 여기 0은 초기 level을 뜻한다.


# 이하는 출력을 맞추기 위한 부분
b = []
a = [list(map(str,elem)) for elem in all]
for i in range(len(a)):
    tem = ''
    for j in range(len(a[0])):
        tem += a[i][j]
    b.append(tem)

print(len(set(b)))


# 아 참나...동일한 카드가 있는 경우에는 중복을 거르지 못하기에, 순열을 문자열로 변환시킨다음, 그걸 합쳐서
# set으로 만들어서 중복 없앤 다음에, 길이를 출력해야겠다.