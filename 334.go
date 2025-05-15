package main
import "fmt"
import "math"

func increasingTriplet(nums []int) bool {
    first, second := math.MaxInt, math.MaxInt
    for i, _ := range(nums){
        if nums[i] <= first {
            first = nums[i]
        } else if nums[i] <= second {
            second = nums[i]
        } else {
            return true
        }
    }
    return false
}


func main() {
}
