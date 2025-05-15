package main

import (
    "fmt"
    "slices"
)

func findGCD(nums []int) int {
    slices.Sort(nums)
    s := nums[0]
    l := nums[len(nums)-1]

    if l % s == 0 {
        return s
    }
    if s == 2 || s == 1{
        return 1
    }
    
    for i := s-1; i>0; i-- {
        if s % i == 0 && l % i == 0 {
            return i
        }
    }

    return 1
}

func main() {
    nums := []int{2,5,6,9,10}
    gcd := findGCD(nums)
    fmt.Println(gcd)
}

