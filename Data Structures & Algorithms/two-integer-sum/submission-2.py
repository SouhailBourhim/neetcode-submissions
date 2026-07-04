class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        hashmap = {}
        for i,c in enumerate(nums):
            if (target - c) in hashmap:
                return  [hashmap[target - c],i]
            hashmap[c] = i
        return []