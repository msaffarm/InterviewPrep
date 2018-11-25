# BST and BT implementation

class Node(object):

	def __init__(self,val=None):
		self.data = val
		self.right = None
		self.left = None


# BST impelmentation
class BST(object):

	def __init__(self):
		self.root = None


	def insert(self,val):

		current = self.root
		if not current:
			self.root = Node(val=val)
			return

		while True:
			if val > current.data:
				if current.right:
					current = current.right
				else:
					n = Node(val=val)
					current.right = n
					break

			elif val < current.data:
				if current.left:
					current = current.left
				else:
					n = Node(val=val)
					current.left = n
					break


	def get_root(self):
		return self.root


	def print_in_order(self,root):
		if not root:
			return
		self.print_in_order(root.left)
		print(root.data, end= " ")
		self.print_in_order(root.right)


	def print_pre_order(self,root):
		if not root:
			return
		print(root.data, end=" ")
		self.print_pre_order(root.left)
		self.print_pre_order(root.right)


	def get_max_val(self):

		current = self.root
		max_val = 0
		while current:
			max_val = current.data
			current = current.right
		return max_val


	def get_min_val(self):

		current = self.root
		min_val = 0
		while current:
			min_val = current.data
			current = current.left
		return min_val


# BT implementation!
class BT(object):

	def __init__(self):
		self.root = None


	def _is_balanced(self,s):
		if s.right and s.left:
			return True
		return False


	def insert(self,val):

		current = self.root
		if not current:
			self.root = Node(val=val)
			return

		queue = []
		queue.append(self.root)
		while queue:
			current = queue.pop(0)
			if self._is_balanced(current):
				if current.left.data!=None:
					queue.append(current.left)
				if current.right.data!=None:
					queue.append(current.right)
				continue
			
			if not current.left:
				n = Node(val=val)
				current.left = n
				break
			
			elif not current.right:
				n = Node(val=val)
				current.right = n
				break


	def get_root(self):
		return self.root


	def print_in_order(self,root):
		if not root:
			return
		self.print_in_order(root.left)
		if root.data!=None:
			print(root.data, end= " ")
		self.print_in_order(root.right)


	def print_pre_order(self,root):
		if not root:
			return
		if root.data!=None:
			print(root.data, end=" ")
		self.print_pre_order(root.left)
		self.print_pre_order(root.right)



def main():
	
	bst = BT()
	vals = [1,None,3,None,4,5,6,7,None,8,9]
	for x in vals:
		bst.insert(x)

	bst.print_in_order(bst.get_root())
	print()


if __name__ == '__main__':
	main()
