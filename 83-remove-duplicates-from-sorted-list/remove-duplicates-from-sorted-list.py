# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current = head
        
        # Iterate through the linked list
        while current and current.next:
            # If the current node's value is the same as the next node, skip the next node
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        
        return head
