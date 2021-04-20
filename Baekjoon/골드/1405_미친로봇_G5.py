# 1405번 미친 로봇
"""
가지치기, 브루트포스, 그래프 탐색

"""

# 통제 할 수 없는 미친 로봇이 평면위에 있다. 
# 그리고 이 로봇은 N번의 행동을 취할 것이다.
# 각 행동에서 로봇은 4개의 방향 중에 하나를 임의로 선택한다. 그리고 그 방향으로 한 칸 이동한다.

# 로봇이 같은 곳을 한 번보다 많이 이동하지 않을 때, 
# 로봇의 이동 경로가 단순하다고 한다. (로봇이 시작하는 위치가 처음 방문한 곳이다.) 
# 로봇의 이동 경로가 단순할 확률을 구하는 프로그램을 작성하시오.
# 예를 들어, EENE와 ENW는 단순하지만, 
# ENWS와 WWWWSNE는 단순하지 않다. (E는 동, W는 서, N은 북, S는 남)

# 첫째 줄에 N, 동쪽으로 이동할 확률, 서쪽으로 이동할 확률, 남쪽으로 이동할 확률, 북쪽으로 이동할 확률이 주어진다. 
# N은 14보다 작거나 같은 자연수이고,  모든 확률은 100보다 작거나 같은 자연수 또는 0이다.
# 그리고, 동서남북으로 이동할 확률을 모두 더하면 100이다.

# 확률의 단위는 %이다.

# 출력

# 첫째 줄에 로봇의 이동 경로가 단순할 확률을 출력한다. 절대/상대 오차는 10-9 까지 허용한다.
# 그냥 쓰면 시간초과나니까, 가망없는 놈들들을 잘 걸러야한다... 일단 percent가 0과 거의 근접한 놈들..얘들한테 시간 낭비하면 안될거 같다
# 지도를 직접 그려서 풀이한 사람이 많다. 지도를 반복해서 그리는게 아니기 때문에, 적절한 크기의 지도를 만든다면 실행속도가 더 빨라진다는 건가?
import math

def manic(x:int,y:int,cnt:int,percent:int,path:list)->None:
    global total
    if (x,y) in path:
        return
    if cnt == N:
        total += percent
        return
    else:
        if math.isclose(percent,0):
            return
        for idx in range(4):
            manic(x+dx[idx],y+dy[idx],cnt+1, percent*(data[idx]*0.01),path+[(x,y)])
    return

# 진짜 지도를 그려버리는게 더 빠르고, 메모리도 덜 먹는다.
# in 메서드와 math 모듈 불러오는 작업이 그렇게 시간을 많이 잡아 먹나?
def manic2(x,y,cnt,percent):
    global total
    if cnt == N:
        total += percent

    else:
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            # if 0<=nx<N and 0<=ny<N: <-- 어짜피 짱짱 넓게 만들어놨기 때문에 인덱스 에러 일어날 일 없음
            if maps[nx][ny]:
                continue
            maps[nx][ny] = 1
            manic2(nx,ny,cnt+1,percent*(data[i]*0.01)) # 재귀 구조로 방문처리
            maps[nx][ny] = 0




# data = list(map(int,input().split()))
data = [2,25,25,25,25]
N = data.pop(0)
total = 0
dx= [1,-1,0,0]
dy = [0,0,1,-1]
maps = [[0 for _ in range((N*2)+1)] for __ in range((N*2)+1)]
# manic(0,0,0,1,[])
maps[N//2][N//2] = 1 # 시작위치 True로 만들기
manic2(N//2,N//2,0,1)
print(total)

# 시간복잡도 줄이려고 path를 set으로 썻는데, set에는 unhashable한 자료형은 못 넣는다. -> 그럼 사전형으로 바꾼다

# def manic(x:int,y:int,cnt:int,percent:int,path:dict)->None:
#     global total
#     if (x,y) in path:
#         return
#     if cnt == N:
#         total += percent
#         return
#     else:
#         # 동쪽으로
#         if math.isclose(percent,0):
#             return
#         if path.get((x,y),1):
#             path[(x,y)] = 0 *******<-- 외부에서 path를 변경하니, path가 복사된다. 재귀를 빠져나와도 이전에 재귀할때 쓰던 path들이 남아있다.
#             """
#             그런 얇은 복사를 막기 위해서는 parameter에 직접 변경사항을 전달해줘야하는데, dict 자료형으로는 inline으로 키 밸류를 추가할 수 없다.
#             그래서 다시 리스트로 돌아왔다. 생각해보면 max( len(N))이라고 해봤자 14일텐데, 독립성만 잘 유지되면 그렇게 시간을 많이 잡아먹을거 같지 않다는 생각이였다.
#             """
#             manic(x+1,y,cnt+1,percent*(data[0]*0.01),path)
#             # 서쪽으로
#             manic(x-1,y,cnt+1,percent*(data[1]*0.01),path)
#             # 남쪽으로
#             manic(x,y+1,cnt+1,percent*(data[2]*0.01),path)
#             # 북쪽으로
#             manic(x,y-1,cnt+1,percent*(data[3]*0.01),path)
#     return