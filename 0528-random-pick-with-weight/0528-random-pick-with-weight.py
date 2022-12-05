from random import random

class Solution:
    # F(x) ~ U(0,1)
    # random.random() ~ U(0,1)
    # [1], [1/3, 1], [0.1, 0.9, 1]

    def __init__(self, w: List[int]):
        self.total_sum = sum(w)
        prefix_sum = 0
        self.cum_w = []
        for ele in w:
            prefix_sum += ele
            self.cum_w.append(prefix_sum)

    def pickIndex(self) -> int:
        target = random() * self.total_sum
        n = len(self.cum_w)
        left, right = 0, n - 1
        
        while left < right:
            mid = left + (right - left) // 2
            if target > self.cum_w[mid]:
                left = mid + 1
            else:
                right = mid
        return left

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()