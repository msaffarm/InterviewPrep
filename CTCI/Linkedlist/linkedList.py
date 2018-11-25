class Node(object):
	def __init__(self,data=None):
		self.next = None
		self.prev = None
		self.data = data


class LinedList():

	def __init__(self):
		self.head = None
		self.size = 0


	def insert(self,n):
		node = Node(n)
		if not self.head:
			self.head = node
		else:
			cur = self.head
			while cur.next:
				cur = cur.next
			cur.next = node


	def delete(self,n):
		cur = self.head
		prev = None
		while cur:
			if cur.data==n:
				if not prev:
					self.head = cur.next
				else:
					prev.next = cur.next
			prev = cur
			cur = prev.next



	def search(self,n):
		cur = self.head
		while cur:
			if cur.data ==n:
				return cur
			cur = cur.next
		return None


	def __str__(self):
		cur = self.head
		path = ""
		while cur:
			path += str(cur.data) + " "
			cur = cur.next
		return path


def main():
	l = LinedList()
	l.insert(1)
	l.insert(2)
	l.insert(4)
	l.insert(9)
	l.insert(10)
	print(l)
	l.delete(1)
	print(l)


if __name__ == '__main__':
	main()