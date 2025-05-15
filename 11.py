class Solution(object):
    def maxArea(self, height):
        l,r = 0, len(height)-1
        maxVolume = 0
        while l < r:
            v = min(height[l], height[r]) * (r-l)
            if v > maxVolume:
                maxVolume = v
                # print(f"maxVolume={v}, l={l}, r={r} = ({height[l]},{height[r]})")
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        
        return maxVolume


if __name__ == '__main__':
    s = Solution()
    height = [1,8,6,2,5,4,8,3,7]
    print(s.maxArea(height))

