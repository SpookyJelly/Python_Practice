# 이진 탐색 하기.

import sys
sys.stdin = open('binary_search.txt', 'r')


def bin_search(target: int, start, end):
    global answer
    if start > end:
        return None
    else:
        mid = (start + end) // 2

        if bin_lst[mid] == target:
            answer = mid+1
        elif bin_lst[mid] > target:
            bin_search(target, start, mid-1)
        elif bin_lst[mid] < target:
            bin_search(target, mid+1, end)


n = int(input())
bin_lst = list(map(int, input().split()))
target = int(input())
answer = "X"
bin_search(target, 0, n)
print(answer)
