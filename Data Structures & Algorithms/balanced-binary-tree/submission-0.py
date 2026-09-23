class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def traverse(node):
            if not node:
                return 0 # Height of empty tree is zero
            
            # Check left subtree
            left = traverse(node.left)
            if left == -1:
                return -1 # Not balanced
            
            # Check right subtree
            right = traverse(node.right)
            if right == -1:
                return -1 # Not balanced
            
            # Check if current node is balanced
            if abs(left - right) > 1:
                return -1
            
            # Return the height of the current node
            return 1 + max(left, right)
        
        # Call the helper and check if the result is valid
        return traverse(root) != -1