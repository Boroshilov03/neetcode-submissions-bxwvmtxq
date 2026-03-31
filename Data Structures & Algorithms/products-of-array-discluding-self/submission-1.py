class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Ex where nums: [1,2,3,4]
        #Initialize the array: [1, 1, 1, 1]
        res = [1] * len(nums)

        #Prefix precompute]
        #res = [1, 1, 2, 6]
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        #res = [,,,,6]
        postfix = 1
        for j in range(len(nums)-1, -1, -1):
            res[j] *= postfix
            postfix *= nums[j]
        
        return res