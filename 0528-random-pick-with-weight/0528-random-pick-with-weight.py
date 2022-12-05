from random import random

class Solution:
    # F(x) ~ U(0,1)
    # random.random() ~ U(0,1)
    # [1], [0.1, 0.9, 1]

    def __init__(self, w: List[int]):
        total = sum(w)
        prefix_sum = 0
        self.cum_w = []
        for ele in w:
            prefix_sum += ele
            self.cum_w.append(prefix_sum / total)

    def pickIndex(self) -> int:
        r = random()
        for i in range(len(self.cum_w)):
            if r < self.cum_w[i]:
                return i


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()