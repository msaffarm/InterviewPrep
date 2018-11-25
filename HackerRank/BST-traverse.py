

class Node(object):
	def __init__(self):
		self.right = None
		self.left = None
		self.data = None

# DFS Traversal
def preOrder(root):

	print(root.data, end=" ")
	if root.left:
		preOrder(root.left)
	if root.right:
		preOrder(root.right)

def postOrder(root):
	
	if root.left:
		postOrder(root.left)
	if root.right:
		postOrder(root.right)
	print(root.data, end=" ")


def inOrder(root):

	if root.left:
		inOrder(root.left)
	print(root.data, end=" ")
	if root.right:
		inOrder(root.right)

# BFS Traversal

def add2Queue(node,q):
	if node.left:
		q.append(node.left)
	if node.right:
		q.append(node.right)


def levelOrder(root):
	queue = []
	print(root.data, end=" ")
	add2Queue(root,queue)
	while queue:
		current_node = queue.pop()
		print(current_node.data, end=" ")
		add2Queue(current_node,queue)


# HEIGHT
def getHeight(root):

	if not root:
		return -1
	return max(1+getHeight(root.left),1+getHeight(root.right))


# TOP VIEW!!
def printRight(root):
	print(root.data, end=" ")
	if root.right:
		printRight(root.right)

def printLeft(root):
	if root.left:
		printLeft(root.left)
	print(root.data, end=" ")

def topView(root):
	if root.left:
		printLeft(root.left)
	print(root.data,end= " ")

	if root.right:
		printRight(root.right)


def main():

	root = Node()
	root.data = 1
	n1 = Node()
	n1.data = 3
	root.left = n1
	n2 = Node()
	n2.data = 5
	root.right = n2

	levelOrder(root)



if __name__ == '__main__':
	main()