package main
import "fmt"

func isSubsequence(s string, t string)bool {
    si, ti := 0,0
    for  ; si < len(s) && ti < len(t); ti++{
        if s[si] == t[ti] {
            si++
        }
    }
    
    if si >= len(s) {
        return true
    }

    return false
}

func main (){
    s:="abc"
    t:="ahbdc"
    fmt.Println(isSubsequence(s,t))
}
