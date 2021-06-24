# 1920번
# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

# 첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

import sys
sys.stdin = open('1920_input.txt','r')

# 기본적으로 이진탐색은 인덱스로 검사를 수행하므로, 원본 리스트를 건들이지 마라
def bin_search(start:int, end: int, lst:list,target_value:int):
    # start == end 인 경우에도 정답이 될 수 있다. --> 딱 중간에서 만났을때
    if start > end:
        return 0

    else:
        mid = (start+end)//2
        mid_value = lst[mid]
        if mid_value == target_value:
            return 1
        # 재귀로 돌리면 이미 검사한 mid는(idx)는 검사 범위에 안들어가게 해야한다
        # return 값을 재귀의 결과로 받아야한다. 함수가 스택에서 빠져나가면서 위로 return 결과를 들고 오기 때문.
        # 그렇지 않다면 그대로 검색 결과가 그대로 증발한다.
        elif mid_value > target_value:
            return bin_search(start,mid-1,lst,target_value)
        elif mid_value < target_value:
            return bin_search(mid+1,end,lst,target_value)


N = int(input())
num_lst = list(map(int,input().split()))
M = int(input())
target_num_lst = list(map(int,input().split()))

num_lst.sort()

for num in target_num_lst:
    print(bin_search(0,N-1,num_lst,num))