# Given a binary tree, you need to compute the length of the diameter of
# the tree. The diameter of a binary tree is the length of the longest path
# between any two nodes in a tree. This path may or may not pass through the root.

# Example:
# Given a binary tree 
#           1
#          / \
#         2   3
#        / \     
#       4   5    
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

# Note: The length of path between two nodes is represented by the number
# of edges between them.
###############################################

class Node(object):
	def __init__(self,val=None):
		self.val = val
		self.right = None
		self.left = None


class Solution(object):
 	def diameterOfBinaryTree(self,root):
 		self.len_max_path = 0

 		def dfs(root):
 			if not root:
 				return 0
 			max_right,max_left = dfs(root.right),dfs(root.left)
 			max_right+=1 if root.right else 0
 			max_left+=1 if root.left else 0
 			self.len_max_path = max(self.len_max_path,max_right+max_left)
 			return max(max_left,max_right)

 		dfs(root)
 		return self.len_max_path


def print_inorder(root):
	if not root:
		return ""
	print_inorder(root.right)
	print(root.val,end="")
	print_inorder(root.left)


def main():
	root = Node(1)
	root.right = Node(2)
	root.left = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)
	print_inorder(root)
	# s = Solution()
	# print(s.diameterOfBinaryTree(root))


if __name__ == '__main__':
 	main()