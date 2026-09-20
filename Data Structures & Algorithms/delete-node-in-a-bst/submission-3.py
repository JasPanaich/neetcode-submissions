# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
    
# Return min value of node by going all the way left
def getMin(root):
    curr = root
    while curr and curr.left:
        curr = curr.left
    return curr

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # Base case: DNE or not in tree
        if not root:
            return None 

        # Search for key
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key) 
        else:
            # Key is found. Delete it

            # 0 or 1 child: make pointer look past node and to its children
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
                
            # If two children
            # Get smallest value of right subtree
            min_node = getMin(root.right)
            root.val = min_node.val # set root to this
            # delete value we just used to replace our key with
            root.right = self.deleteNode(root.right, root.val) 

        # tell parent to keep pointing here
        return root