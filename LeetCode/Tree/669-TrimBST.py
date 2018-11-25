# Given a binary search tree and the lowest and highest boundaries as L and R,
# trim the tree so that all its elements lies in [L, R] (R >= L). You might need to
# change the root of the tree, so the result should return the new root of
# the trimmed binary search tree.

# Example 1:
# Input: 
#     1
#    / \
#   0   2

#   L = 1
#   R = 2

# Output: 
#     1
#       \
#        2
# Example 2:
# Input: 
#     3
#    / \
#   0   4
#    \
#     2
#    /
#   1

#   L = 1
#   R = 3

# Output: 
#       3
#      / 
#    2   
#   /
#  1
##############################################
class TreeNode(object):
    def __init__(self,x=None):
        self.val = x
        self.right = None
        self.left = None


class Solution(object):
    def trimBST(self, root, L, R):
        if not root:
            return
        if root.val > R:
            root = self.trimBST(root.left,L,R)
        elif root.val < L:
            root = self.trimBST(root.right,L,R)
        else:
            root.left = self.trimBST(root.left,L,R)
            root.right = self.trimBST(root.right,L,R)
        return root


def print_inorder(root):
    if not root:
        return
    print_inorder(root.left)
    print(root.val,end="")
    print_inorder(root.right)


def main():
    sol = Solution()
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)
    # print_inorder(root)
    L,R = 3,4
    root2 = sol.trimBST(root,L,R)
    print_inorder(root2)


if __name__ == '__main__':
    main()