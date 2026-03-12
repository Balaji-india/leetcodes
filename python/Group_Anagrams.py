class Solution(object):
    def groupAnagrams(self, strs):
        d1={}
        for words in strs:
            key="".join(sorted(words))
            if key not in d1:
                d1[key]=[]
            d1[key].append(words)
        return list(d1.values())
