from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        root = node = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1 :
                v1 = l1.val
                l1 = l1.next
            if l2 :
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1 + v2 + carry, 10)
            node.next = ListNode(val)
            node = node.next
        return root.next





if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    result = Solution().addTwoNumbers(l1, l2)
    while result:
        print(result.val)
        result = result.next




