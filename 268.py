class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = len(nums)
        low = 0
        high = n-1
        if nums[0] != 0:
            return low
        while low <= high:
            mid = low + (high-low)//2
            if mid != nums[mid] and mid-1 == nums[mid-1]:
                return mid
            if nums[mid] != mid:
                high = mid-1
            else:
                low = mid+1

        return n

