class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #AAABABB k = 1
        # {A: 3, B: 1}
        # max = 3 total = 4
        # total (4) - max (3) = 1 <= k then we good


        # {A: 1, B:1, C: 1} k = 1
        #  Max = 1, total = 1
        # total (3) - max (1 ) <= 1

        res = 0

        char_count = dict()
        max_char_count = 0
        l= 0
        for r in range(len(s)):
            char = s[r]
            char_count[char] = char_count.get(char, 0) + 1
            max_char_count = max(max_char_count, char_count[char])

            while ((r - l + 1) - max_char_count > k):
                char_count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res
            
            
