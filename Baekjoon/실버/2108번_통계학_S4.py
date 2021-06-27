#2108번
# 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.

# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이

import sys
sys.stdin=open('2108_input.txt','r')
input = sys.stdin.readline

def define_avg (base_lst:list,length:int):
    total = 0
    for item in base_lst:
        for idx in range(item[0]):
            total += item[1]
    return round(total / length)

def define_median(base_lst:list,mid_index:int):
    mid_index=mid_index
    for item in base_lst:
        if item[0]:
            mid_index -= item[0]
            if mid_index <0:
                return item[1]
       
def define_mode(base_lst:list,max_frequency:int):
    max_frequency = max_frequency
    mode_lst = []
    for item in base_lst:
        if item[0] == max_frequency:
            mode_lst.append(item)
    if len(mode_lst) == 1:
        return mode_lst[0][1]
    else:
        return mode_lst[1][1]

def define_range(base_lst:list):
    v_list = []
    for item in base_lst:
        if item[0]:
            v_list.append(item[1])
    return max(v_list) - min(v_list)

N = int(input())

base_lst = [[0, i] for i in range(-4000,4001)]

for _ in range(N):
    base_lst[4000+int(input())][0] += 1
max_frequency = max(base_lst)[0]

print(define_avg(base_lst,N))
print(define_median(base_lst,N//2))
print(define_mode(base_lst,max_frequency))
print(define_range(base_lst))
