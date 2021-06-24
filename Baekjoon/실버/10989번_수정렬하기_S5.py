#N개의 수가 주어졌을 때 이를 오름차순으로 정렬하는 프로그램을 작성하시오
import sys

sys.stdin = open('10989_input.txt','r')
input = sys.stdin.readline
N = int(input())
zero_lst = [0 for i in range(10000+1)] # 입력되는 숫자의 최대값이 10000 이므로 0~10000를 표시할 수 있는 크기로 만든다.
for i in range(N):
    zero_lst[int(input())] += 1 # 입력된 숫자를 인덱스 삼아서 zero_lst의 요소를 1씩 증가시킨다

for idx in range(10000+1):
    for i in range(zero_lst[idx]):
        print(idx)