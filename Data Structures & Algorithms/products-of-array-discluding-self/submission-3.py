class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        #nums = [1,2,4,6]
        #res = [1,1,1,1]
        prefix = 1
        
        #[1, 1, 2, 8]
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        #[, , 8, 8]
        postfix = 1
        for j in range(n-1, -1, -1):
            res[j] *= postfix
            postfix *= nums[j] 

        return res

