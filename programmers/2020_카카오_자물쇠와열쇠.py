#2020 카카오_자물쇠와 열쇠

# 고고학자인 "튜브"는 고대 유적지에서 보물과 유적이 가득할 것으로 추정되는 비밀의 문을 발견하였습니다. 
# 그런데 문을 열려고 살펴보니 특이한 형태의 자물쇠로 잠겨 있었고 문 앞에는 특이한 형태의 열쇠와 함께 자물쇠를 푸는 방법에 대해 
# 다음과 같이 설명해 주는 종이가 발견되었습니다.

# 잠겨있는 자물쇠는 격자 한 칸의 크기가 1 x 1인 N x N 크기의 정사각 격자 형태이고 
# 특이한 모양의 열쇠는 M x M 크기인 정사각 격자 형태로 되어 있습니다.

# 자물쇠에는 홈이 파여 있고 열쇠 또한 홈과 돌기 부분이 있습니다. 
# 열쇠는 회전과 이동이 가능하며 열쇠의 돌기 부분을 자물쇠의 홈 부분에 딱 맞게 채우면 자물쇠가 열리게 되는 구조입니다. 
# 자물쇠 영역을 벗어난 부분에 있는 열쇠의 홈과 돌기는 자물쇠를 여는 데 영향을 주지 않지만, 
# 자물쇠 영역 내에서는 열쇠의 돌기 부분과 자물쇠의 홈 부분이 정확히 일치해야 하며 열쇠의 돌기와 자물쇠의 돌기가 만나서는 안됩니다. 
# 또한 자물쇠의 모든 홈을 채워 비어있는 곳이 없어야 자물쇠를 열 수 있습니다.
# 열쇠를 나타내는 2차원 배열 key와 자물쇠를 나타내는 2차원 배열 lock이 매개변수로 주어질 때, 
# 열쇠로 자물쇠를 열수 있으면 true를, 열 수 없으면 false를 return 하도록 solution 함수를 완성해주세요.

import copy
def rotate(key,m):
    tem_key = copy.deepcopy(key)
    for i in range(m):
        for j in range(m):
            tem_key[i][j] = key[m-1-j][i]
    return tem_key
    

def test(key,lock,i,j,m,n):
    dump = copy.deepcopy(lock)
    # p는 m만큼 (key의 크기만큼만 반복). 단 그 시작 위치는 i에 따라 달라짐
    for p in range(i,i+m):
        if 0<=p<n:
            # k도 m 만큼만 반복 <-- test 함수 자체가 key의 크기만큼만 돈다.
            for k in range(j,j+m):
                if 0<=k<n:
                    dump[p][k] += key[p-i][k-j]
                    # 밑에꺼로 하면 왜 안될까??

                    # 0 + 0 <-- 이건 괜찮다. 무조건 False를 리턴하는 경우가 아님.
                    # 그래서 밑에 있는 코드가 오답인거
                    
                    # if dump[p][k] + key[p-i][k-j] != 1:
                    #     return False

    for line in dump:
        for item in line:
            if item != 1:
                return False
    
    return True


def solution(key, lock):
    m = len(key)
    n = len(lock)
    # 1. 자물쇠 회전하는 거 만들기 (rotate 함수)
    rotate_90 = rotate(key,m)
    rotate_180 = rotate(rotate_90,m)
    rotate_270 = rotate(rotate_180,m)
    key_lst = [key,rotate_90,rotate_180,rotate_270]
    # print(key_lst)
    #2. 각 키에 대하여 꼭 들어맞는지 확인
    # 싸그리 더한다. (M은 항상 N 이하니까. M만큼 돌면 되나?)
    # key의 4시 방향 타일과 lock의 11시 방향 타일만 매치시켰다고 할때,
    # key의 11시 방향 타일의 위치는 lock11시 타일이 0,0이라고 하면 (-(m+1),-(m+1))이다.
    # 모든 좌표를 다 양수로 바라보려고 해서 어려웠던것 같다. (정확히 말하면 key를 0,0으로)
    # 가끔은 발상을 전환하여, 음수 좌표 ~ 양수 좌표를 오가는 풀이방안도 연구해야겠다.
    for key in key_lst:
        for i in range(-(m-1),n):
            for j in range(-(m-1),n):
                if test(key,lock,i,j,m,n):
                    return True
    return False

key = [[0,0,0],[1,0,0],[0,1,1]]
lock = [[1,1,1],[1,1,0],[1,0,1]]

print(solution(key,lock))
