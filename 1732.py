class Solution:
    def largestAltitude(self, gain):
        maxAl = 0
        al = 0
        for g in gain:
            al += g
            maxAl = al if al > maxAl else maxAl
        return maxAl

if __name__ == "__main__":
    s = Solution()
    gain = [-4,-3,-2,-1,4,3,2]
    al = s.largestAltitude(gain)
    print(al)
    print()

