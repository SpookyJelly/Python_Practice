# 9934번
# 완전 이진트리를 중위 순회하였을때, 각 레벨 별로 있는 노드의 번호를 구하라
import sys
sys.stdin = open('9934_input.txt','r')
depth = int(input())
order = list(map(int,input().split()))

tre = [[]*depth for _ in range(depth+1)]



while depth != 1:
    removelst =[]
    for idx in range(len(order)):
        if idx%2 != 1:
            tre[depth].append(order[idx])
            removelst.append(order[idx])

    for elem in removelst:
        order.remove(elem)


    depth -= 1

tre[depth].append(order.pop())
for i in range(1,len(tre)):
    for j in range(len(tre[i])):
        print(tre[i][j],end=' ')
    print()

