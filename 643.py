class Solution(object):
    def findMaxAverage(self, nums, k):
        n = len(nums)
        if n < k:
            return None
        rollingSum = sum(nums[0:k])
        rollingMean = rollingSum/k
        maxMean = rollingMean
        for i in range(1, n-k+1):
            rollingSum = rollingSum - nums[i-1] + nums[i+k-1]
            rollingMean = rollingSum/k
            print(f"{nums[i:i+k]}, {rollingSum}/{k}={rollingMean}")
            if rollingMean > maxMean:
                maxMean = rollingMean
        
        return maxMean

if __name__ == "__main__":
    s = Solution()
    nums = [0,1,1,3,3]
    k = 4
    print(s.findMaxAverage(nums,k))
    print()

