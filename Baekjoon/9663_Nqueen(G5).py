# 9663번 N queen

def check(board, i):
    global cnt
    # 3. 본격적으로 퀸을 놓기 전에, 정말 겹치는 곳이 없는지 확인한다.
    if (promising(i, board)):
        if i == N:
            cnt += 1
        else:
            for j in range(1, N + 1):
                board[i + 1] = j
                check(board, i + 1)


# 4. 그리고 이제 검사를 하는데, board[i] == board[k] 면 탈락,(같은 열에 두개의 퀸 위치), 대각선 abs(board[i]-board[k]) == i-k 이면 탈락
# 그리고 그 두가지 검사를 하나의 함수에서 하자
# promising은 현재까지 말이 놓인 행 이상으로는 검사하지 않는다.
def promising(i, board):
    for k in range(1, i):
        if (board[i] == board[k]) or (abs(board[i] - board[k]) == i - k):
            return False
    return True


N = int(input())
# 1. 먼저 1차원 배열 만들자, 인덱스가 열번호, 요소가 행 번호가 될 것이다. (단, N+1 길이로 만들어라)
board = [0] * (N + 1)
cnt = 0
# 2. dfs를 사용해서 검사한다.
check(board, 0)
print(cnt)

## 시간 초과 개빡친다 진짜


# n, ans = int(input()), 0
# a, b, c = [False]*n, [False]*(2*n-1), [False]*(2*n-1)
#
# def solve(i):
#     global ans
#     if i == n:
#         ans += 1
#         return
#     for j in range(n):
#         if not (a[j] or b[i+j] or c[i-j+n-1]):
#             a[j] = b[i+j] = c[i-j+n-1] = True
#             solve(i+1)
#             a[j] = b[i+j] = c[i-j+n-1] = False
#
# solve(0)
# print(ans)

