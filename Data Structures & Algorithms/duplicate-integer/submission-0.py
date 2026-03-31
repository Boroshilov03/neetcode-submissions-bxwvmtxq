class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        emptyList = []
        n = len(nums)
        for i in range(n):
            if nums[i] not in emptyList:
                emptyList.append(nums[i])
            else:
                return True
        return False
