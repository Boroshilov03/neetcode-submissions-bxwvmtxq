class Solution:
    def groupAnagrams(self, strs: List[str]):
        word_dict = dict()
        res = []
        for word in strs:
            sorted_word = sorted(word)
            word_str = ("").join(sorted_word)
            if word_str not in word_dict:
                word_dict[word_str] = []
            word_dict[word_str].append(word)
        
        for anagramlist in word_dict.values():
            anagrams = []
            for word in anagramlist:
                anagrams.append(word)
            res.append(anagrams)

        return res