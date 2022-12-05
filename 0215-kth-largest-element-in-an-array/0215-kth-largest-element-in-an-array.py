import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # maintain a min heap of size k recording the largest k elements
        # outout root of the heap
        
        large = []
        n = len(nums)
        
        for i in range(n):
            if len(large) < k:
                heapq.heappush(large, nums[i])
            else:
                heapq.heappushpop(large, nums[i])
        
        return large[0]
        
        