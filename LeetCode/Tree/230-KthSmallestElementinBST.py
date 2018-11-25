# Given a binary search tree, write a function kthSmallest to find the kth smallest
# element in it.

# Note: 
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

# Follow up:
# What if the BST is modified (insert/delete operations) often and you need to
# find the kth smallest frequently? How would you optimize the kthSmallest routine?
#####################################################################################
class TreeNode(object):
    def __init__(self,x=None):
        self.val = x
        self.right = None
        self.left = None


class Solution(object):
    def kthSmallest(self,root,k):
    	self.counter=0
    	self.val=None
    	self.find_kth_smallest(root,k)
    	return self.val

    def find_kth_smallest(self,root,k):
    	if not root:
    		return
    	self.find_kth_smallest(root.left,k)
    	self.counter += 1
    	if self.counter==k:
    		self.val=root.val
    	if self.counter < k:
    		self.find_kth_smallest(root.right,k)


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
    print(sol.kthSmallest(root,2))


if __name__ == '__main__':
    main()