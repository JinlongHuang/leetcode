import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = Counter(words)
        return heapq.nsmallest(k, cnt.keys(), key=lambda x: (-cnt[x], x))

