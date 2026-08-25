class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        current = dummy 
        current_l1 = l1
        current_l2 = l2
        carry = 0

        while current_l1 is not None or current_l2 is not None or carry != 0:
            val1 = current_l1.val if current_l1 is not None else 0
            val2 = current_l2.val if current_l2 is not None else 0
            

            total = val1 + val2 + carry 
            digit = total - 10  

            if  total > 9 :
                current.next = ListNode(total - 10 )
                current = current.next
                carry = total // 10
            else  :
                current.next = ListNode(total)
                current = current.next
                carry = 0
                


            if current_l1 is not None:
                current_l1 = current_l1.next
            if current_l2 is not None:
                current_l2 = current_l2.next
            


        return dummy.next
                