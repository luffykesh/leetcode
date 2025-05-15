class Solution:
    def longestOnes(self, nums,k):
        l,r = 0,0
        flipped = 0
        maxlen = 0
        windowlen = 0
        while l < len(nums) and r < len(nums):
            if nums[r] == 1:
                windowlen += 1
            else:
                if flipped < k:
                    flipped += 1
                    windowlen += 1
                else:
                    maxlen = windowlen if maxlen<windowlen else maxlen
                    while l<r and nums[l]==1:
                        l += 1
                    l+=1
                    windowlen = r-l+1 if k>0 else 0
            if r == len(nums)-1:
                break
            else:
                r += 1
            
        maxlen = windowlen if maxlen < windowlen else maxlen
        
        return maxlen

if __name__ == "__main__":
    s = Solution()
    nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
    k = 3
    print(s.longestOnes(nums,k))
    print()

