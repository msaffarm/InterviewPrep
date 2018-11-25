
# Given an array where elements are sorted in ascending order, convert it to a
# height balanced BST.

# For this problem, a height-balanced binary tree is defined as a binary tree in which
 # the depth of the two subtrees of every node never differ by more than 1.


# Example:

# Given the sorted array: [-10,-3,0,5,9],

# One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

#       0
#      / \
#    -3   9
#    /   /
#  -10  5
############################
class Node(object):
	def __init__(self,val=None):
		self.val = val
		self.right = None
		self.left = None


class Solution(object):
	def sortedArrayToBST(self,nums):
		if not nums:
			return None
		return self.createBST(nums,0,len(nums)-1)

	def createBST(self,nums,head,tail):
		if head==tail:
			return Node(nums[head])
		mid=(head+tail)//2
		root = Node(nums[mid])
		if mid<tail:
			root.right = self.createBST(nums,mid+1,tail)
		if mid>head:
			root.left = self.createBST(nums,head,mid-1)
		return root


def main():
	sol = Solution()
	l = list(range(10))
	print(l)
	r = sol.sortedArrayToBST(l)
	print(r.val)
	print(r.right.val)
	print(r.left.val)


if __name__ == '__main__':
	main()