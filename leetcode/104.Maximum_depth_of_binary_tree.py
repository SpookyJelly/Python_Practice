# Given the root of a binary tree, return its maximum depth.
#
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# 깊이를 측정하는데에는 여러 방법이 있지만 먼저 BFS를 이용해서 풀어보겠다.

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        if root is None:
            return 0
        que = deque([root])
        depth = 0
        # 큐 연산 추출 노드의 자식 노드 삽입
        while que:
            depth += 1
            for _ in range(len(que)):
                cur_root = que.popleft()
                if cur_root.left:
                    que.append(cur_root.left)
                if cur_root.right:
                    que.append(cur_root.right)

        return depth
