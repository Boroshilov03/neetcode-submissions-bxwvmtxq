class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)

        max_length = 0

        for num in nums:
            l = 1
            if (num - 1) not in set_nums:
                while (num +l) in set_nums:
                    l+=1
                max_length = max(max_length, l)
        return max_length