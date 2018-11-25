from random import randint
class ListNode(object):

	def __init__(self,x):
		self.val = x
		self.next = None

class Solution(object):

	def __init__(self,head):
		self.head = head


	def getRandom(self):
		selected = []
		k = 1
		cur_node = self.head
		i = 0
		while cur_node:
			if i < k:
				selected.append(cur_node.val)
			else:
				s = randint(0,i)
				if s < k:
					selected[randint(0,k-1)] = cur_node.val
			cur_node = cur_node.next
			i+=1

		return selected[0]


def main():
	head = ListNode(1)
	head.next = ListNode(6)
	head.next.next = ListNode(10)
	s = Solution(head)
	print(s.getRandom())


if __name__ == '__main__':
	main()