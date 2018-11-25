# Given a Binary Search Tree (BST), convert it to a Greater Tree such
# that every key of the original BST is changed to the original key
# plus sum of all keys greater than the original key in BST.

# Example:

# Input: The root of a Binary Search Tree like this:
#               5
#             /   \
#            2     13

# Output: The root of a Greater Tree like this:
#              18
#             /   \
#           20     13
######################################################################
from collections import deque

class Node(object):
	def __init__(self,val=None):
		self.val = val
		self.right = None
		self.left = None


class Solution(object):
	def convertBST(self,root):
		self.sum = 0

		def reverse_inorder(root):
			if not root:
				return
			reverse_inorder(root.right)
			self.sum += root.val
			root.val = self.sum
			reverse_inorder(root.left)
		
		reverse_inorder(root)
		return root


	def stack_solution(self,root):
		stack = deque()
		



# mutable default argument!!!
# check this:http://docs.python-guide.org/en/latest/writing/gotchas/
def get_inordered_list(root,l):
	if not root:
		return
	get_inordered_list(root.left,l)
	l.append(root.val)
	get_inordered_list(root.right,l)
	return l


def stack_inorder(root,l):
	stack = deque()
	stack.append(root)
	visited = set()
	while stack:
		cur_node = stack[-1]
		if cur_node.left and cur_node.left not in visited:
			stack.append(cur_node.left)
		else:
			stack.pop()
			l.append(cur_node.val)
			if cur_node.right and cur_node.right not in visited:
				stack.append(cur_node.right)
		visited.add(cur_node)

	return l


def main():
	root = Node(2)
	root.right = Node(3)
	root.left = Node(0)
	root.left.right = Node(1)
	root.left.left = Node(-4)
	l = []
	print(stack_inorder(root,l))
	l = []
	# s = Solution()
	# s.convertBST(root)
	print(get_inordered_list(root,l))



if __name__ == '__main__':
	main()