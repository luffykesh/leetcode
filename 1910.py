class Solution:
    def calculateLps(self, part):
        i,j = 1,0
        lps = [0]*len(part)
        while i < len(part):
            if part[i] == part[j]:
                lps[i] = lps[i-1] + 1
                i += 1
                j += 1
            else:
                if j == 0:
                    lps[i] = 0
                    i += 1
                else:
                    j = lps[j - 1]
        
        return lps

    def removeOccurrences(self, s: str, part: str) -> str:
        flag = True
        output = s
        lps = self.calculateLps(part)
        while flag:
            output,flag = self.removeOnceKMP(output,part, lps)
            print("o=%s %s"%(output, flag))
            print()
        return output

    def removeOnceKMP(self, s, part, lps):
        output = ''
        i,j = 0,0
        flag = False
        window = ''
        while i < len(s):
            if s[i] == part[j]:
                window += s[i]
                i +=1
                j += 1
                print("window=%s"%(window))
                if j == len(part):
                    print("window matched")
                    j = lps[j-1]
                    window = ''
                    flag = True
            else:
                if j == 0:
                    i += 1
                    print("window broke=%s"%(window))
                    output += window
                    window = ''
                else:
                    j = lps[j-1]
                    print('streak broken, reset j = %d'%(j))
                    output += window[0:len(window)-j]
                    window = window[len(window)-j:]
                    print('output=%s, window=%s'%(output,window))

        return output, flag

                

        for c in s:
            if c != part[parti]:
                parti = 0
                output += window
                window = ''

            if c == part[parti]:
                window += c
                parti += 1
                print('window=%s'%(window))
                if window == part:
                    print('window match')
                    parti = 0
                    window = ''
                    flag=True
            else:
                print('window broke=%s, %s != %s'%(window, c, part[parti]))
                output += c
                window = ''
        output += window
        return output, flag
                
                  
if __name__ == "__main__":
    part = "kpygkivtlqoocssnextkqzjpycbylkaonds"
    s = "kpygkivtlqoocskpygkpygkivtlqoocssnextkqzjpycbylkaondskivtlqoocssnextkqzjpycbylkaondssnextkqzjpycbylkaondshijzgaovndkjiiuwjtcpdpbkrfsi"
    sol = Solution()
    op = sol.removeOccurrences(s, part)
    print("final=" ,op)

