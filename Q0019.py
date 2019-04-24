from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        pDelete = pTail = head
        for i in range(n):
            pTail = pTail.next
        if pTail is None:
            return head.next
        while pTail.next is not None:
            pTail = pTail.next
            pDelete = pDelete.next
        pDelete.next = pDelete.next.next
        return head





if __name__ == "__main__":
    result = Solution().removeNthFromEnd([-5,-4,-3,-2,1,3,3,5],
                                -11)
    print(result)


