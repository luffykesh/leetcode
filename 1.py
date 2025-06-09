class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i, n in enumerate(nums):
            required = target - n
            if required in nums_map:
                return [nums_map[required], i]
            if n not in nums_map:
                nums_map[n] = i
        return [-1, -1]

