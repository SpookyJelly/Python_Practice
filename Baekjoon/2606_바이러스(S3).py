#2606번 바이러스 (S3)
"""
문제
신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다.
한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.

예를 들어 7대의 컴퓨터가 <그림 1>과 같이 네트워크 상에서 연결되어 있다고 하자.
1번 컴퓨터가 웜 바이러스에 걸리면 웜 바이러스는 2번과 5번 컴퓨터를 거쳐
3번과 6번 컴퓨터까지 전파되어 2, 3, 5, 6 네 대의 컴퓨터는 웜 바이러스에 걸리게 된다.
하지만 4번과 7번 컴퓨터는 1번 컴퓨터와 네트워크상에서 연결되어 있지 않기 때문에 영향을 받지 않는다.


어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다.
컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때,
1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.

입력

첫째 줄에는 컴퓨터의 수가 주어진다.
컴퓨터의 수는 100 이하이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다.
둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다.
이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.

출력
1번 컴퓨터가 웜 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 첫째 줄에 출력한다.

"""
import sys
sys.stdin = open('2606_input.txt','r')

# 스택으로 만드는 DFS
def DFS(start:int):
    stack = [start]
    result = [] # 경로를 담아놓을 리스트
    visited = [0]*(N+1) # 방문체크로 사용할 리스트 <-- 인덱스 맞추기 귀찮으니까 node수 보다 하나 더 만듦
    while stack:
        way = stack.pop()
        if not visited[way] and way not in result:
            visited[way] = 1
            stack.extend(com_dic[way]) # extend 쓰는 이유: way와 이어진 노드들의 데이터를 다 stack에 넣어야하는데, com_dic이 리스트라서.
            result.append(way)
    return result
# 재귀로 만드는 DFS
def DFS_recursive(L:int,discoverd=[]):
    discoverd.append(L)
    while discoverd:
        for elem in com_dic[L]:
            if elem not in discoverd:
                DFS_recursive(elem,discoverd)
        return discoverd

# 큐로 만드는 BFS
def BFS(start:int):
    queue = [start]
    result = []
    visited = [0] * (N+1)
    while queue:
        way = queue.pop(0)
        if not visited[way] and way not in result:
            visited[way] = 1
            queue.extend(com_dic[way])
            result.append(way)
    return result


# 컴퓨터의 수
N = int(input())
# 컴퓨터에 경로의 수
pair = int(input())

com_dic={}
# dic 꼴로 경로 삽입
for idx in range(pair):
    S,G = map(int,input().split())
    com_dic[S] = com_dic.get(S,[]) + [G]
    com_dic[G] = com_dic.get(G,[]) + [S]

DFS_ver=DFS(1)
DFS_re_ver = DFS_recursive(1)
BFS_ver = BFS(1)
print('DFS_ver',DFS_ver,'ans:',len(DFS_ver)-1)
print('DFS_recursive_ver',DFS_re_ver,'ans',len(DFS_re_ver)-1)
print('BFS_ver',BFS_ver,'ans',len(BFS_ver)-1)