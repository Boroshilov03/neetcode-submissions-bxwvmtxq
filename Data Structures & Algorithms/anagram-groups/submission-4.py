
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]):
        word_dict = defaultdict(list)

        # char_count = [0] * 26 #from a (97) - z 
        
        for word in strs:
            char_count = [0] * 26 #from a (97) - z 

            for char in word:
                index = ord(char) - ord('a')
                char_count[index] += 1
            word_dict[tuple(char_count)].append(word)
        return list(word_dict.values())