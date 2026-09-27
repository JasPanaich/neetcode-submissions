# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque 

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque() 
        result = []

        if root:
            q.append(root)

        while len(q) > 0:
            level_size = len(q)
            for i in range (level_size):
                curr = q.popleft()
                if i == level_size - 1: # Last node at level
                    result.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

        return result




        