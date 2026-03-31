class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while l < r:
            sum_of_l_and_r = numbers[l] + numbers[r]
            if sum_of_l_and_r > target:
                r -=1
            elif sum_of_l_and_r < target:
                l +=1
            else:
                return  [l+1,r+1]
        return []