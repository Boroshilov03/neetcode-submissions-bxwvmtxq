class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numHash = {}

        for index, val in enumerate(nums):
            missingVal = target - val
            if missingVal in numHash:
                return [numHash[missingVal], index]
            numHash[val] = index
