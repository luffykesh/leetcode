# same as 205
class Solution:
    def morph(self, itr):
        mp = {}
        l = []
        for i in range(len(itr)):
            if itr[i] not in mp:
                mp[itr[i]] = i
            l.append(mp[itr[i]])
        return tuple(l)

    def wordPattern(self, pattern: str, s: str) -> bool:
        patternMorph = self.morph(pattern)
        sMorph = self.morph(s.split(' '))

        print(patternMorph)
        print(sMorph)

        return patternMorph == sMorph

