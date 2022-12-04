class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicts = {}
        
        for i in range(len(nums)):
            if not (target - nums[i]) in dicts:
                dicts[nums[i]] = i
            else:
                return dicts[target - nums[i]], i