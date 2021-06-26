# 1654번 랜선자르기
# 첫째 줄에는 가지고 있는 랜선의 갯수 K , 필요한 랜선의 개수 N이 입력된다.
# K는 1이상 10,000이하의 정수이고, N은 1이상 1,000,000이하의 정수이다. 그리고 항상 K ≦ N 이다. 그 후 K줄에 걸쳐 이미 가지고 있는 각 랜선의 길이가 센티미터 단위의 정수로 입력된다.
import sys
sys.stdin = open('1654_input.txt','r')
input = sys.stdin.readline

def bin_search(left:int,right:int,goal:int)->int:
    ans = 0
    # 종료 조건을 while문으로 할때랑 재귀로 할때랑 조금 다르다. 기본 결은 left가 right보다 클 때 무조건 끝이 나야한다.
    while left <= right:
        mid = (left+right) // 2
        result = cnt_check(lan_lst,mid,goal)

        if result == "too short":
            ans = max(mid,ans)
            left = mid + 1
        else:
            right = mid -1

    return ans

def cnt_check(lan_lst:list,mid:int,goal:int):
    cnt = 0
    for lan in lan_lst:
        cnt += lan // mid
    
    if cnt >= goal:
        return "too short"
    else:
        return "too long"


K, N = map(int,input().split())
lan_lst= []
for _ in range(K):
    lan_lst.append(int(input()))

# print(lan_lst)

MAX_LAN_LEN = max(lan_lst)

print(bin_search(1,MAX_LAN_LEN,N))