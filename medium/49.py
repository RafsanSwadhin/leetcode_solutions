# 49. Group Anagrams
from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for i in strs:
            lst = [0] * 26
            for c in i:
                lst[ord(c) - ord("a")] += 1
            res[tuple(lst)].append(i)
        return list(res.values())
