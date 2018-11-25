

class Stack(object):

	def __init__(self):
		self._items = []

	
	def is_empty(self):
		return True if not self._items else False


	def insert(self,x):
		self._items.append(x)


	def pop(self):
		self._items.pop()


	def peek(self,x):
		return self._items[-1]

	def print(self):
		print(self._items)


def main():
	# s = Stack()
	# s.insert(1)
	# s.insert(2)
	# s.pop()
	# s.pop()
	# print(s.is_empty())
	# s.print()

if __name__ == '__main__':
	main()
