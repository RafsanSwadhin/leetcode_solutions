# top k frequent element

from collections import Counter
from typing import List  # Import List from the typing module

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        top_k = [x for x, _ in count.most_common(k)]
        return top_k
