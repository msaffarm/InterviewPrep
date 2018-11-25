# You are given two non-empty linked lists representing two non-negative integers. 
# digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero,
# except the number 0 itself.

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8


##########################

from random import randint

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def print(self):
        return_str = ""
        current_node = self
        while current_node!=None:
            return_str += str(current_node.val)
            current_node = current_node.next
        return return_str


    def print_recursive(self):

        if self.next==None:
            return str(self.val)
        return str(self.val) + self.next.print_recursive()


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = current_node = ListNode(0)
        carry_out = 0
        while l1 or l2 or carry_out:
            v1,v2 = 0,0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next

            dig, carry_out = (v1+v2+carry_out)%10, (v1+v2+carry_out)//10
            t = ListNode(dig)
            current_node.next = t
            current_node = t

        
        return head.next


def main():

    l1 = ListNode(5)
    l2 = ListNode(3)
    current_node_1 = l1
    current_node_2 = l2
    for _ in range(2):
        t_2 = ListNode(randint(0,9))
        current_node_2.next = t_2
        current_node_2 = t_2       
        t_1 = ListNode(randint(0,9))
        current_node_1.next = t_1
        current_node_1 = t_1

    # t = ListNode(7)
    # current_node_1.next = t
    print(l1.print())
    print(l2.print())

    # l1,l2
    s = Solution()
    res = s.addTwoNumbers(l1,l2)
    print(res.print())

if __name__ == '__main__':
    main()