# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        list_node = ListNode(0)
        sort_list = list_node

        sort_list1 = list1
        sort_list2 = list2
        
        while sort_list1 is not None and sort_list2 is not None:
            min_list1 = sort_list1.val
            min_list2 = sort_list2.val

            if min_list1 <= min_list2 :

                sort_list.next = ListNode(sort_list1.val)
                sort_list = sort_list.next
                sort_list1 = sort_list1.next
            else:

                sort_list.next = ListNode(sort_list2.val)
                sort_list = sort_list.next
                sort_list2 = sort_list2.next
            
        while sort_list1 is not None:
            sort_list.next = ListNode(sort_list1.val)
            sort_list = sort_list.next
            sort_list1 = sort_list1.next
        while sort_list2 is not None:
            sort_list.next = ListNode(sort_list2.val)
            sort_list = sort_list.next
            sort_list2 = sort_list2.next 

        return list_node.next
            



