package main

import (
    "fmt"
    "strconv"
    "slices"
)

func findDifferentBinaryString(nums []string) string {
    n := len(nums)
    intnums := make([]int64, n)
    for i:=0 ;i < len(nums); i++ {
        intnums[i], _ = strconv.ParseInt(nums[i], 2, 64)
    }
    slices.Sort(intnums)
    expected := int64(0)
    for _, n := range intnums {
        if n != expected {
            break
        }
        expected += 1
    }
    return fmt.Sprintf("%0*b",n, expected)
}

func main() {
    nums := []string{"111","011","001"}
    missing := findDifferentBinaryString(nums)
    fmt.Println(missing)
}

