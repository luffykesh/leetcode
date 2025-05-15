package main
import "fmt"

func moveZeroes(nums []int) {
    l,r := 0,0
    for ;  r<len(nums); r++ {
        if nums[r]!=0 {
            nums[l], nums[r] = nums[r],nums[l]
            l++
        }
    }
}


func moveZeroes1stAttempt(nums []int) {
    zeroi := -1
    for i:=0; i<len(nums); {
        for ; zeroi==-1 && i<len(nums); i++ {
            if nums[i] == 0 {
                zeroi = i
            }
        }
        for ;i<len(nums) && nums[i]==0; i++ { }

        if i < len(nums) {
            nums[zeroi],nums[i] = nums[i],nums[zeroi]
            i = zeroi + 1
            zeroi = -1
        }
    }
}

func main() {
    nums := []int{0,1,0,2,3}
    fmt.Println(nums)
    moveZeroes(nums)
    fmt.Println(nums)
}
