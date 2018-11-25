# Given a binary tree, find the length of the longest path where eac
# h node in the path has the same value. This path may or may not pass through the root.

# Note: The length of path between two nodes is represented by the number
 # of edges between them.

# Example 1:

# Input:

#               5
#              / \
#             4   5
#            / \   \
#           1   1   5
# Output:2

# Example 2:

# Input:

#               1
#              / \
#             4   5
#            / \   \
#           4   4   5
# Output:2
###########################################################################

class Node(object):
	def __init__(self,val=None):
		self.val = val
		self.right = None
		self.left = None


class Solution(object):
	def longestUnivaluePath(self, root):
		self.longest = 0
		def dfs(root):
			if not root:
				return 0
			max_right,max_left = dfs(root.right),dfs(root.left)
			len_right = 1+max_right if root.right and root.right.val==root.val else 0
			len_left = 1+max_left if root.left and root.left.val==root.val else 0
			self.longest = max(self.longest,len_right+len_left)
			return max(len_left,len_right)
		dfs(root)
		return self.longest


def print_inorder(root):
	if not root:
		return ""
	print_inorder(root.left)
	print(root.val,end="")
	print_inorder(root.right)


def main():
	root = Node(2)
	root.right = Node(2)
	root.left = Node(2)
	root.left.left = Node(2)
	root.left.right = Node(2)
	print_inorder(root)
	s = Solution()
	c = s.longestUnivaluePath(root)
	print(c)

if __name__ == '__main__':
	main()
