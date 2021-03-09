#1260번 DFS와 BFS
'''
문제
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000),
탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다.
어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다.
V부터 방문된 점을 순서대로 출력하면 된다.


'''
import sys
sys.stdin = open('1260_input.txt','r')
# DFS는 재귀랑 스택으로 구현 가능
# L이 시작 위치, discovered도 본인 위치로
def DFS_recursive (L:int,discovered:list):
    global DFS_ans
    # 일단 재귀로 할꺼니까, 종료조건부터 설정해주자.
    # discovered에 경로를 저장할꺼니까, 이거 길이가 N이 되면 되겠지? <-- 시발...이게 오산이였다.!!!! 모든 노드를 다 한번씩 도는  경우만에서는 맞겠지만,
    # 다들 분리되어있는 경우에는 무한 루프에 빠지는거셈...
    # 잘 되었는데...이 Return 값을 어떻게 가져가냐... Global이 답인가?
    if len(discovered) == N:
        DFS_ans = discovered[:]
        return

    while discovered : # 몇번 반복해야지?? <-- 몇번 돌려야할지 몰라서, 재귀 이후 후처리로 return 해줬다.
        for elem in node_dic[L]:
            if elem not in discovered:
                # 1. discovered.append(elem)은 안 통한다. 임시변수라서 그런듯. list로 객체화 시킨다음 더해줘야지 제대로 값이 들어간다
                # 2. return의 위치는 후처리 과정에 넣어준다. 안그러면 다른 방식으로 그래프 탐색한다.
                # 그러니까....한번 Depth 들어가면 그냥 역할 끝내자구
                DFS_recursive(elem,discovered+[elem])
                return

# 햐...이런 방식의 재귀도 있네.. 이러면 global 안써도 된다!
def DFS_recursive2 (L:int,discovered =[]):
    discovered.append(L)
    for w in node_dic[L]:
        if not w in discovered:
            discovered = DFS_recursive2(w, discovered)
    return discovered

# BFS는 큐로만 구현 가능
# 필요한거 : 큐, 방문체크할 친구 , 이동경로 체크할 친구
# 아니 근데 BFS가 이렇게 길었었나??? 뭔가 중복되게 사용하고 있는거 같은데 <-- 근데 맞았다.. BFS 경로 체크에는 queue랑 result 리스트 동시에 필요하다
def BFS(start:int):
    queue = []
    result = []
    visited = [0] * (N + 1)
    queue.append(start)

    while queue:
        way = queue.pop(0)
        if not visited[way]: # 여기 조건을 설정해줌으로서, result를 처음부터 비울 수 있구나..
            visited[way] = 1
            result.append(way)
        for elem in node_dic[way]:
            if not visited[elem]:
                visited[elem] = 1
                result.append(elem)
                queue.append(elem)

    return result


TC = int(input())
for tc in range(1,TC+1):
    # N : 정점의 개수 / M : 간선의 개수 / 탐색 시작 정점 번호 : V
    N,M,V = list(map(int,input().split()))
    node_dic={}
    # node_dic을 정렬해줘야지, 문제에서 의도한대로 작은 숫자의 노드부터 방문하게 된다.
    # 만약에 높은 숫자부터 방문하라고 했으면 오름차순으로 만들어줬으면 되었을듯
    for start,goal in [list(map(int,input().split())) for _ in range(M)]:
        node_dic[start] = sorted(node_dic.get(start,[]) + [goal])
        node_dic[goal] = sorted(node_dic.get(goal,[]) + [start])

    print(node_dic)
    # DFS_ans =[]
    # DFS_recursive(V,[V])
    DFS_ans = list(map(str,DFS_recursive2(V,[])))
    BFS_ans = list(map(str,BFS(V)))
    # print('DFS',*DFS_ans)
    # print('DFS2',*DFS_recursive2(V))
    # print('BFS',*BFS_ans)
    print(' '.join(DFS_ans))
    print(' '.join(BFS_ans))

# 아니 백준 시발 이게 왜 키에러야!!!! 출력 잘되는데1!!
