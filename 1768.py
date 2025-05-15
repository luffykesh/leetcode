class Solution:
	def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        merged = str()
        rem = str()
        while True:
            if i >= len(word1):
                rem = word2
                break
            if i >= len(word2):
		rem = word1
                break
	    merged += word1[i]
            merged += word2[i]
            i += 1
        while i < len(rem):
	    merged += rem[i]
            i+=1
	return merged
        

s = Solution()
print(s.mergeAlternately("abcd", "pq")

