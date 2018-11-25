import heapq


class ListNode(object):
	def __init__(self,x):
		self.val = x
		self.next = None


class Solution(object):
	def mergeKLists(self,lists):
		sorted_head = ListNode(None)
		sorted_head_copy = sorted_head
		vals = [(x.val,x) for x in lists if x]
		heapq.heapify(vals)
		while vals:
			min_val,node = heapq.heappop(vals)
			sorted_head.next = ListNode(min_val)
			sorted_head = sorted_head.next
			next_node = node.next
			if next_node:
				heapq.heappush(vals,(next_node.val,next_node))

		return sorted_head_copy.next



def print_list(head):
	s = ""
	while head:
		s += str(head.val) + " "
		head = head.next
	print(s)


def main():
	head1 = ListNode(1)
	head1.next = ListNode(5)
	head2 = ListNode(3)
	head2.next = ListNode(10)
	head3 = ListNode(2)
	head3.next = ListNode(4)
	l = [head1,head2,head3]
	s = Solution()
	print_list(s.mergeKLists([]))


if __name__ == '__main__':
	main()