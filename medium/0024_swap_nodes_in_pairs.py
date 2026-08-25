# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None :
            return head
        
        dummy = ListNode(0)
        dummy.next = head

        pre = dummy
        # current = pre.next
        # fast = current.next

        while pre.next != None and pre.next.next != None:

            current = pre.next
            fast = pre.next.next

            pre.next = fast
            current.next = fast.next
            fast.next = current

            pre = current


        return dummy.next