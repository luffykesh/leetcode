package main


import "fmt"

func calculateLps(part string) []int {
    lps := make([]int, len(part))
    i,j := 1,0
    for ; i < len(part) ; {
        if part[i] == part[j] {
            lps[i] = lps[j] + 1
            i +=1
            j +=1
        } else if j == 0 {
            lps[i] = 0
            i += 1
        } else {
            j = lps[j-1]
        }
    }

    return lps
}

func kmp(s string, part string) []int {
    matches := make([]int,0)
    i,j := 0,0
    lps := calculateLps(part)
    
    for ; i < len(s) ; {
        if s[i] == part[j]{
            i += 1
            j += 1
            if j == len(part) {
                idx := i - len(part)
                matches = append(matches, idx)
                j = lps[j-1]
            }
        } else if lps[j] == 0 {
            i += 1
        } else {
            j = lps[j-1]
        }
    }
    
    return matches
}

func main() {
    s := "kpygkivtlqoocskpygkpygkivtlqoocssnextkqzjpycbylkaondskivtlqoocssnextkqzjpycbylkaondssnextkqzjpycbylkaondshijzgaovndkjiiuwjtcpdpbkrfsi"
    part := "kpygkivtlqoocssnextkqzjpycbylkaonds"
    lps := calculateLps(part)
    fmt.Println("lps=",lps)
    matches := kmp(s, part)
    fmt.Println("matches=", matches)
}

