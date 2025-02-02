# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def caminho (a, p):
    c = []
    while a != None and a != p:
        c.append(a)
        if a.val > p.val: a = a.left
        else: a = a.right
    c.append(p)
    return c 

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
    
        cp = caminho(root, p)
        cq = caminho(root, q)
        
        i = 0
        tam = len(cp) if len(cp) < len(cq) else len (cq)
        while i < tam and cp[i] == cq[i]:
            i += 1
        return cp[i - 1]
