from collections import defaultdict,deque
class Solution:
    def getFreqMap(self, s)->Tuple[int]:
        count = [0]*26
        for c in s:
            count[97-ord(c)] += 1
        return tuple(count)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = defaultdict(deque)
        output = []
        for s in strs:
            freqmap = self.getFreqMap(s)
            anagramMap[freqmap].append(s)

        for _,anagrams in anagramMap.items():
            output.append(list(anagrams))

        return output

