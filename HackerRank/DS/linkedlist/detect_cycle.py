"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""
class Node(object):
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next = next_node


def has_cycle(root):
	if not root:
		return False
	fast = root
	slow = root
	while True:
		slow = slow.next
		if not slow:
			break
		n = fast.next
		if not n:
			break
		fast = n.next
		if fast==slow:
			return True
	return False




def main():
	root = Node(1)
	root.next = Node(2)
	root.next.next = Node(3)
	root.next.next.next = root.next
	print(has_cycle(root))


if __name__ == '__main__':
	main()