class Solution:
   def maxVowels(self, s, k):
        vowelCount = 0
        maxCount = 0
        vowels = {'a','e','i','o','u'}
        for i in range(0,len(s)):
            
            if i<k:
                if s[i] in vowels:
                    vowelCount+=1
                maxCount = vowelCount
                continue
            
            if s[i] in vowels:
                vowelCount += 1
            if s[i-k] in vowels:
                vowelCount -= 1
            maxCount = vowelCount if maxCount<vowelCount else maxCount
        
        return maxCount


if __name__ == "__main__":
    sol = Solution()
    s = "tryhard"
    k = 4
    print(sol.maxVowels(s,k))
    print()

