class Solution:
    def longestSubarray(self, nums) -> int:
        l,r = 0,0
        deleted = False
        wlen = 0
        maxlen = 0
        for r  in range(0,len(nums)):
            if nums[r]==1:
                wlen += 1
            else:
                if not deleted:
                    deleted=True
                    # wlen += 1
                else:
                    maxlen = max(maxlen, wlen)
                    while nums[l]!=0 and l<r:
                        l += 1
                    l+=1
                    wlen = r-l
        if not  deleted:
            wlen = max(0, wlen-1)
        maxlen = max(maxlen, wlen)

        return maxlen

if __name__ == "__main__":
    s = Solution()
    nums = [1,1,1]
    print(s.longestSubarray(nums))
    print()

                
