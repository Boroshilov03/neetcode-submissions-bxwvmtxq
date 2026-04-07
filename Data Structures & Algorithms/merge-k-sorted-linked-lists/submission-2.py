

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]):
        nums = []
        res = ListNode(0)
        res_cur = res
        for head in lists:
            curr = head
            while curr:
                nums.append(curr.val)
                curr = curr.next
        sorted_nums = sorted(nums)
        for num in sorted_nums:
            res_cur.next = ListNode(num)
            res_cur = res_cur.next
        
        return res.next
