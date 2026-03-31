class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        sortedNums = sorted(nums)
        for i, val in enumerate(sortedNums):
            if i > 0 and val == sortedNums[i-1]:
                continue
            l, r = i+1, len(sortedNums)-1
            while l < r:
                threeSum = sortedNums[l] + sortedNums[r] + val

                if threeSum > 0:
                    r-=1
                elif threeSum < 0:
                    l+=1
                else:
                    res.append([val, sortedNums[l], sortedNums[r]])
                    r -=1
                    l +=1
                    while sortedNums[l] == sortedNums[l-1] and l<r:
                        l+=1

        return res
            
