package main
import (
    "fmt"
)

func productExceptSelf(nums []int) []int {
    ans := make([]int,len(nums))
    prefix, postfix := 1,1

    for i,_ := range(nums) {
        ans[i]=prefix
        prefix *= nums[i]
    }
    fmt.Println(ans)

    for i:=len(nums)-1; i >=0; i-- {
        ans[i]=postfix * ans[i]
        postfix *= nums[i]
    }
    fmt.Println(ans)

    return ans
}

func main() {
    nums := []int{1,2,3,4}
    ans := productExceptSelf(nums)
    fmt.Println(ans)
}

