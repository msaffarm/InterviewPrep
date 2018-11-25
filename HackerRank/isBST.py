#interesting case!
# Case 1 :
#    20
#   /  \
#  10   2

# Case 2:
#    18
#   /  \
#  8    20
#      /  \
#     10  30
############################

class Node(object):
	def __init__(self):
		self.right = None
		self.left = None
		self.data = None


# def find_max(root):

# 	current = root
# 	max_val = 0
# 	while current:
# 		max_val = current.data
# 		current = current.right
# 	return max_val


# def find_min(root):

# 	current = root
# 	min_val = 0
# 	while current:
# 		min_val = current.data
# 		current = current.left
# 	return min_val


def check_binary_search_tree_(root):

	if not root:
		return True
	is_bst = True
	if root.left:
		if root.left.data >= root.data:
			is_bst = False
	if root.right:
		if root.right.data < root.data:
			is_bst = False

	return is_bst and check_binary_search_tree_(root.left) and check_binary_search_tree_(root.right)


def main():
	root = Node()
	root.data = 5
	n1 = Node()
	n1.data = 1
	root.left = n1
	n2 = Node()
	n2.data = 3
	root.right = n2
	print(check_binary_search_tree_(root))


if __name__ == '__main__':
	main()