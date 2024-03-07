from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursive
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if root is None:
#             return 0
#         else:
#             return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque()
        level = 0

        if root:
            q.append(root)

        while q:
            for _ in range(len(q)):
                current = q.popleft()
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
            level += 1
            
        return level


tree = [3,9,20,None,None,15,7]
tree = [TreeNode(e) if e is not None else None for e in tree]

tree[0].left = tree[1]
tree[0].right = tree[2]
tree[2].left = tree[5]
tree[2].right = tree[6]

out = Solution().maxDepth(tree[0])
print(out)