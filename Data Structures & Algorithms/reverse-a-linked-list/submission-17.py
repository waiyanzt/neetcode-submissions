# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head #0
        prev = None
        
        while curr:
            next_node = curr.next #1
            curr.next = prev
            # the below should be the final action where curr pointer moves onto the next one
            prev = curr
            curr = next_node
        return prev

