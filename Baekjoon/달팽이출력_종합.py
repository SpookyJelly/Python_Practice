from pprint import pprint

# 달팽이 출력 1

# 델타 없이, switch라는 변수로 출력 방향을 컨트롤 하는 방식


N, M = list(map(int,input().split()))
#N = 7  # 한 리스트(행)에 포함되어 있는 요소의 갯수
#M = 6  # 전체 리스트에 행이 몇개인지 (열)의 갯수
arr = [[0] * N for x in range(M)]
row = M  # row는 음의 방향이므로,
col = 0  # col은 (행(리스트)의 요소들은 양의 방향이므로)
cnt = 1
switch = 1
while N > 0 and M > 0:  # 둘 중 하나가 앵꼬나는 순간 끝
    # 세로를 입력하는 달팽이
    for __ in range(1, M + 1):
        row -= switch
        arr[row][col] = cnt
        cnt += 1

    # 한행,한열을 풀로 입력할때마다 다음 달팽이는 자신의 최대 길이에서 1을 감소한 만큼 입력해야함
    # (비록 자신의 타입과 다르더라도)
    # 그러니까, 쭉 입력만 되면, 일단 -1 하고 시작
    N -= 1
    M -= 1
    switch *= -1
    # 가로를 입력하는 달팽이
    for _ in range(1, N + 1):
        col -= switch
        arr[row][col] = cnt
        cnt += 1

pprint(arr)

##################################################################################

# 달팽이 출력 2

# 방향 지시자인, 델타를 만들어서 시행하는 방식

# 행과 열를 입력
R, C = map(int, input().split())

# 우 밑 좌 상 반복

# dx=[1,0,-1,0]
# dy=[0,1,0,-1]

# 수정해서 좌 상 우 하 로 해보자
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# C = 리스트의 길이 --> 열, R = 리스트의 갯수 --> 행
board = [[0] * C for _ in range(R)]

# 최초 값을 직접 입력
# 좌 상 우 하에 맞게 시작값도 수정해야겠지?
# board[R-1][C-1]은 board의 가장 오른쪽 아래에 있는 지점이다.
# 시작위치를 잘 생각하고 입력을 해줘야한다.
board[R - 1][C - 1] = 1

# 초기 값은 위에서 이미 해놓았기에, cnt는 2부터 시작
cnt = 2

# nx와 ny 는 board에서의 좌표가 될 것이다.
nx, ny = C - 1, R - 1

# R행 C열의 셀의 개수는 R*C개이므로, 그까지만 순환한다.
while cnt <= (R * C):
    # 특이하게도, 이 달팽이는 for문들 돈다. dx/dy 세트를 계속 순환하게 하려고 만든거 같은데, 이거 없앨수도?
    # 드는 생각은, d가 4번밖에 반복이 안되므로, 한바퀴 다 돌면 멈추는거 아닐까? 인데,
    # 생각해보니, for가 종료되어도 상위 while문은 계속 순환하고 있기에,
    # 다시 한번 for d in range(4) 가 시작된다.

    for d in range(4):
        nx += dx[d]  # nx와 ny에 전부 dx[0~3] 만큼을 더한 뒤,
        ny += dy[d]  # 해당 위치서부터 아래의 while문을 돌린다.

        while 0 <= nx < C and 0 <= ny < R and board[ny][nx] == 0:  # nx가 C이하, ny가 R 이하, ny/nx 가 0일때만
            board[ny][nx] = cnt  # cnt를 새긴다.
            cnt += 1  # 그리고 cnt += 1
            nx += dx[d]  # 새로운 nx는 마찬가지로, dx[d] 만큼 추가해준다. d가 뜻하는 방향에 따라
            ny += dy[d]  # 새로운 nx와 ny의 값이 정해지겠지.
        nx -= dx[d]  # while문이 종료 되면,
        ny -= dy[d]  # nx와 ny의 값을 원위치 한다.
pprint(board)