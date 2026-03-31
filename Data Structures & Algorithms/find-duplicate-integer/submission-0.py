class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sum_value = sum(nums) #[1,2,3,2,2]
        set_value = sum(set(nums)) #[1,2,3]
        diff = sum_value - set_value
        diff_len = len(nums) - len(set(nums))
        ans = diff // diff_len
        return ans
        
        