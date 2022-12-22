class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        diff = [x - y for x, y in zip(gas, cost)]
        prefix_sum = []
        _sum = 0
        for ele in diff:
            _sum += ele
            prefix_sum.append(_sum)
        
        if prefix_sum[-1] < 0:
            return -1
        else:
            return (prefix_sum.index(min(prefix_sum)) + 1) % n