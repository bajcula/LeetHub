# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        helper = ListNode(0, head)   
        preLeft, curr = helper, head
        
        for i in range(left - 1):
            preLeft, curr = curr, curr.next
            
        prev = None
        for i in range(right - left + 1):
            temp = curr.next
            curr.next = prev
            prev, curr = curr, temp
        
        preLeft.next.next = curr
        preLeft.next = prev
        
        return helper.next