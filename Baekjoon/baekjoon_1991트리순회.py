# 이진 트리를 입력 받아 전위순회, 중위 순회, 후위 순회 한 결과를 출력하시오


import sys

sys.stdin = open('1991_input.txt')


# lst[0] : value
# lst[1] : left_child
# lst[2] : right_child

def parentnode(alpha: str) -> int:
    for idx in range(len(tre)):
        if tre[idx][0] == alpha:
            return idx


def preorder(lst):
    global pre_result
    pre_result += lst[0]
    if lst[1] != '.':
        next = parentnode(lst[1])
        preorder(tre[next])
    if lst[2] != '.':
        next2 = parentnode(lst[2])
        preorder(tre[next2])
    return


def inorder(lst):
    global in_result
    if lst[1] != '.':
        next = parentnode(lst[1])
        inorder(tre[next])
    in_result += lst[0]
    if lst[2] != '.':
        next2 = parentnode(lst[2])
        inorder(tre[next2])
    return


def postorder(lst):
    global post_result
    if lst[1] != '.':
        next = parentnode(lst[1])
        postorder(tre[next])
    if lst[2] != '.':
        next2 = parentnode(lst[2])
        postorder(tre[next2])
    post_result += lst[0]


N = int(input())

tre = [[0, 0, 0] for _ in range(N)]
for i in range(N):
    tre[i] = list(input().split())

pre_result, in_result, post_result = '', '', ''
preorder(tre[0])
inorder(tre[0])
postorder(tre[0])
#######################
print(pre_result)
print(in_result)
print(post_result)
