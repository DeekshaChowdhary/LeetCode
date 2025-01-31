# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Create a dummy node to simplify handling the merged list
        dummy = ListNode(-1)
        current = dummy
        
        # Traverse through both lists while both are not empty
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # If one of the lists is not empty, append the remaining nodes
        current.next = list1 if list1 else list2
        
        # Return the merged list starting from the next node after dummy
        return dummy.next
