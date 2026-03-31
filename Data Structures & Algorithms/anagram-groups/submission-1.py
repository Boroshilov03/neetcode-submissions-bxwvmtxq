from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # A dictionary to map sorted string to list of anagrams
        word_dict = {}

        for word in strs:
            sorted_word = sorted(word)
            str_word = "".join(sorted_word)
            if str_word not in word_dict:
                word_dict[str_word] = []
            word_dict[str_word  ].append(word)

        return list(word_dict.values())

