# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node to account for edge cases
        dummy = ListNode()
        tail = dummy

        # If not null (empty)
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1 # make node for new list
                # Then move to the next node 
                list1 = list1.next
            else: 
                tail.next = list2
                list2 = list2.next
            
            tail = tail.next # Advances tail to node we just attached
        
        # Need to see for case if one listnode is empty
        # If list1 is NOT null (still continuing)
        # Append the ones left to end of list
        if list1:
            tail.next = list1
        elif list2: 
            tail.next = list2

        return dummy.next
        

        




    

