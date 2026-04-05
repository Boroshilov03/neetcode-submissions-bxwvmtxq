# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #If both heads missing return None
        #If one of the heads is missing return the other
        #Iterate though through the smallest head or at the same time until one is empty or both
        #Append rest of the head to the res
        if not list1 and not list2:
            return None

        if not list1:
            return list2
        
        if not list2:
            return list1


        curr = ListNode(0)
        res = curr
        #list1 = [1,2,4], list2 = [1,3,5]
        #        
        #0 -> 1 (list1) ->
        while list1 and list2:
            if list1.val > list2.val:
                curr.next = list2
                list2 = list2.next
            else:
                curr.next = list1
                list1 = list1.next
            curr = curr.next

        curr.next = list1 or list2

        return res.next
