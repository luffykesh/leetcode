class Solution:
    def morph(self,s) -> Tuple[int]:
        mp = {}
        l = []
        for i in range(len(s)):
            if s[i] not in mp:
                mp[s[i]] = i
            l.append(mp[s[i]])
        return tuple(l)

    def isIsomorphic(self, s: str, t: str) -> bool:
        smorph = self.morph(s)
        tmorph = self.morph(t)
        
        return smorph == tmorph

