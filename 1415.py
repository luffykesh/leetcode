from collections import List
class Solution:
    def getHappyString(self, n: int, k: int) -> str:

    def makeHappyStrings(self, n: int, k :int) -> List[str]:
        chars='abc'
        happy = ''
        happyStrings = set()
        i = 0

        for firstCharIdx in range(len(chars)):
            happy = chars[firstCharIdx]
            i = firstCharIdx + 1
            while True:
                if i >= n:
                    i = 0
                c = chars[i]

                if len(happy) == n:
                    if happy in happyStrings:
                        continue
                    happyStrings.append(happy)
                    happy = ''
                if c == happy[-1]:
                    continue

                happy += c
        return happyStrings
                    
