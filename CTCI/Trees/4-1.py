class Node(object):
	def __init__(self):
		self.data = None
		self.right = None
		self.left = None


def calc_height(root):
	if not root:
		return 0
	if abs(calc_height(root.right)-calc_height(root.left))>1:
		return -1
	return max(calc_height(root.right),calc_height(root.left)) + 1 


def main():
	pass


if __name__ == '__main__':
	main()
