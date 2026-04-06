class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = fast = dummy

        # Move fast n+1 steps
        for _ in range(n + 1):
            fast = fast.next

        # Move both
        while fast:
            slow = slow.next
            fast = fast.next

        # Remove node
        slow.next = slow.next.next

        return dummy.next