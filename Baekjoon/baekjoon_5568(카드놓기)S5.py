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


# def perm(arr, depth, n, k):
#     # depth가 0부터 시작하여 k라면, k개를 모두 뽑은 것이므로, print후 return
#     if depth == k:
#         print(arr)
#         return
#     for idx in range(depth, n):
#         # 각 depth에 대해 남아있는 것들 중에 모두 뽑고,
#         # 해당 경우에 대해 재귀적으로 perm 함수를 돌리고
#         # 원상복구하여 다시 경우의 수를 찾는다.
#         arr[idx], arr[depth] = arr[depth], arr[idx]
#         perm(arr, depth + 1, n, k)
#         arr[idx], arr[depth] = arr[depth], arr[idx]



# n = int(input())
# k = int(input())
# lst = [int(input()) for _ in range(n)]
# print(lst)
# n = 5
# k = 2
# lst = [1, 2, 3, 13, 21]
# visited = [0] * n  # 방문 체크할 행렬
# # print(perm(lst, 0,n,k))
#
# # 일단 for문으로 해보자...
#
# for i in range(n-2):
#     for j in range(i+1,n-1):
#         for k in range(j+1,n):
#             print([lst[i],lst[j],lst[k]])
# # 이건 조합이네
# print('='*50)
#
# # 이건 퍼온 방법인데, 설명도 못할정도로 이해를 못했다...
# def perm(lst,n):
#     result =[]
#     # 주어진 리스트보다 더 큰 순열을 반환하라고 하면 그냥 빈 리스트를 반환
#     if n > len(lst) :
#         return result
#     # 베이스 케이스, 만약에
#     if n == 1:
#         for i in lst:
#             result.append([i])
#     elif n > 1:
#         for i in range(len(lst)):
#             temp = [i for i in lst]
#             temp.remove(lst[i])
#             for p in perm(temp,n-1):
#                 result.append([lst[i]]+p)
#     return result
#
# print(perm(lst,7))


# DFS를 이용한 순열 구현법
# 1. DFS를 이용
# 2. 체크리스트를 이용
# 순열은 그냥 외운다.
# 이거 괜찮다... 물건이다...
def DFS (L):
    #DFS는 종료조건이 명확히 보이는 경우 사용한다.
    # DFS의 레벨이 뽑는 갯수와 동일하면 종료가 된다.


    if L == r:
        print(result)
        all.append(result[:]) # result는 계속 재귀를 돌면서 바뀌기 때문에, 복사안해주고 append하면 한번에 다 바뀔 수 있다.
    else:
        for i in range(len(n)):
            if checklist[i] == 0: # 아직 체크리스트를 쓰지 않아서 한단계 들어갈 수 있다.
                ########재귀로 들어갈때 쓰는 전처리 친구들은 위에 써라
                result[L] = n[i]
                checklist[i] = 1
                DFS(L+1)
                ########재귀를 백트랙할때 쓰는 조건은 여기 아래에 적어라
                checklist[i] = 0 # if L == r의 백트랙을 할때 (돌아올때, 체크리스트를 원복해야한다)

    return all

n = [13,2,3,1,4,5]
r = 3
result = [-1]*r
checklist = [0] * len(n)
all = []
DFS(0) # level 0부터 시작한다.

print(DFS(0))


# 이제 상근이 놈의 의문점을 해결해주러 가자.