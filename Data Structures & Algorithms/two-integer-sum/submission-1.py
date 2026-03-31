class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapVal = {}

        for i, val in enumerate(nums):
            secondVal = target - val
            if secondVal in mapVal.keys():
                return [mapVal[secondVal], i]
            mapVal[val] = i
        return []


