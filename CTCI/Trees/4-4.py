class Node(object):
	def __init__(self,d=None):
		self.data = d
		self.right = None
		self.left = None



def creat_bst(l):
	
	if not l:
		return None
	if len(l)==1:
		return Node(l[0])

	i = len(l)//2
	n = Node(l[i])
	n.left = creat_bst(l[:i])
	n.right = creat_bst(l[i+1:])
	return n


def print_level(root):
	pass


def print_inorder(root):
	if not root:
		return
	print_inorder(root.left)
	print(root.data,end=' ')
	print_inorder(root.right)


def print_preorder(root):
	if not root:
		return
	print(root.data,end=' ')
	print_preorder(root.left)
	print_preorder(root.right)


def main():
	root = creat_bst(list(range(7)))
	# print_inorder(root)
	print_inorder(root)


if __name__ == '__main__':
	main()