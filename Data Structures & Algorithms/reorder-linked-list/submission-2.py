# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#Goal
#[0, 1, 2, 3]
#[4, 5, 6] -> [6, 5, 4]
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        #[0, 1, 2, 3, 4, 5, 6]
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #[0, 1, 2, 3, 4, 5, 6]
        #          s
        #                   r
        #Split
        head_second_list = slow.next
        slow.next = None
        curr = head_second_list
        # 0 -> 1-> 2 -> 3 -> None
        # 4 -> 5 -> 6 -> None
        prev = None 
        #None <- 4 <- 5 <- 6
        #Might be mistake
        while curr:
            temp = curr.next #5
            curr.next = prev #4
            prev = curr
            curr = temp

        first, second = head, prev
        # 0 -> 1-> 2 -> 3 -> None
        # 6 -> 5 -> 4 -> None
        while second:
            temp = first.next
            second_temp = second.next
            first.next = second
            second.next = temp
            first, second = temp, second_temp

            




        

        
            
             