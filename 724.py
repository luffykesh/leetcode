class Solution:
    def pivotIndex(self, nums):
        total = sum(nums)
        lsum, rsum = 0,0
        for i in range(len(nums)):
            if i == 0:
                lsum = 0
            else:
                lsum = lsum + nums[i-1]

            rsum = total - lsum - nums[i]
            if lsum == rsum:
                return i

        return -1

if __name__=="__main__":
    s = Solution()
    nums = [1,2,3]
    i = s.pivotIndex(nums)
    print(i)
    print()

