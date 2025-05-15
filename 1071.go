package main
import (
    "strings"
	"fmt"
)

func gcdRecursive(str1 string, str2 string, prev string) string{
    if len(str1) < len(str2) {
        return gcdRecursive(str2, str1, prev)
    }
    i, j := 0,0
    for ; i < len(str1) ;  {
        if str1[i] == str2[j] {
            i++
            j++
            if j >= len(str2) {
                j = 0
            }
        } else {
            return ""
        }
    }
    gcd := str2[j:]
    // fmt.Println("GCD=",gcd)
    // fmt.Println("prev=",prev)
    if len(gcd) == 0 || strings.Compare(prev, gcd) == 0 {
        return prev
    }
    prev = gcd
    return gcdRecursive(str2, gcd, prev)    
}

func gcdOfStrings(str1 string, str2 string) string {
    return gcdRecursive(str1, str2, "")
}


func main(){
	str1 := "ABABABAB"
	str2 := "ABAB"
	ret := gcdOfStrings(str1, str2)
	fmt.Println(ret)	
}