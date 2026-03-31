class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexValDict = dict()

        for i, val in enumerate(nums):
            diff = target - val
            if diff in indexValDict:
                return [indexValDict[diff], i]
            else:
                indexValDict[val] = i
        return []