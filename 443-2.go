package main
import "strconv"
import "fmt"

func compress(chars []byte) int {
    l := 0
    for i,j:=0,0 ; i<len(chars); {
        count := 0
        for j = i; j<len(chars) ; j++ {
            if chars[j] != chars[i] {
                break
            }
            count++
        }
        chars[l]=chars[i]
        l++
        if count > 1 {
            l += copy(chars[l:], strconv.Itoa(count))
        }
        i = j
    }

    return l
}

func main() {
    chars := []byte{'a','b','b','c','c','c','q'}
    l := compress(chars)
    fmt.Println("l=", l)
    fmt.Println(string(chars[0:l]))
}
