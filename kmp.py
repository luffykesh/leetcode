from typing import *

def calculateLps(part:  str) -> List[int]:
    i,j = 1,0
    lps = [0]*len(part)

    while i < len(part):
        if part[i]==part[j]:
            lps[i] = lps[j] + 1
            i += 1
            j += 1
        elif j == 0:
            lps[i] = 0
            i += 1
        else:
            j = lps[j-1]

    return lps

def kmp(s: str, part: str) -> List[int]:
    i, parti = 0,0
    lps = calculateLps(part)
    res = []    
    while i < len(s):
        if s[i] == part[parti]:
            i += 1
            parti += 1
            if parti == len(part):
                res.append(i - len(part))
                parti = lps[parti - 1]
        else:
            if parti == 0:
                i += 1
            else:
                parti = lps[parti - 1]

    return res

if __name__ == '__main__':
    part ='kpygkivtlqoocssnextkqzjpycbylkaonds'
    part = 'AAACAAAA'
    s = 'aabaacaadaabaaba'
    part = 'aaba'
    lps = calculateLps(part)
    print(lps)
    matches = kmp(s, part)
    print("matches=", matches)

