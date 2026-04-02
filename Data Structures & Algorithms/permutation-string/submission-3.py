class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #s1 = "abc", s2 = "lecabee"
        #dict = {a:1, b:1, c:1} = total 3
        #dict = {a:1, b:1, c:1, d:1} = total 3

        s1_dict, s2_dict = dict(), Counter()

        for i in range(len(s1)):
            s1_dict[s1[i]] = s1_dict.get(s1[i], 0) + 1

        l = 0
        for r in range(len(s2)):
            s2_dict[s2[r]] += 1

            if r - l + 1 > len(s1):
                s2_dict[s2[l]] -= 1
                if s2_dict[s2[l]] == 0:
                    del s2_dict[s2[l]]
                l+=1
            
            if s2_dict == s1_dict:
                return True

        return False
