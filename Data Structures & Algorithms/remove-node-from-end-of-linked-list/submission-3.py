# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#[1,2,3,4,5] n = 1
#[1,2,3,4]

#[1,2,3,4,5] n = 2
#[1,2,3,5]
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and n>0:
            fast = fast.next
            n-=1

        if not fast:
            return head.next

        while fast.next:
            slow = slow.next
            fast = fast.next 
        
        slow.next = slow.next.next

        return head
