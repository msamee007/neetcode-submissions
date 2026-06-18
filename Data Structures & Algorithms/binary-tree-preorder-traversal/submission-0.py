# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def preorder(r):
            if r==None:
                return 
            l.append(r.val)
            preorder(r.left)
            preorder(r.right)
        l=[]
        preorder(root)
        return l