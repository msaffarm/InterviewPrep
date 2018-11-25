import sys

class Node(object):
	def __init__(self):
		self.right = None
		self.left = None
		self.data = None


def checkBST(root):
	pass


def main():
	root = Node()
	root.data = 1
	a = Node()
	a.data = 2
	root.right = a
	b = Node()
	b.data = 0
	root.left = b
	print(sys.maxsize)



if __name__ == '__main__':
	main()