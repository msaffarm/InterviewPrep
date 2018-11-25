class Node(object):
	def __init__(self,d=None):
		self.data = d
		self.right = None
		self.left = None
		self.parent = None


def creat_bst(l):	
	if not l:
		return None
	if len(l)==1:
		return Node(l[0])

	i = len(l)//2
	n = Node(l[i])
	n.left = creat_bst(l[:i])
	n.right = creat_bst(l[i+1:])
	if n.left:
		n.left.parent = n
	if n.right:
		n.right.parent = n
	return n


def print_inorder(root):
	if not root:
		return
	print_inorder(root.left)
	print(root.data,end=' ')
	print_inorder(root.right)


def find_min(n):
	cur = n
	min_val = 0
	while n:
		min_val = n.data
		n = n.left
	return min_val


def find_next_inorder(n):
	if n.right:
		return find_min(n.right)

	while n.parent:
		if n.parent.data > n.data:
			return n.parent.data
		n = n.parent
	return None


def main():
	root = creat_bst(list(range(7)))
	# print_inorder(root)
	print(find_next_inorder(root.right.right))


if __name__ == '__main__':
	main()