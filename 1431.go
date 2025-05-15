package main
import (
    "fmt"
)
func kidsWithCandies(candies []int, extraCandies int) []bool {
    result := make([]bool, len(candies))
    maxCandiesInHand := 0

    for i := 0; i<len(candies); i++ {
	if candies[i] > maxCandiesInHand {
	    maxCandiesInHand = candies[i]
	}
    }
    
    for i := 0; i<len(candies); i++ {
	if candies[i] + extraCandies >= maxCandiesInHand {
	    result[i] = true
	} else {
	    result[i] = false
	}
    }
    return result
}

func main() {
    candies := []int{2,3,5,1,3}
    var extraCandies int = 3
    result := kidsWithCandies(candies, extraCandies)
    fmt.Println(result)
}
