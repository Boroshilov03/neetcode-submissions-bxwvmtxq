class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numsSet = set(nums)
        Maxcount = 1
        for num in nums:
            count = 1
            while num-count in numsSet:
                count += 1
                Maxcount = max(count, Maxcount)
        return Maxcount
    