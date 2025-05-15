class Solution(object):
    def  maxOperations(self,nums, k):
        required = {}
        count = 0
        for n in nums:
            if n >= k:
                continue
            if n in required:
                count+=1
                required[n] = required[n]-1
                if required[n]==0:
                    del required[n]
            else:
                required[k-n] = required.get(k-n,0)+1

        return count


if __name__ == "__main__":
    s = Solution()
    nums = [2,5,4,4,1,3,4,4,1,4,4,1,2,1,2,2,3,2,4,2]
    k = 3
    print(s.maxOperations(nums,k))

