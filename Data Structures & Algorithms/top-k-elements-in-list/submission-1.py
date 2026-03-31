class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Hashmap, array
        #Initialize
        num_count = {}
        res = []
        freq = [[] for i in range(len(nums)+1)]
        for num in nums:
            num_count[num] = 1 +num_count.get(num, 0)
        
        for key, value in num_count.items():
            freq[value].append(key)

        for i in range(len(nums),0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res


        