package main
import "strconv"
import "fmt"

func compress(chars []byte) int {
    l := 0
    var g byte
    glen := 0
    g = chars[0]
    for _, c := range(chars) {
        if c == g {
            glen++
        } else {
            if glen > 1 {
                chars[l] = g
                l++
                l += copy(chars[l:], strconv.Itoa(glen))
            } else {
                chars[l] = g
                l++
            }
            g = c
            glen = 1
        }
    }

    chars[l] = g
    l++
    if glen > 1 {
        l += copy(chars[l:], strconv.Itoa(glen))
    } 

    return l
}

func main() {
    chars := []byte{'a','b','b','c','c','c'}
    l := compress(chars)
    fmt.Println("l=", l)
    fmt.Println(string(chars[0:l]))
}
