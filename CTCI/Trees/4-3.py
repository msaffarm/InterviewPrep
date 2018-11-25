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


def main():
	l = list(range(5))
	print(l)
	n = creat_bst(l)
	print(n.data)
	print(n.left.data)
	print(n.right.data)



if __name__ == '__main__':
	main()