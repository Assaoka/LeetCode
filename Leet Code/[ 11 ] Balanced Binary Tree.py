# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        def height (a):
            if a == None: return True

            esq = height(a.left)
            if esq == -1: return -1

            dir = height(a.right)
            if dir == -1: return -1

            if abs(esq - dir) > 1: return -1
            return max(esq, dir) + 1

        if height(root) != -1: return True
        return False
        