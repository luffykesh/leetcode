package main
import (
    "fmt"
)

func canPlaceFlowers(flowerbed []int, n int) bool {
	availableBeds := 0
	if n == 0 {
		return true
	}
	if len(flowerbed) == 1 {
		if flowerbed[0] == 0 {
			return true
		} else {
			return false
		}
	}
	for i := 0; i < len(flowerbed); i++ {
		if flowerbed[i] == 0 {
			if i == 0 {
				if flowerbed[i+1] == 0 {
					availableBeds += 1
					flowerbed[i] = 1
				}
			} else if i == len(flowerbed)-1 {
				if flowerbed[i-1] == 0 {
					availableBeds += 1
					flowerbed[i] = 1
				}
			} else if flowerbed[i-1] == 0 {
				if flowerbed[i+1] == 0 {
					availableBeds += 1
					flowerbed[i] = 1
				}
			}
		}
		if availableBeds >= n {
			return true
		}
	}
	return false
}

func main() {
    flowerbed := []int{1,0,0,0,0,1}
    n := 2
    res := canPlaceFlowers(flowerbed, n)
    fmt.Println(res)
}

